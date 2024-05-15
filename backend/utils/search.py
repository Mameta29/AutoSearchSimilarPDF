# backend/utils/search.py
# import numpy as np
# import faiss
# from utils.database import get_all_documents

# def search_similar_documents(text_features, image_features, top_k=3):
#     documents = get_all_documents()
    
#     text_index = faiss.IndexFlatL2(text_features.shape[0])
#     image_index = faiss.IndexFlatL2(image_features.shape[1])
    
#     for doc in documents:
#         text_index.add(np.array([doc.text_features]))
#         image_index.add(np.array([doc.image_features]))
    
#     text_scores, text_indices = text_index.search(np.array([text_features]), top_k)
#     image_scores, image_indices = image_index.search(image_features, top_k)
    
#     similar_documents = []
#     for i in range(top_k):
#         document_id = documents[text_indices[0][i]].id
#         similarity_score = (text_scores[0][i] + image_scores[i][0]) / 2
#         similar_documents.append({"document_id": document_id, "similarity_score": similarity_score})
    
#     return similar_documents

import numpy as np
import faiss
from utils.database import get_all_document_ids
from utils.text_processing import extract_text_features
from utils.image_processing import extract_image_features

def search_similar_documents(text_features, image_features, top_k=3):
    document_ids = get_all_document_ids()
    text_features_list = [np.load(f"text_features_{doc_id}.npy") for doc_id in document_ids]
    image_features_list = [np.load(f"image_features_{doc_id}.npy") for doc_id in document_ids]

    text_index = faiss.IndexFlatL2(text_features.shape[0])
    image_index = faiss.IndexFlatL2(image_features.shape[1])

    for feature in text_features_list:
        text_index.add(np.array([feature]))

    for feature in image_features_list:
        image_index.add(np.array([feature]))

    text_scores, text_indices = text_index.search(np.array([text_features]), top_k)
    image_scores, image_indices = image_index.search(image_features, top_k)

    similar_documents = []
    for i in range(top_k):
        document_id = document_ids[text_indices[0][i]]
        similarity_score = (text_scores[0][i] + image_scores[i][0]) / 2
        similar_documents.append({"document_id": document_id, "similarity_score": similarity_score})

    return similar_documents