# backend/utils/text_processing.py
from PyPDF2 import PdfReader
import io
from sklearn.feature_extraction.text import TfidfVectorizer

async def extract_text_features(file):
    print("------------------extract_text_features------------------")
    content = await file.read()
    print("------------------extract_text_features2------------------")
    print("content", content)
    pdf_reader = PdfReader(io.BytesIO(content))
    print("pdf_reader", pdf_reader)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    print("text", text)
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform([text])
    return features.toarray()[0]