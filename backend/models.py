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

class Procedure(Document):
    id = StringField(required=True)
    soqd = StringField()
    ten = StringField()
    capthuchien = StringField()
    loaithutuc = StringField()
    linhvuc = StringField()
    trinhtuthuchien = StringField()
    cachthucthuchiens = ListField(DictField())
    thanhphanhosos = ListField(DictField())
    doituongthuchien = StringField()
    coquanthuchien = StringField()
    coquanthamquyen = StringField()
    diachitiepnhanhs = StringField()
    coquanuyquyen = StringField()
    coquanphoihop = StringField()
    ketquathuchien = StringField()
    cancuphaplys = ListField(DictField())
    yeucaudieukien = StringField()