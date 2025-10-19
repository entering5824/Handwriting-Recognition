@echo off
echo 🚀 AI Handwriting Recognition - GitHub Deploy
echo ==============================================

REM Check if git is initialized
if not exist ".git" (
    echo 📁 Initializing git repository...
    git init
)

REM Check if remote origin exists
git remote | findstr "origin" >nul
if errorlevel 1 (
    echo 🔗 Please add remote origin first:
    echo git remote add origin https://github.com/yourusername/handwriting-recognition.git
    pause
    exit /b 1
)

REM Add all files
echo 📝 Adding files to git...
git add .

REM Commit changes
echo 💾 Committing changes...
git commit -m "feat: AI handwriting recognition system

- Advanced CNN model with 98%%+ accuracy
- Modern GUI with CustomTkinter
- Real-time handwriting recognition
- Professional dashboard and analytics
- Comprehensive documentation
- Ready for interview presentations"

REM Push to GitHub
echo 🚀 Pushing to GitHub...
git push origin main

if %errorlevel% equ 0 (
    echo ✅ Successfully deployed to GitHub!
    echo 🔗 Repository: https://github.com/yourusername/handwriting-recognition
) else (
    echo ❌ Failed to push to GitHub
    echo 💡 Try: git push -u origin main
)

echo.
echo 📋 Next steps:
echo 1. Update repository description on GitHub
echo 2. Add topics/tags: ai, machine-learning, cnn, tensorflow, python
echo 3. Create a release (v1.0.0)
echo 4. Add demo GIF to README
echo.
echo 🎯 Ready for interviews! 🚀

pause
