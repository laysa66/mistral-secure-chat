from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.models.schemas import ChatRequest, ChatResponse
from app.auth import verify_token
from app.services.mistral_service import mistral_service

router = APIRouter(prefix="/chat", tags=["chat"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    return payload

@router.post("/", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest, user: dict = Depends(get_current_user)):
    
    username = user.get('sub')
    
    try:
        # Appeler l'API Mistral pour obtenir une vraie réponse IA
        ai_response = await mistral_service.chat_completion(
            message=request.message,
            username=username
        )
        
        return ChatResponse(
            user_message=request.message,
            ai_response=ai_response
        )
        
    except Exception as e:
        print(f"error endpoint: {e}")
        # En cas d'erreur, retourner un message d'erreur convivial
        return ChatResponse(
            user_message=request.message,
            ai_response=" sorry i have a small problem retry later ."
        )


