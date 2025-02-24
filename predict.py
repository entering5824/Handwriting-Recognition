import tensorflow as tf
import numpy as np
from preprocess import preprocess_image

def predict(image_path):
    model = tf.keras.models.load_model("handwriting_model.h5")
    img = preprocess_image(image_path)
    prediction = np.argmax(model.predict(img))
    return prediction

if __name__ == "__main__":
    image_path = "test_image.png"
    print(f"Kết quả dự đoán: {predict(image_path)}")
