# backend/models/document.py
from mongoengine import Document, IntField, BinaryField

class Document(Document):
    id = IntField(primary_key=True)
    text_features = BinaryField()
    image_features = BinaryField()