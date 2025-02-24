from train import train
from predict import predict

def main():
    print("1. Huấn luyện mô hình")
    print("2. Nhận dạng chữ viết tay")
    choice = input("Chọn (1/2): ")

    if choice == "1":
        train()
    elif choice == "2":
        image_path = input("Nhập đường dẫn ảnh: ")
        result = predict(image_path)
        print(f"Kết quả nhận dạng: {result}")
    else:
        print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
