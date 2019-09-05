from mongoengine import Document, StringField, EmailField, ReferenceField, ListField, DictField


class User(Document):
    username = StringField(max_length=30)
    email = EmailField(max_length=30)
    friends = ListField(ReferenceField('self'))
    extra = DictField()

class Post(Document):
    title = StringField(max_length=30)
    body = StringField(max_length=1024)
    author = StringField(max_length=30)
