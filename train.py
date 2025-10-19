import numpy as np
import matplotlib.pyplot as plt
from dataset_loader import load_mnist
from model import build_model, get_callbacks

def train():
    """Huấn luyện mô hình với các tính năng nâng cao"""
    print("🚀 Starting model training...")
    
    # Load data
    print("📊 Loading MNIST dataset...")
    (x_train, y_train), (x_test, y_test) = load_mnist()
    
    # Data augmentation
    print("🔄 Applying data augmentation...")
    x_train_augmented, y_train_augmented = augment_data(x_train, y_train)
    
    # Build model
    print("🏗️ Building advanced CNN model...")
    model = build_model()
    
    # Display model summary
    print("\n📋 Model Architecture:")
    model.summary()
    
    # Get callbacks
    callbacks = get_callbacks()
    
    # Training
    print("\n🏋️ Starting training...")
    history = model.fit(
        x_train_augmented, y_train_augmented,
        epochs=50,
        batch_size=128,
        validation_data=(x_test, y_test),
        callbacks=callbacks,
        verbose=1
    )
    
    # Evaluate model
    print("\n📈 Evaluating model...")
    test_loss, test_accuracy, test_top_k = model.evaluate(x_test, y_test, verbose=0)
    print(f"Test Accuracy: {test_accuracy:.4f}")
    print(f"Test Top-K Accuracy: {test_top_k:.4f}")
    
    # Save model
    model.save("handwriting_model.h5")
    print("✅ Model saved successfully!")
    
    # Plot training history
    plot_training_history(history)
    
    return model, history

def augment_data(x_train, y_train):
    """Data augmentation để cải thiện hiệu suất mô hình"""
    from tensorflow.keras.preprocessing.image import ImageDataGenerator
    
    # Tạo data generator với augmentation
    datagen = ImageDataGenerator(
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1,
        zoom_range=0.1,
        fill_mode='nearest'
    )
    
    # Fit generator
    datagen.fit(x_train)
    
    # Generate augmented data
    augmented_data = []
    augmented_labels = []
    
    for batch in datagen.flow(x_train, y_train, batch_size=1000):
        augmented_data.append(batch[0])
        augmented_labels.append(batch[1])
        
        if len(augmented_data) >= 60:  # 60 batches = 60,000 samples
            break
    
    # Combine original and augmented data
    x_augmented = np.concatenate([x_train] + augmented_data)
    y_augmented = np.concatenate([y_train] + augmented_labels)
    
    return x_augmented, y_augmented

def plot_training_history(history):
    """Vẽ biểu đồ lịch sử training"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
    # Plot accuracy
    ax1.plot(history.history['accuracy'], label='Training Accuracy')
    ax1.plot(history.history['val_accuracy'], label='Validation Accuracy')
    ax1.set_title('Model Accuracy')
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Accuracy')
    ax1.legend()
    ax1.grid(True)
    
    # Plot loss
    ax2.plot(history.history['loss'], label='Training Loss')
    ax2.plot(history.history['val_loss'], label='Validation Loss')
    ax2.set_title('Model Loss')
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('Loss')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig('training_history.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("📊 Training history plot saved as 'training_history.png'")

if __name__ == "__main__":
    train()
