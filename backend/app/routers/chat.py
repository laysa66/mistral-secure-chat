from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    # For now, mock a response (we'll connect to Mistral later)
    return ChatResponse(
        user_message=request.message,
        ai_response=f"Echo from AI: {request.message}"
    )
