from langchain_core.messages import AIMessage, BaseMessage, HumanMessage

_sessions: dict[str, list[BaseMessage]] = {}
MAX_MESSAGES = 20


def get_history(session_id: str) -> list[BaseMessage]:
    return list(_sessions.get(session_id, []))


def append_messages(session_id: str, human: str, ai: str) -> None:
    if session_id not in _sessions:
        _sessions[session_id] = []
    _sessions[session_id].extend(
        [
            HumanMessage(content=human),
            AIMessage(content=ai),
        ]
    )
    if len(_sessions[session_id]) > MAX_MESSAGES:
        _sessions[session_id] = _sessions[session_id][-MAX_MESSAGES:]


def clear_session(session_id: str) -> None:
    _sessions.pop(session_id, None)
