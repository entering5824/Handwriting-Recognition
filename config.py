"""
Configuration file for AI Handwriting Recognition System
"""

# Model Configuration
MODEL_CONFIG = {
    "input_shape": (28, 28, 1),
    "num_classes": 10,
    "model_file": "handwriting_model.h5",
    "batch_size": 128,
    "epochs": 50,
    "learning_rate": 0.001,
    "validation_split": 0.2
}

# Training Configuration
TRAINING_CONFIG = {
    "early_stopping_patience": 10,
    "reduce_lr_patience": 5,
    "reduce_lr_factor": 0.5,
    "min_learning_rate": 0.0001,
    "data_augmentation": {
        "rotation_range": 10,
        "width_shift_range": 0.1,
        "height_shift_range": 0.1,
        "zoom_range": 0.1,
        "fill_mode": "nearest"
    }
}

# GUI Configuration
GUI_CONFIG = {
    "window_title": "AI Handwriting Recognition System",
    "window_size": "1200x800",
    "min_window_size": "1000x700",
    "theme": "dark",
    "canvas_size": 280,
    "brush_size": 12
}

# Application Configuration
APP_CONFIG = {
    "version": "2.0",
    "author": "AI Developer",
    "description": "Advanced AI-powered handwriting recognition system",
    "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
    "max_image_size": (1024, 1024)
}

# Performance Configuration
PERFORMANCE_CONFIG = {
    "confidence_threshold": 0.8,
    "high_confidence_color": "green",
    "medium_confidence_color": "orange", 
    "low_confidence_color": "red",
    "prediction_history_limit": 100
}

# File Paths
PATHS = {
    "models_dir": "models",
    "data_dir": "data", 
    "logs_dir": "logs",
    "exports_dir": "exports",
    "reports_dir": "reports"
}

# Logging Configuration
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file": "logs/app.log"
}
