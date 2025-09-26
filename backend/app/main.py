from fastapi import FastAPI
from app.routers import chat

app = FastAPI(title="Mistral Secure Chat - Backend")

# include chat router
app.include_router(chat.router)

@app.get("/") # we create our running app using FastAPI
def root():# we define a root endpoint 
    return {"message": "Backend is running 🚀"}
