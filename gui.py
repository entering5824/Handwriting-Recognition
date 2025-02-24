import customtkinter as ctk
import numpy as np
import tensorflow as tf
from PIL import Image, ImageDraw

from preprocess import preprocess_pil_image

# Tải mô hình đã huấn luyện
model = tf.keras.models.load_model("handwriting_model.h5")

class HandwritingApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Nhận dạng chữ viết tay")
        self.geometry("400x500")

        # Khung vẽ
        self.canvas_size = 280
        self.canvas = ctk.CTkCanvas(self, width=self.canvas_size, height=self.canvas_size, bg="white")
        self.canvas.pack(pady=20)

        # Ảnh nền vẽ
        self.image = Image.new("L", (self.canvas_size, self.canvas_size), 255)
        self.draw = ImageDraw.Draw(self.image)

        # Nút Nhận dạng
        self.recognize_button = ctk.CTkButton(self, text="Nhận dạng", command=self.recognize_digit)
        self.recognize_button.pack(pady=10)

        # Nút Reset
        self.reset_button = ctk.CTkButton(self, text="Reset", command=self.clear_canvas)
        self.reset_button.pack(pady=10)

        # Label hiển thị kết quả
        self.result_label = ctk.CTkLabel(self, text="Vẽ số và nhấn 'Nhận dạng'", font=("Arial", 16))
        self.result_label.pack(pady=10)

        # Sự kiện chuột
        self.canvas.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        x, y = event.x, event.y
        radius = 8  # Độ dày nét vẽ
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="black", outline="black")
        self.draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill="black")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (self.canvas_size, self.canvas_size), 255)
        self.draw = ImageDraw.Draw(self.image)
        self.result_label.configure(text="Vẽ số và nhấn 'Nhận dạng'")

    def recognize_digit(self):
        img = preprocess_pil_image(self.image)
        prediction = np.argmax(model.predict(img))
        self.result_label.configure(text=f"Kết quả: {prediction}")

if __name__ == "__main__":
    app = HandwritingApp()
    app.mainloop()
