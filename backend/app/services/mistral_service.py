import os
import json
import httpx
from typing import Optional, List, Dict, Any
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

class MistralService:
    def __init__(self):
        self.api_key = os.getenv("MISTRAL_API_KEY")
        self.api_url = "https://api.mistral.ai/v1/chat/completions"
        
        if not self.api_key or self.api_key == "your_mistral_api_key_here":
            print(" ATTENTION: Clé API Mistral non configurée!")
            
            self.api_configured = False
        else:
            self.api_configured = True
    
    async def chat_completion(self, message: str, username: Optional[str] = None) -> str:

        
        # Vérifier si la clé API est configurée
        if not self.api_configured:
                return " Sorry, the Mistral API is not configured yet. Please add your Mistral API key in the .env file to use the AI!"

        
        try:
            # Créer le contexte de conversation
            system_message = """You are a useful and friendly AI assistant. Respond in a concise and relevant manner in French. 
You are integrated into a secure chat with JWT authentication."""
            
            if username:
                system_message += f" the username is {username}."
            
            # Préparer la requête pour l'API Mistral
            messages = [
                {"role": "system", "content": system_message},
                {"role": "user", "content": message}
            ]
            
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": "mistral-small-latest",
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 500
            }
            
            # Appeler l'API Mistral directement avec httpx
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    self.api_url,
                    headers=headers,
                    json=data,
                    timeout=30.0
                )
            
            # Extraire la réponse
            response_json = response.json()
            
            if response.status_code != 200:
                error_message = response_json.get("error", {}).get("message", "Erreur inconnue")
                print(f"Erreur API Mistral: {error_message}")
                return f" sorry error {error_message}"
            
            if "choices" in response_json and len(response_json["choices"]) > 0:
                ai_response = response_json["choices"][0]["message"]["content"]
                return f" {ai_response}"
            else:
                return " sorry, i can't generate an answer right now."
                
        except Exception as e:
            print(f"Error API Mistral: {e}")
            
            # Messages d'erreur spécifiques selon le type d'erreur
            error_str = str(e).lower()
            if "unauthorized" in error_str or "invalid" in error_str:
                return " Error : Mistral API key is invalid. Please check your .env configuration."
            elif "quota" in error_str or "limit" in error_str:
                return "Error: Mistral API quota exceeded. Please check your usage limits."
            elif "network" in error_str or "connection" in error_str:
                return "Error: Network issue while connecting to Mistral API. Please try again later."
            else:
                return f"Error: {str(e)}"

# Instance globale du service
mistral_service = MistralService()