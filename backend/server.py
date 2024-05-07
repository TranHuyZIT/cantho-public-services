from models import Conversation, Message
from dtos import AnswerRequest

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
import datetime


app = FastAPI()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/{conversation_id}")
def get_conversation(conversation_id: str):
    conversation = Conversation.objects.get(id=conversation_id)
    return conversation


@app.post("/chat")
def chat(body: AnswerRequest):
    conversation_id = body.conversation_id
    question = body.question
    if not conversation_id:
        conversation = Conversation(
            name=question,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        conversation.save()
        conversation_id = conversation.id
    else:
        conversation = Conversation.objects.get(id=conversation_id)
    
    user_message = Message(role="user", message=question, created_at=datetime.datetime.now(), updated_at=datetime.datetime.now() , conversation=conversation)
    user_message.save()

    return {
        "answer": "Hello world"
    }
    
    