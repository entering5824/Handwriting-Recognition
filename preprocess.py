import cv2
import numpy as np
from PIL import Image

def preprocess_image(image_path):
    """Tiền xử lý ảnh từ file path"""
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
    img = cv2.resize(img, (28, 28))
    img = img / 255.0
    img = np.expand_dims(img, axis=(0, -1))
    return img

def preprocess_pil_image(pil_image):
    """Tiền xử lý ảnh từ PIL Image object"""
    # Convert PIL image to numpy array
    img_array = np.array(pil_image)
    
    # Invert colors (black digits on white background -> white digits on black background)
    img_array = 255 - img_array
    
    # Resize to 28x28
    img_resized = cv2.resize(img_array, (28, 28))
    
    # Normalize to [0, 1]
    img_normalized = img_resized / 255.0
    
    # Add batch and channel dimensions
    img_final = np.expand_dims(img_normalized, axis=(0, -1))
    
    return img_final
