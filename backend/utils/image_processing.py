# backend/utils/image_processing.py
from pdf2image import convert_from_bytes
import numpy as np
import cv2

async def extract_image_features(file):
    print("------------------extract_image_features------------------")
    content = await file.read()
    print("content", content)
    
    try:
        images = convert_from_bytes(content)
        print("images", images)
        image_features = []
        for image in images:
            resized_image = cv2.resize(np.array(image), (224, 224))
            features = resized_image.flatten()
            image_features.append(features)
        return np.array(image_features)
    except Exception as e:
        print(f"Error in extract_image_features: {str(e)}")
        return None