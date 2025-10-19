"""
Quick Demo Script for AI Handwriting Recognition System
Perfect for interviews and presentations
"""

import os
import sys
import time
import numpy as np
from PIL import Image, ImageDraw

def print_demo_banner():
    """Print demo banner"""
    print("\n" + "="*60)
    print("🎯 AI HANDWRITING RECOGNITION - LIVE DEMO")
    print("="*60)
    print("📋 This demo will showcase:")
    print("   • Real-time handwriting recognition")
    print("   • Advanced CNN model with 98%+ accuracy") 
    print("   • Professional GUI interface")
    print("   • Model analytics and performance metrics")
    print("="*60)

def check_system():
    """Check system requirements"""
    print("\n🔍 SYSTEM CHECK")
    print("-" * 30)
    
    # Check Python version
    print(f"Python: {sys.version.split()[0]} ✅")
    
    # Check dependencies
    required_packages = ['tensorflow', 'customtkinter', 'opencv-python', 'matplotlib', 'numpy']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"{package}: ✅")
        except ImportError:
            print(f"{package}: ❌")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        print("Please run: pip install -r requirements.txt")
        return False
    
    # Check model
    if os.path.exists("handwriting_model.h5"):
        model_size = os.path.getsize("handwriting_model.h5") / (1024 * 1024)
        print(f"Model: ✅ Available ({model_size:.1f} MB)")
    else:
        print("Model: ❌ Not found")
        print("💡 Training a model...")
        try:
            from train import train
            train()
            print("✅ Model trained successfully!")
        except Exception as e:
            print(f"❌ Training failed: {e}")
            return False
    
    return True

def demo_gui():
    """Launch GUI demo"""
    print("\n🎨 LAUNCHING GUI DEMO")
    print("-" * 30)
    print("The GUI application will open in a new window.")
    print("Try drawing digits 0-9 in the canvas!")
    
    input("\nPress Enter to launch GUI...")
    
    try:
        import gui
        gui.main()
    except Exception as e:
        print(f"❌ GUI demo failed: {e}")

def demo_command_line():
    """Demo command line functionality"""
    print("\n💻 COMMAND LINE DEMO")
    print("-" * 30)
    
    # Create a sample image for demo
    print("Creating sample handwritten digit...")
    
    # Create a simple "7" digit
    img = Image.new("L", (28, 28), 255)
    draw = ImageDraw.Draw(img)
    
    # Draw a "7"
    draw.line([(5, 5), (20, 5)], fill=0, width=2)  # Top horizontal
    draw.line([(20, 5), (15, 20)], fill=0, width=2)  # Diagonal
    draw.line([(10, 20), (15, 20)], fill=0, width=2)  # Bottom horizontal
    
    # Save demo image
    img.save("demo_digit.png")
    print("✅ Sample digit saved as 'demo_digit.png'")
    
    # Predict
    try:
        from predict import predict
        result = predict("demo_digit.png")
        print(f"🎯 Prediction: {result}")
        print("✅ Command line prediction successful!")
    except Exception as e:
        print(f"❌ Prediction failed: {e}")

def demo_reports():
    """Generate demo reports"""
    print("\n📊 GENERATING DEMO REPORTS")
    print("-" * 30)
    
    try:
        from report_generator import ReportGenerator
        generator = ReportGenerator()
        
        print("Generating model report...")
        report = generator.generate_model_report()
        
        # Save report
        import json
        with open("demo_report.json", "w") as f:
            json.dump(report, f, indent=2, default=str)
        
        print("✅ Demo report generated!")
        print(f"📈 Model Accuracy: {report.get('performance', {}).get('test_accuracy', 'N/A'):.4f}")
        print(f"🔢 Total Parameters: {report.get('model_info', {}).get('total_parameters', 'N/A'):,}")
        
    except Exception as e:
        print(f"❌ Report generation failed: {e}")

def main():
    """Main demo function"""
    print_demo_banner()
    
    # System check
    if not check_system():
        print("\n❌ System check failed. Please fix issues and try again.")
        return
    
    print("\n✅ System ready for demo!")
    
    # Demo options
    while True:
        print("\n📋 DEMO OPTIONS")
        print("=" * 30)
        print("1. 🎨 GUI Demo (Recommended)")
        print("2. 💻 Command Line Demo")
        print("3. 📊 Generate Reports")
        print("4. 🚪 Exit Demo")
        print("=" * 30)
        
        choice = input("\nSelect demo option (1-4): ").strip()
        
        if choice == "1":
            demo_gui()
        elif choice == "2":
            demo_command_line()
        elif choice == "3":
            demo_reports()
        elif choice == "4":
            print("\n👋 Demo completed! Thank you!")
            break
        else:
            print("❌ Invalid choice. Please select 1-4.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
