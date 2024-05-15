# backend/utils/database.py
import os
# from models.document import Document
from utils.text_processing import extract_text_features
from utils.image_processing import extract_image_features
from dotenv import load_dotenv

load_dotenv() # Load environment variables
# document_directory = "documents/TYPE-A"
document_directory = os.getenv("DOCUMENT_DIRECTORY")
searched_directory = os.getenv("SEARCHED_DIRECTORY")

def save_document(file):
    document_id = len(os.listdir(searched_directory))
    document_path = os.path.join(searched_directory, f"{document_id}.pdf")
    
    with open(document_path, "wb") as f:
        f.write(file.file.read())
    
    # text_features = extract_text_features(file)
    # image_features = extract_image_features(file)
    
    # document = Document(id=document_id, text_features=text_features, image_features=image_features)
    # document.save()
    
    return document_id

def get_document_path(document_id):
    return os.path.join(document_directory, f"{document_id}.pdf")

def get_all_document_ids():
    # return Document.objects.all()
    return [int(file.split(".")[0]) for file in os.listdir(document_directory)]