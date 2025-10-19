import customtkinter as ctk
import numpy as np
import tensorflow as tf
from PIL import Image, ImageDraw, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
from datetime import datetime

from preprocess import preprocess_pil_image

# Thiết lập theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class HandwritingRecognitionApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("AI Handwriting Recognition System")
        self.geometry("1200x800")
        self.minsize(1000, 700)

        # Biến lưu trữ
        self.model = None
        self.canvas_size = 280
        self.prediction_history = []
        self.model_stats = {}
        
        # Tải mô hình
        self.load_model()
        
        # Tạo giao diện
        self.create_widgets()
        
        # Khởi tạo canvas vẽ
        self.init_drawing_canvas()

    def load_model(self):
        """Tải mô hình đã huấn luyện"""
        try:
            if os.path.exists("handwriting_model.h5"):
                self.model = tf.keras.models.load_model("handwriting_model.h5")
                self.model_stats = {
                    'loaded': True,
                    'input_shape': self.model.input_shape,
                    'output_shape': self.model.output_shape,
                    'total_params': self.model.count_params()
                }
            else:
                self.model_stats = {'loaded': False, 'error': 'Model file not found'}
        except Exception as e:
            self.model_stats = {'loaded': False, 'error': str(e)}

    def create_widgets(self):
        """Tạo các widget cho giao diện"""
        # Header
        self.create_header()
        
        # Main content với tabs
        self.create_tabs()
        
        # Footer
        self.create_footer()

    def create_header(self):
        """Tạo header với tiêu đề và thông tin"""
        header_frame = ctk.CTkFrame(self)
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        # Tiêu đề chính
        title_label = ctk.CTkLabel(
            header_frame, 
            text="🤖 AI Handwriting Recognition System", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(pady=10)
        
        # Subtitle
        subtitle_label = ctk.CTkLabel(
            header_frame,
            text="Powered by Deep Learning & Computer Vision",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        subtitle_label.pack(pady=(0, 10))

    def create_tabs(self):
        """Tạo tab system"""
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Tab 1: Recognition
        self.tabview.add("🎯 Recognition")
        self.create_recognition_tab()
        
        # Tab 2: Model Info
        self.tabview.add("📊 Model Analytics")
        self.create_analytics_tab()
        
        # Tab 3: Training
        self.tabview.add("🏋️ Training")
        self.create_training_tab()

    def create_recognition_tab(self):
        """Tạo tab nhận dạng"""
        tab = self.tabview.tab("🎯 Recognition")
        
        # Frame chính với 2 cột
        main_frame = ctk.CTkFrame(tab)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Cột trái - Canvas vẽ
        left_frame = ctk.CTkFrame(main_frame)
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        # Canvas vẽ
        canvas_frame = ctk.CTkFrame(left_frame)
        canvas_frame.pack(pady=20)
        
        self.canvas = ctk.CTkCanvas(
            canvas_frame, 
            width=self.canvas_size, 
            height=self.canvas_size, 
            bg="white",
            highlightthickness=2,
            highlightcolor="gray"
        )
        self.canvas.pack(padx=20, pady=20)
        
        # Hướng dẫn
        instruction_label = ctk.CTkLabel(
            left_frame,
            text="Draw a digit (0-9) in the canvas above",
            font=ctk.CTkFont(size=12),
            text_color="gray"
        )
        instruction_label.pack(pady=(0, 20))
        
        # Nút điều khiển
        button_frame = ctk.CTkFrame(left_frame)
        button_frame.pack(pady=20)
        
        self.recognize_button = ctk.CTkButton(
            button_frame,
            text="🔍 Recognize",
            command=self.recognize_digit,
            font=ctk.CTkFont(size=14, weight="bold"),
            height=40
        )
        self.recognize_button.pack(side="left", padx=10)
        
        self.clear_button = ctk.CTkButton(
            button_frame,
            text="🗑️ Clear",
            command=self.clear_canvas,
            font=ctk.CTkFont(size=14),
            height=40,
            fg_color="gray"
        )
        self.clear_button.pack(side="left", padx=10)
        
        # Cột phải - Kết quả và thông tin
        right_frame = ctk.CTkFrame(main_frame)
        right_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))
        
        # Kết quả nhận dạng
        result_frame = ctk.CTkFrame(right_frame)
        result_frame.pack(fill="x", pady=20)
        
        result_title = ctk.CTkLabel(
            result_frame,
            text="🎯 Recognition Result",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        result_title.pack(pady=10)
        
        self.result_label = ctk.CTkLabel(
            result_frame,
            text="Draw a digit to get started",
            font=ctk.CTkFont(size=32, weight="bold"),
            text_color="gray"
        )
        self.result_label.pack(pady=20)
        
        # Confidence score
        self.confidence_label = ctk.CTkLabel(
            result_frame,
            text="",
            font=ctk.CTkFont(size=14)
        )
        self.confidence_label.pack(pady=(0, 20))
        
        # Lịch sử nhận dạng
        history_frame = ctk.CTkFrame(right_frame)
        history_frame.pack(fill="both", expand=True, pady=(0, 20))
        
        history_title = ctk.CTkLabel(
            history_frame,
            text="📈 Recognition History",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        history_title.pack(pady=10)
        
        # Scrollable text widget cho lịch sử
        self.history_text = ctk.CTkTextbox(history_frame, height=200)
        self.history_text.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    def create_analytics_tab(self):
        """Tạo tab phân tích mô hình"""
        tab = self.tabview.tab("📊 Model Analytics")
        
        main_frame = ctk.CTkFrame(tab)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Thông tin mô hình
        info_frame = ctk.CTkFrame(main_frame)
        info_frame.pack(fill="x", pady=(0, 20))
        
        info_title = ctk.CTkLabel(
            info_frame,
            text="🧠 Model Information",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        info_title.pack(pady=15)
        
        # Hiển thị thông tin mô hình
        self.model_info_text = ctk.CTkTextbox(info_frame, height=150)
        self.model_info_text.pack(fill="x", padx=20, pady=(0, 20))
        
        # Biểu đồ
        chart_frame = ctk.CTkFrame(main_frame)
        chart_frame.pack(fill="both", expand=True)
        
        chart_title = ctk.CTkLabel(
            chart_frame,
            text="📊 Recognition Statistics",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        chart_title.pack(pady=15)
        
        self.create_charts(chart_frame)

    def create_training_tab(self):
        """Tạo tab training"""
        tab = self.tabview.tab("🏋️ Training")
        
        main_frame = ctk.CTkFrame(tab)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Thông tin training
        info_frame = ctk.CTkFrame(main_frame)
        info_frame.pack(fill="x", pady=(0, 20))
        
        title = ctk.CTkLabel(
            info_frame,
            text="🏋️ Model Training",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        title.pack(pady=15)
        
        # Thông tin về dataset và training
        training_info = """
📚 Dataset: MNIST Handwritten Digits
🔢 Total Samples: 70,000 (60,000 train + 10,000 test)
🎯 Classes: 10 digits (0-9)
🏗️ Architecture: Convolutional Neural Network (CNN)
⚙️ Optimizer: Adam
📏 Image Size: 28x28 pixels
🎨 Preprocessing: Normalization, Grayscale
        """
        
        training_text = ctk.CTkTextbox(info_frame, height=200)
        training_text.pack(fill="x", padx=20, pady=(0, 20))
        training_text.insert("1.0", training_info)
        training_text.configure(state="disabled")
        
        # Nút training
        button_frame = ctk.CTkFrame(main_frame)
        button_frame.pack(pady=20)
        
        train_button = ctk.CTkButton(
            button_frame,
            text="🚀 Start Training",
            command=self.start_training,
            font=ctk.CTkFont(size=14, weight="bold"),
            height=50
        )
        train_button.pack(pady=20)

    def create_charts(self, parent):
        """Tạo biểu đồ thống kê"""
        # Tạo matplotlib figure
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
        
        # Biểu đồ 1: Lịch sử nhận dạng
        if self.prediction_history:
            digits, counts = np.unique([p['digit'] for p in self.prediction_history], return_counts=True)
            ax1.bar(digits, counts, color='skyblue', alpha=0.7)
            ax1.set_title('Recognition History')
            ax1.set_xlabel('Digits')
            ax1.set_ylabel('Count')
        else:
            ax1.text(0.5, 0.5, 'No predictions yet', ha='center', va='center', transform=ax1.transAxes)
            ax1.set_title('Recognition History')
        
        # Biểu đồ 2: Confidence distribution
        if self.prediction_history:
            confidences = [p['confidence'] for p in self.prediction_history]
            ax2.hist(confidences, bins=10, color='lightgreen', alpha=0.7)
            ax2.set_title('Confidence Distribution')
            ax2.set_xlabel('Confidence')
            ax2.set_ylabel('Frequency')
        else:
            ax2.text(0.5, 0.5, 'No predictions yet', ha='center', va='center', transform=ax2.transAxes)
            ax2.set_title('Confidence Distribution')
        
        plt.tight_layout()
        
        # Embed vào tkinter
        canvas = FigureCanvasTkAgg(fig, parent)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=20, pady=(0, 20))

    def create_footer(self):
        """Tạo footer"""
        footer_frame = ctk.CTkFrame(self)
        footer_frame.pack(fill="x", padx=20, pady=(10, 20))
        
        footer_text = ctk.CTkLabel(
            footer_frame,
            text="Built with TensorFlow, CustomTkinter & ❤️ | Version 2.0",
            font=ctk.CTkFont(size=12),
            text_color="gray"
        )
        footer_text.pack(pady=10)

    def init_drawing_canvas(self):
        """Khởi tạo canvas vẽ"""
        self.image = Image.new("L", (self.canvas_size, self.canvas_size), 255)
        self.draw = ImageDraw.Draw(self.image)
        
        # Bind events
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<Button-1>", self.paint)
        
        # Cập nhật thông tin mô hình
        self.update_model_info()

    def paint(self, event):
        """Xử lý sự kiện vẽ"""
        x, y = event.x, event.y
        radius = 12  # Độ dày nét vẽ
        
        self.canvas.create_oval(
            x - radius, y - radius, x + radius, y + radius, 
            fill="black", outline="black"
        )
        self.draw.ellipse(
            [x - radius, y - radius, x + radius, y + radius], 
            fill="black"
        )

    def clear_canvas(self):
        """Xóa canvas"""
        self.canvas.delete("all")
        self.image = Image.new("L", (self.canvas_size, self.canvas_size), 255)
        self.draw = ImageDraw.Draw(self.image)
        self.result_label.configure(text="Draw a digit to get started")
        self.confidence_label.configure(text="")

    def recognize_digit(self):
        """Nhận dạng chữ số"""
        if not self.model:
            self.result_label.configure(text="❌ Model not loaded")
            return
            
        try:
            # Tiền xử lý ảnh
            img = preprocess_pil_image(self.image)
            
            # Dự đoán
            predictions = self.model.predict(img, verbose=0)
            predicted_digit = np.argmax(predictions)
            confidence = np.max(predictions) * 100
            
            # Cập nhật UI
            self.result_label.configure(
                text=f"{predicted_digit}",
                text_color="green"
            )
            self.confidence_label.configure(
                text=f"Confidence: {confidence:.1f}%",
                text_color="green" if confidence > 80 else "orange" if confidence > 60 else "red"
            )
            
            # Lưu vào lịch sử
            prediction_record = {
                'digit': predicted_digit,
                'confidence': confidence,
                'timestamp': datetime.now().strftime("%H:%M:%S")
            }
            self.prediction_history.append(prediction_record)
            
            # Cập nhật lịch sử hiển thị
            self.update_history_display()
            
        except Exception as e:
            self.result_label.configure(text=f"❌ Error: {str(e)}")

    def update_history_display(self):
        """Cập nhật hiển thị lịch sử"""
        self.history_text.delete("1.0", "end")
        
        history_text = "Recent Predictions:\n" + "="*50 + "\n\n"
        
        for record in self.prediction_history[-10:]:  # Hiển thị 10 lần gần nhất
            history_text += f"🔸 Digit: {record['digit']} | Confidence: {record['confidence']:.1f}% | Time: {record['timestamp']}\n"
        
        self.history_text.insert("1.0", history_text)

    def update_model_info(self):
        """Cập nhật thông tin mô hình"""
        self.model_info_text.delete("1.0", "end")
        
        if self.model_stats.get('loaded', False):
            info_text = f"""
✅ Model Status: Loaded Successfully
🏗️ Architecture: CNN (Convolutional Neural Network)
📏 Input Shape: {self.model_stats.get('input_shape', 'N/A')}
🎯 Output Shape: {self.model_stats.get('output_shape', 'N/A')}
🔢 Total Parameters: {self.model_stats.get('total_params', 'N/A'):,}
📊 Model File: handwriting_model.h5
🎨 Framework: TensorFlow/Keras
            """
        else:
            error_msg = self.model_stats.get('error', 'Unknown error')
            info_text = f"""
❌ Model Status: Not Loaded
🚨 Error: {error_msg}
💡 Please train the model first using the Training tab
            """
        
        self.model_info_text.insert("1.0", info_text)

    def start_training(self):
        """Bắt đầu training mô hình"""
        try:
            from train import train
            train()
            # Reload model sau khi training
            self.load_model()
            self.update_model_info()
            
            # Hiển thị thông báo thành công
            success_label = ctk.CTkLabel(
                self.tabview.tab("🏋️ Training"),
                text="✅ Training completed successfully!",
                font=ctk.CTkFont(size=14, weight="bold"),
                text_color="green"
            )
            success_label.pack(pady=10)
            
        except Exception as e:
            error_label = ctk.CTkLabel(
                self.tabview.tab("🏋️ Training"),
                text=f"❌ Training failed: {str(e)}",
                font=ctk.CTkFont(size=14, weight="bold"),
                text_color="red"
            )
            error_label.pack(pady=10)

if __name__ == "__main__":
    app = HandwritingRecognitionApp()
    app.mainloop()
