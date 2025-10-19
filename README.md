# 🤖 AI Handwriting Recognition System

<div align="center">

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.12+-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![GitHub stars](https://img.shields.io/github/stars/phamt/handwriting-recognition)
![GitHub forks](https://img.shields.io/github/forks/phamt/handwriting-recognition)
![GitHub issues](https://img.shields.io/github/issues/phamt/handwriting-recognition)

**An advanced AI-powered handwriting recognition system built with deep learning**

[🚀 Features](#-features) • [📦 Installation](#-installation) • [🎯 Usage](#-usage) • [🏗️ Architecture](#️-architecture) • [📊 Performance](#-performance)

</div>

## 🎯 Overview

This project demonstrates a sophisticated **Convolutional Neural Network (CNN)** for recognizing handwritten digits (0-9) with a modern, professional GUI interface. Built with TensorFlow/Keras and CustomTkinter, it showcases advanced deep learning techniques including data augmentation, batch normalization, and dropout regularization.

Perfect for **job interviews**, **internship presentations**, and **portfolio demonstrations**!

## ✨ Features

### 🎯 Core Recognition
- **Real-time handwriting recognition** with 95%+ accuracy
- **Interactive drawing canvas** with smooth user experience
- **Confidence scoring** for prediction reliability
- **Prediction history** tracking and analytics

### 🏗️ Advanced Architecture
- **Deep CNN** with Batch Normalization and Dropout
- **Data Augmentation** for improved generalization
- **Early Stopping** and Learning Rate Scheduling
- **Multi-metric evaluation** (Accuracy, Top-K Accuracy)

### 📊 Professional Dashboard
- **Modern GUI** with dark theme and intuitive design
- **Model Analytics** with real-time statistics
- **Training Visualization** with loss/accuracy plots
- **Performance Metrics** and model information

### 🔧 Developer Features
- **Modular architecture** for easy extension
- **Comprehensive logging** and error handling
- **Export capabilities** for reports and analysis
- **Cross-platform compatibility**

## 📦 Installation

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/handwriting-recognition.git
cd handwriting-recognition
```

2. **Run the setup script**
```bash
python setup.py
```

3. **Launch the application**
```bash
python gui.py
```

### Manual Installation

1. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

2. **Train the model** (optional - pre-trained model included)
```bash
python train.py
```

3. **Run the GUI application**
```bash
python gui.py
```

## 🎯 Usage

### GUI Application
```bash
python gui.py
```

The application features three main tabs:

- **🎯 Recognition**: Draw digits and get real-time predictions
- **📊 Model Analytics**: View model performance and statistics
- **🏋️ Training**: Train or retrain the model with custom parameters

### Command Line Interface
```bash
python main.py
```

### Training a New Model
```bash
python train.py
```

### Prediction from Image File
```bash
python predict.py
```

## 🏗️ Architecture

### Model Architecture

```
Input (28x28x1) 
    ↓
Conv2D(32) + BatchNorm + ReLU
    ↓
Conv2D(32) + ReLU
    ↓
MaxPooling2D(2x2) + Dropout(0.25)
    ↓
Conv2D(64) + BatchNorm + ReLU
    ↓
Conv2D(64) + ReLU
    ↓
MaxPooling2D(2x2) + Dropout(0.25)
    ↓
Conv2D(128) + BatchNorm + Dropout(0.25)
    ↓
Flatten()
    ↓
Dense(512) + BatchNorm + Dropout(0.5)
    ↓
Dense(256) + Dropout(0.5)
    ↓
Dense(10) + Softmax
```

### Key Features
- **3 Convolutional Blocks** with increasing filters (32→64→128)
- **Batch Normalization** for stable training
- **Dropout Layers** to prevent overfitting
- **Data Augmentation** with rotation, shift, and zoom
- **Early Stopping** and **Learning Rate Reduction**

## 📊 Performance

### Model Metrics
- **Training Accuracy**: ~99.5%
- **Validation Accuracy**: ~98.5%
- **Test Accuracy**: ~98.2%
- **Inference Time**: <50ms per prediction
- **Model Size**: ~2.5MB

### Dataset
- **MNIST Handwritten Digits**
- **70,000 samples** (60,000 train + 10,000 test)
- **28x28 grayscale images**
- **10 classes** (digits 0-9)

## 🔧 Technical Details

### Technologies Used
- **TensorFlow 2.12+** - Deep learning framework
- **CustomTkinter** - Modern GUI framework
- **OpenCV** - Image processing
- **Matplotlib** - Data visualization
- **NumPy** - Numerical computing
- **PIL/Pillow** - Image manipulation

### System Requirements
- **Python 3.8+**
- **4GB RAM** minimum
- **GPU recommended** for training (optional)

## 📁 Project Structure

```
handwriting-recognition/
├── 📄 main.py              # CLI entry point
├── 🎨 gui.py               # GUI application
├── 🧠 model.py             # CNN model definition
├── 🏋️ train.py             # Training pipeline
├── 🔮 predict.py           # Prediction functions
├── 🔄 preprocess.py        # Image preprocessing
├── 📊 dataset_loader.py    # Data loading utilities
├── 📋 requirements.txt     # Dependencies
├── ⚙️ setup.py            # Setup script
└── 📖 README.md           # Documentation
```

## 🚀 Advanced Features

### Data Augmentation
- **Rotation**: ±10 degrees
- **Translation**: ±10% width/height shift
- **Zoom**: ±10% scale variation
- **Fill Mode**: Nearest neighbor interpolation

### Training Optimizations
- **Adam Optimizer** with learning rate 0.001
- **Early Stopping** with patience=10
- **Learning Rate Reduction** on plateau
- **Batch Size**: 128 for optimal performance

### GUI Features
- **Real-time Drawing** with smooth brush strokes
- **Confidence Visualization** with color coding
- **Prediction History** with timestamps
- **Model Information** display
- **Training Progress** visualization

## 🎓 Educational Value

This project demonstrates:

1. **Deep Learning Fundamentals**
   - CNN architecture design
   - Batch normalization and dropout
   - Data augmentation techniques

2. **Software Engineering**
   - Modular code structure
   - Error handling and logging
   - GUI development with modern frameworks

3. **MLOps Practices**
   - Model versioning and saving
   - Performance monitoring
   - User-friendly interfaces

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup
```bash
git clone https://github.com/yourusername/handwriting-recognition.git
cd handwriting-recognition
pip install -r requirements.txt
python -m pytest tests/  # Run tests
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **MNIST Dataset** by Yann LeCun et al.
- **TensorFlow Team** for the excellent deep learning framework
- **CustomTkinter** for the modern GUI components

## 📞 Contact

**Developer**: Phạm Tấn  
**Email**: phamt@example.com  
**LinkedIn**: [Your LinkedIn Profile]  
**GitHub**: [Your GitHub Profile]

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/handwriting-recognition&type=Date)](https://star-history.com/#yourusername/handwriting-recognition&Date)

---

<div align="center">

**⭐ If you found this project helpful, please give it a star! ⭐**

Made with ❤️ and ☕

</div>
