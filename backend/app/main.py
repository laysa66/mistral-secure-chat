from fastapi import FastAPI
from app.routers import chat, auth
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Mistral Secure Chat - Backend")

origins = [
    "http://localhost",
    "http://localhost:3000",  # React dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routers
app.include_router(chat.router)
app.include_router(auth.router)

@app.get("/") # we create our running app using FastAPI
def root():# we define a root endpoint 
    return {"message": "Backend is running 🚀"}

