from langchain.agents import create_agent
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI

from app.agent.tools import ALL_TOOLS
from app.config import settings
from app.memory.session_store import append_messages, get_history

SYSTEM_PROMPT = """你是一个贴心的 AI 生活助手，帮助用户处理日常事务。

【数据存储——必须严格遵守】
- 待办任务 → todos 表，工具：add_todo / list_todos
- 个人偏好/习惯/爱好 → preferences 表，工具：save_preference / search_preferences
- 支出 → expenses 表；收入 → incomes 表

【工具选择规则】
1. 用户问偏好、爱好、习惯 → 必须调用 search_preferences，禁止调用 list_todos。
2. 用户要求记住偏好、爱好、习惯 → 必须调用 save_preference，禁止调用 add_todo。
3. 用户问待办、任务 → 必须调用 list_todos，禁止调用 search_preferences。
4. 用户要求添加待办 → 必须调用 add_todo，禁止调用 save_preference。

【回答规则】
- 必须基于工具返回结果回答，禁止编造数据。
- 工具返回无记录时，如实告知用户。
- 回答简洁、友好、实用。"""

_agent = None


def get_llm() -> ChatOpenAI:
    return ChatOpenAI(
        model=settings.deepseek_model,
        api_key=settings.deepseek_api_key,
        base_url=settings.deepseek_base_url,
        temperature=0.3,
    )


def get_agent():
    global _agent
    if _agent is None:
        _agent = create_agent(
            get_llm(),
            tools=ALL_TOOLS,
            system_prompt=SYSTEM_PROMPT,
        )
    return _agent


def _extract_reply(messages: list) -> str:
    for message in reversed(messages):
        if isinstance(message, AIMessage) and message.content and not message.tool_calls:
            if isinstance(message.content, str):
                return message.content
            return str(message.content)
    raise ValueError("Agent 未返回有效回复")


async def chat(session_id: str, message: str) -> str:
    agent = get_agent()
    history = get_history(session_id)
    result = await agent.ainvoke(
        {"messages": [*history, HumanMessage(content=message)]}
    )
    reply = _extract_reply(result["messages"])
    append_messages(session_id, message, reply)
    return reply
