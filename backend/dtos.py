from pydantic import BaseModel, Field

class AnswerRequest(BaseModel):
    question: str
    conversation_id: str | None = Field(default=None)