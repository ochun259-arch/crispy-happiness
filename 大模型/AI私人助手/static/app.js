const STORAGE_KEY = "ai_assistant_sessions";
const CURRENT_KEY = "ai_assistant_current";

const messagesEl = document.getElementById("messages");
const welcomeScreen = document.getElementById("welcomeScreen");
const chatForm = document.getElementById("chatForm");
const messageInput = document.getElementById("messageInput");
const sendBtn = document.getElementById("sendBtn");
const newChatBtn = document.getElementById("newChatBtn");
const clearMemoryBtn = document.getElementById("clearMemoryBtn");
const historyList = document.getElementById("historyList");
const menuBtn = document.getElementById("menuBtn");
const sidebar = document.getElementById("sidebar");
const sidebarOverlay = document.getElementById("sidebarOverlay");

let sessionId = localStorage.getItem(CURRENT_KEY) || createSessionId();
let isLoading = false;

function createSessionId() {
  return `chat-${Date.now()}-${Math.random().toString(36).slice(2, 7)}`;
}

function getSessions() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
  } catch {
    return {};
  }
}

function saveSessions(sessions) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(sessions));
}

function getSessionMessages(id) {
  return getSessions()[id]?.messages || [];
}

function saveSessionMessages(id, messages, title) {
  const sessions = getSessions();
  sessions[id] = {
    title: title || sessions[id]?.title || "新对话",
    messages,
    updatedAt: Date.now(),
  };
  saveSessions(sessions);
  renderHistory();
}

function escapeHtml(text) {
  return text
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function renderMarkdown(text) {
  if (typeof marked !== "undefined") {
    return marked.parse(text, { breaks: true });
  }
  return escapeHtml(text).replaceAll("\n", "<br>");
}

function showChatArea() {
  welcomeScreen.classList.add("hidden");
  messagesEl.classList.remove("hidden");
  messagesEl.classList.add("active");
}

function appendMessage(role, text, { persist = true } = {}) {
  showChatArea();

  const row = document.createElement("div");
  row.className = `msg-row ${role}`;

  const avatar = document.createElement("div");
  avatar.className = "msg-avatar";
  avatar.textContent = role === "user" ? "我" : role === "assistant" ? "AI" : "!";

  const bubble = document.createElement("div");
  bubble.className = "msg-bubble";

  if (role === "assistant") {
    bubble.innerHTML = renderMarkdown(text);
  } else {
    bubble.textContent = text;
  }

  row.appendChild(avatar);
  row.appendChild(bubble);
  messagesEl.appendChild(row);
  messagesEl.scrollTop = messagesEl.scrollHeight;

  if (persist) {
    const messages = getSessionMessages(sessionId);
    messages.push({ role, text });
    const title =
      messages.find((m) => m.role === "user")?.text?.slice(0, 24) || "新对话";
    saveSessionMessages(sessionId, messages, title);
  }

  return row;
}

function showTyping() {
  showChatArea();
  const row = document.createElement("div");
  row.className = "msg-row assistant";
  row.id = "typingRow";
  row.innerHTML = `
    <div class="msg-avatar">AI</div>
    <div class="msg-bubble">
      <div class="typing-indicator"><span></span><span></span><span></span></div>
    </div>`;
  messagesEl.appendChild(row);
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

function hideTyping() {
  document.getElementById("typingRow")?.remove();
}

function setLoading(loading) {
  isLoading = loading;
  sendBtn.disabled = loading;
  messageInput.disabled = loading;
}

function renderHistory() {
  const sessions = getSessions();
  const entries = Object.entries(sessions).sort(
    (a, b) => (b[1].updatedAt || 0) - (a[1].updatedAt || 0)
  );

  historyList.innerHTML = "";
  if (!entries.length) {
    historyList.innerHTML = '<li class="history-empty">暂无历史</li>';
    return;
  }

  entries.slice(0, 8).forEach(([id, data]) => {
    const li = document.createElement("li");
    li.className = `history-item${id === sessionId ? " active" : ""}`;

    const title = document.createElement("span");
    title.className = "history-item-title";
    title.textContent = data.title || "新对话";
    title.title = data.title || "新对话";

    const deleteBtn = document.createElement("button");
    deleteBtn.className = "history-delete-btn";
    deleteBtn.type = "button";
    deleteBtn.setAttribute("aria-label", "删除对话");
    deleteBtn.innerHTML =
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M8 6V4h8v2M19 6l-1 14H6L5 6"/></svg>';
    deleteBtn.addEventListener("click", (e) => deleteSession(id, e));

    li.addEventListener("click", () => switchSession(id));
    li.appendChild(title);
    li.appendChild(deleteBtn);
    historyList.appendChild(li);
  });
}

async function deleteSession(id, event) {
  event.stopPropagation();

  const title = getSessions()[id]?.title || "新对话";
  if (!confirm(`确定删除「${title}」吗？`)) return;

  const sessions = getSessions();
  delete sessions[id];
  saveSessions(sessions);

  try {
    await fetch(`/chat/${encodeURIComponent(id)}`, { method: "DELETE" });
  } catch {
    // 本地已删除，后端清除失败不影响使用
  }

  if (id === sessionId) {
    const remaining = Object.entries(getSessions()).sort(
      (a, b) => (b[1].updatedAt || 0) - (a[1].updatedAt || 0)
    );
    if (remaining.length) {
      loadSession(remaining[0][0]);
    } else {
      startNewChat();
    }
  } else {
    renderHistory();
  }
}

function loadSession(id) {
  sessionId = id;
  localStorage.setItem(CURRENT_KEY, id);
  messagesEl.innerHTML = "";

  const messages = getSessionMessages(id);
  if (!messages.length) {
    welcomeScreen.classList.remove("hidden");
    messagesEl.classList.add("hidden");
    messagesEl.classList.remove("active");
  } else {
    welcomeScreen.classList.add("hidden");
    messagesEl.classList.remove("hidden");
    messagesEl.classList.add("active");
    messages.forEach((msg) => appendMessage(msg.role, msg.text, { persist: false }));
  }
  renderHistory();
}

function switchSession(id) {
  loadSession(id);
  closeSidebar();
}

function startNewChat() {
  sessionId = createSessionId();
  localStorage.setItem(CURRENT_KEY, sessionId);
  messagesEl.innerHTML = "";
  welcomeScreen.classList.remove("hidden");
  messagesEl.classList.add("hidden");
  messagesEl.classList.remove("active");
  renderHistory();
  messageInput.focus();
  closeSidebar();
}

async function sendMessage(message) {
  if (isLoading || !message.trim()) return;

  appendMessage("user", message);
  setLoading(true);
  showTyping();

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message, session_id: sessionId }),
    });

    hideTyping();

    if (!response.ok) {
      throw new Error(`服务暂时不可用 (${response.status})`);
    }

    const data = await response.json();
    appendMessage("assistant", data.reply);
  } catch (error) {
    hideTyping();
    appendMessage("system", error.message || "发送失败，请确认后端已启动。");
  } finally {
    setLoading(false);
  }
}

function closeSidebar() {
  sidebar.classList.remove("open");
  sidebarOverlay.classList.remove("open");
}

function autoResizeTextarea(el) {
  el.style.height = "auto";
  el.style.height = Math.min(el.scrollHeight, 120) + "px";
}

chatForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const message = messageInput.value.trim();
  if (!message) return;
  messageInput.value = "";
  autoResizeTextarea(messageInput);
  await sendMessage(message);
});

messageInput.addEventListener("input", () => autoResizeTextarea(messageInput));

messageInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    chatForm.requestSubmit();
  }
});

document.querySelectorAll(".chip, .welcome-card").forEach((btn) => {
  btn.addEventListener("click", () => {
    const message = btn.dataset.message;
    if (message) sendMessage(message);
  });
});

newChatBtn.addEventListener("click", startNewChat);

clearMemoryBtn.addEventListener("click", async () => {
  try {
    const response = await fetch(`/chat/${encodeURIComponent(sessionId)}`, {
      method: "DELETE",
    });
    if (!response.ok) throw new Error("清除记忆失败");
    appendMessage("system", "当前对话的后端记忆已清除。");
  } catch (error) {
    appendMessage("system", error.message);
  }
});

menuBtn.addEventListener("click", () => {
  sidebar.classList.toggle("open");
  sidebarOverlay.classList.toggle("open");
});

sidebarOverlay.addEventListener("click", closeSidebar);

loadSession(sessionId);
