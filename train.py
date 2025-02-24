from dataset_loader import load_mnist
from model import build_model

def train():
    (x_train, y_train), (x_test, y_test) = load_mnist()
    model = build_model()
    model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))
    model.save("handwriting_model.h5")
    print("Model đã được lưu!")

if __name__ == "__main__":
    train()
