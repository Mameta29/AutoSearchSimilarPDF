# backend/main.py
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from typing import List
from utils.text_processing import extract_text_features
from utils.image_processing import extract_image_features
from utils.search import search_similar_documents
from utils.database import save_document, get_document_path
from dotenv import load_dotenv

load_dotenv()
document_directory = os.getenv("DOCUMENT_DIRECTORY")
app = FastAPI()

class SimilarDocument(BaseModel):
    document_id: str
    similarity_score: float

@app.post("/search", response_model=List[SimilarDocument])
async def search_documents(file: UploadFile = File(...)):
    document_id = save_document(file)
    text_features = extract_text_features(file)
    image_features = extract_image_features(file)
    similar_docs = search_similar_documents(text_features, image_features)
    return similar_docs

@app.get("/{document_directory}/{document_id}.pdf")
async def get_document(document_id: str):
    document_path = get_document_path(document_id)
    return FileResponse(document_path)