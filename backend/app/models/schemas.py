from pydantic import BaseModel
# model and schema of how the app will be built 

# we have to define the structure of our requests and responses using Pydantic models.
#the role of Pydantic is to validate the data.
class ChatRequest(BaseModel): # a model of what a chat request looks like
    message: str # the user's message type is string 

class ChatResponse(BaseModel): # a model of what a chat response looks like
    user_message: str # the user's message type is string
    ai_response: str # the ai response to the user message type is string
