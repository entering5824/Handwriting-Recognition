import cv2
import numpy as np

def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
    img = cv2.resize(img, (28, 28))
    img = img / 255.0
    img = np.expand_dims(img, axis=(0, -1))
    return img
