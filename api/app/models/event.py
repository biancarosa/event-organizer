from mongoengine import (
    Document, StringField, DateTimeField
)


class Event(Document):
    name = StringField(required=True)
    date = DateTimeField()
