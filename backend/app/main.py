from fastapi import FastAPI
from app.routers import chat

app = FastAPI(title="Mistral Secure Chat - Backend")

# include chat router
app.include_router(chat.router)

@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}
