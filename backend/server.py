from models import Conversation, Message
from dtos import AnswerRequest
from rag.modules.rag_facade import RAGFacade

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import datetime
import json



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


@app.get("/conversations")
def get_conversations(name: Optional[str] = None):
    if name:
        conversations = Conversation.objects(name__icontains=name).order_by('-created_at')
    else:
        conversations = Conversation.objects().order_by('-created_at').all()

    return {"conversations": json.loads(conversations.to_json())[:5]}


@app.get("/conversations/{conversation_id}")
def get_conversation(conversation_id: str):
    conversation = Conversation.objects.get(id=conversation_id)
    # Then, get the messages of this conversation
    messages = Message.objects(conversation=conversation)
    result = {
        "conversation": json.loads(conversation.to_json()),
        "messages": json.loads(messages.to_json())
    }

    return result


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
        conversation_id = str(conversation.id)
    else:
        conversation = Conversation.objects.get(id=conversation_id)
    
    messages = Message.objects(conversation=conversation).order_by('created_at').limit(4)
    history = []
    for message in messages:
        history.append({
            "role": message.role,
            "content": message.message
        })
    transformed_question = None
    if len(history) > 0:
        transformed_question = RAGFacade.rewrite_question(question, history)
    
    user_message = Message(role="user", message=question, created_at=datetime.datetime.now(), updated_at=datetime.datetime.now() , conversation=conversation)
    response = RAGFacade.generate_response(transformed_question or question)
    documents= [{"full_text": doc.metadata['full_text'],"source": doc.metadata['filename'].replace(".txt", '')} for doc in response['documents']]
    bot_message = Message(role="bot", message=response['answer'], created_at=datetime.datetime.now(),
                            updated_at=datetime.datetime.now(), 
                            conversation=conversation,
                            documents=documents,
                            metadata={
                                "questions": response['questions'],
                            }
                        )

    user_message.save()
    bot_message.save()

    return {
        "message": json.loads(bot_message.to_json()),
        "answer": response['answer'],
        "conversation_id": conversation_id,
        "documents": documents,
        "questions": response['questions']
    }
    
    