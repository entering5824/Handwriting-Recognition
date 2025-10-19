"""
AI Handwriting Recognition System - Command Line Interface
"""

import os
import sys
from train import train
from predict import predict
from report_generator import ReportGenerator

def print_banner():
    """Print application banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                🤖 AI Handwriting Recognition System          ║
    ║                                                              ║
    ║           Powered by Deep Learning & Computer Vision        ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def show_menu():
    """Display main menu"""
    print("\n📋 MAIN MENU")
    print("=" * 50)
    print("1. 🏋️  Train Model")
    print("2. 🔮 Predict from Image")
    print("3. 🎨 Launch GUI Application")
    print("4. 📊 Generate Reports")
    print("5. ℹ️  Show System Info")
    print("6. 🚪 Exit")
    print("=" * 50)

def train_model():
    """Train the handwriting recognition model"""
    print("\n🏋️ TRAINING MODEL")
    print("-" * 30)
    print("This will train a new CNN model on the MNIST dataset...")
    print("Training may take several minutes depending on your hardware.")
    
    confirm = input("\nProceed with training? (y/N): ").lower()
    if confirm == 'y':
        try:
            train()
            print("\n✅ Training completed successfully!")
        except Exception as e:
            print(f"\n❌ Training failed: {e}")
    else:
        print("Training cancelled.")

def predict_image():
    """Predict handwriting from image file"""
    print("\n🔮 HANDWRITING PREDICTION")
    print("-" * 30)
    
    image_path = input("Enter image path: ").strip()
    
    if not os.path.exists(image_path):
        print("❌ Image file not found!")
        return
    
    try:
        result = predict(image_path)
        print(f"\n🎯 Recognition Result: {result}")
        
        # Show confidence if available
        if hasattr(predict, 'last_confidence'):
            print(f"📊 Confidence: {predict.last_confidence:.2%}")
            
    except Exception as e:
        print(f"❌ Prediction failed: {e}")

def launch_gui():
    """Launch GUI application"""
    print("\n🎨 LAUNCHING GUI APPLICATION")
    print("-" * 30)
    
    try:
        import gui
        print("Starting GUI application...")
        gui.main()
    except ImportError:
        print("❌ GUI module not found!")
    except Exception as e:
        print(f"❌ Failed to launch GUI: {e}")

def generate_reports():
    """Generate model reports and demo materials"""
    print("\n📊 GENERATING REPORTS")
    print("-" * 30)
    
    try:
        generator = ReportGenerator()
        
        print("Generating comprehensive reports...")
        report = generator.generate_model_report()
        
        # Save JSON report
        import json
        with open("model_report.json", "w") as f:
            json.dump(report, f, indent=2, default=str)
        
        # Generate visualizations
        generator.create_confusion_matrix()
        generator.create_sample_predictions()
        
        # Generate HTML report
        generator.generate_html_report()
        
        # Generate demo script
        generator.generate_demo_script()
        
        print("\n✅ Reports generated successfully!")
        print("\n📁 Generated files:")
        print("  - model_report.json")
        print("  - model_report.html") 
        print("  - confusion_matrix.png")
        print("  - sample_predictions.png")
        print("  - demo_script.md")
        
    except Exception as e:
        print(f"❌ Report generation failed: {e}")

def show_system_info():
    """Display system information"""
    print("\nℹ️  SYSTEM INFORMATION")
    print("-" * 30)
    
    print(f"Python Version: {sys.version}")
    print(f"Working Directory: {os.getcwd()}")
    
    # Check if model exists
    model_path = "handwriting_model.h5"
    if os.path.exists(model_path):
        model_size = os.path.getsize(model_path) / (1024 * 1024)  # MB
        print(f"Model Status: ✅ Available ({model_size:.1f} MB)")
    else:
        print("Model Status: ❌ Not found (train model first)")
    
    # Check dependencies
    dependencies = ["tensorflow", "customtkinter", "opencv-python", "matplotlib", "numpy"]
    print("\nDependencies:")
    for dep in dependencies:
        try:
            __import__(dep.replace("-", "_"))
            print(f"  ✅ {dep}")
        except ImportError:
            print(f"  ❌ {dep}")

def main():
    """Main application loop"""
    print_banner()
    
    while True:
        show_menu()
        
        try:
            choice = input("\nSelect option (1-6): ").strip()
            
            if choice == "1":
                train_model()
            elif choice == "2":
                predict_image()
            elif choice == "3":
                launch_gui()
            elif choice == "4":
                generate_reports()
            elif choice == "5":
                show_system_info()
            elif choice == "6":
                print("\n👋 Thank you for using AI Handwriting Recognition System!")
                break
            else:
                print("❌ Invalid choice! Please select 1-6.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
