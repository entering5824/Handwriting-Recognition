#!/usr/bin/env python3
"""
Setup script for AI Handwriting Recognition System
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages from requirements.txt"""
    print("🔧 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    print("🐍 Checking Python version...")
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required!")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def create_directories():
    """Create necessary directories"""
    print("📁 Creating directories...")
    directories = ["models", "data", "logs", "exports"]
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✅ Created directory: {directory}")
        else:
            print(f"📁 Directory already exists: {directory}")

def main():
    """Main setup function"""
    print("🚀 AI Handwriting Recognition System Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        print("❌ Setup failed!")
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    print("\n" + "=" * 50)
    print("🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Run 'python train.py' to train the model")
    print("2. Run 'python gui.py' to launch the application")
    print("3. Or run 'python main.py' for command-line interface")
    print("\n💡 For help, check the README.md file")

if __name__ == "__main__":
    main()
