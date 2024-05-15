from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from typing import List
from utils.text_processing import extract_text_features
from utils.image_processing import extract_image_features
from utils.search import search_similar_documents
from utils.database import save_document, get_document_path, document_directory
import numpy as np
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# CORSの設定
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SimilarDocument(BaseModel):
    document_id: str
    similarity_score: float

@app.post("/search", response_model=List[SimilarDocument])
# async def search_documents(file: UploadFile = File(...)):
#     document_id = save_document(file)
#     text_features = extract_text_features(file)
#     image_features = extract_image_features(file)
#     np.save(f"text_features_{document_id}.npy", text_features)
#     np.save(f"image_features_{document_id}.npy", image_features)
#     similar_docs = search_similar_documents(text_features, image_features)
#     return similar_docs
async def search_documents(file: UploadFile = File(...)):
    print("text_features")
    text_features = await extract_text_features(file)
    print("image_features")
    # content = await file.read()
    # image_features = extract_image_features(content)
    image_features = await extract_image_features(file)
    print("save_document")
    similar_docs = search_similar_documents(text_features, image_features)
    return similar_docs

@app.get("/{document_id}.pdf")
async def get_document(document_id: str):
    document_path = get_document_path(document_id)
    return FileResponse(document_path)