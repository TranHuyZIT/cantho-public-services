from mongoengine import *

connect("chat", username='root', password='example', authentication_source='admin')

class Conversation(Document):
    created_at = DateTimeField()
    updated_at = DateTimeField()
    name = StringField()

class Message(Document):
    role = StringField()
    message = StringField()
    created_at = DateTimeField()
    updated_at = DateTimeField()
    conversation = ReferenceField(Conversation)
    metadata = DictField()
    documents = ListField(DictField())