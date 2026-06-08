from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.memory.session_store import clear_session
from app.services.llm import chat

router = APIRouter(prefix="/chat", tags=["chat"])


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="用户消息")
    session_id: str = Field(
        default="default",
        min_length=1,
        description="会话 ID，相同 ID 共享对话历史",
    )


class ChatResponse(BaseModel):
    reply: str
    session_id: str


@router.post("", response_model=ChatResponse)
async def send_message(body: ChatRequest) -> ChatResponse:
    reply = await chat(body.session_id, body.message)
    return ChatResponse(reply=reply, session_id=body.session_id)


@router.delete("/{session_id}")
async def reset_session(session_id: str):
    clear_session(session_id)
    return {"message": "会话历史已清除", "session_id": session_id}
