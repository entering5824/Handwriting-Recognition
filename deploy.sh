#!/bin/bash

# AI Handwriting Recognition - GitHub Deploy Script
# This script helps deploy the project to GitHub

echo "🚀 AI Handwriting Recognition - GitHub Deploy"
echo "=============================================="

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📁 Initializing git repository..."
    git init
fi

# Check if remote origin exists
if ! git remote | grep -q "origin"; then
    echo "🔗 Please add remote origin first:"
    echo "git remote add origin https://github.com/yourusername/handwriting-recognition.git"
    exit 1
fi

# Add all files
echo "📝 Adding files to git..."
git add .

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo "ℹ️  No changes to commit"
else
    # Commit changes
    echo "💾 Committing changes..."
    git commit -m "feat: AI handwriting recognition system

- Advanced CNN model with 98%+ accuracy
- Modern GUI with CustomTkinter
- Real-time handwriting recognition
- Professional dashboard and analytics
- Comprehensive documentation
- Ready for interview presentations"

    # Push to GitHub
    echo "🚀 Pushing to GitHub..."
    git push origin main
    
    if [ $? -eq 0 ]; then
        echo "✅ Successfully deployed to GitHub!"
        echo "🔗 Repository: https://github.com/yourusername/handwriting-recognition"
    else
        echo "❌ Failed to push to GitHub"
        echo "💡 Try: git push -u origin main"
    fi
fi

echo ""
echo "📋 Next steps:"
echo "1. Update repository description on GitHub"
echo "2. Add topics/tags: ai, machine-learning, cnn, tensorflow, python"
echo "3. Create a release (v1.0.0)"
echo "4. Add demo GIF to README"
echo ""
echo "🎯 Ready for interviews! 🚀"
