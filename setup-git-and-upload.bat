@echo off
echo ========================================
echo Apollo.io Apify Scraper - Git Upload
echo ========================================
echo.

REM Check if Git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Git is not installed!
    echo.
    echo Please install Git first:
    echo 1. Go to: https://git-scm.com/download/windows
    echo 2. Download and install Git
    echo 3. Restart this terminal
    echo 4. Run this script again
    echo.
    pause
    exit /b 1
)

echo [OK] Git is installed!
echo.

REM Navigate to project directory
cd /d "C:\Cursor Projects\apollo\apollo-email-scraper-main"

echo Current directory: %CD%
echo.

REM Configure Git (optional - update with your info)
echo Setting up Git configuration...
set /p git_name="Enter your name (for Git commits): "
set /p git_email="Enter your email (for Git commits): "

git config --global user.name "%git_name%"
git config --global user.email "%git_email%"

echo.
echo ========================================
echo Step 1: Initialize Git Repository
echo ========================================

REM Initialize git if not already
if not exist .git (
    git init
    echo [OK] Git repository initialized
) else (
    echo [OK] Git repository already exists
)

echo.
echo ========================================
echo Step 2: Add Remote Repository
echo ========================================

REM Remove existing origin if exists
git remote remove origin 2>nul

REM Add remote
git remote add origin https://github.com/abdulwasay8126/apollo-2.0.git
echo [OK] Remote repository added

echo.
echo ========================================
echo Step 3: Create Main Branch
echo ========================================

git checkout -b main 2>nul || git checkout main
echo [OK] On main branch

echo.
echo ========================================
echo Step 4: Stage README.md ONLY
echo ========================================

git add README.md
echo [OK] README.md staged

echo.
echo ========================================
echo Step 5: Commit README
echo ========================================

git commit -m "Initial commit: Add comprehensive Apify scraper README"
echo [OK] README committed

echo.
echo ========================================
echo Step 6: Push README to GitHub
echo ========================================

echo.
echo IMPORTANT: This will REPLACE all files in your GitHub repository!
echo Repository: https://github.com/abdulwasay8126/apollo-2.0
echo.
set /p confirm="Are you sure you want to continue? (yes/no): "

if /i not "%confirm%"=="yes" (
    echo.
    echo Upload cancelled. No changes made to GitHub.
    pause
    exit /b 0
)

echo.
echo Pushing to GitHub (you may be asked for credentials)...
git push -f origin main

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Failed to push to GitHub!
    echo.
    echo Possible reasons:
    echo 1. Authentication failed - you may need a Personal Access Token
    echo 2. Network issue
    echo 3. Repository doesn't exist
    echo.
    echo To fix authentication:
    echo 1. Go to: https://github.com/settings/tokens
    echo 2. Generate new token (classic)
    echo 3. Give it 'repo' permissions
    echo 4. Use the token as your password when pushing
    echo.
    pause
    exit /b 1
)

echo.
echo [OK] README successfully pushed to GitHub!
echo.
echo ========================================
echo Step 7: Add All Other Files
echo ========================================
echo.

set /p add_all="Do you want to add all other files now? (yes/no): "

if /i not "%add_all%"=="yes" (
    echo.
    echo Stopping here. README is uploaded.
    echo Run this script again to upload remaining files.
    pause
    exit /b 0
)

echo.
echo Staging all files...
git add .

echo.
echo Committing all files...
git commit -m "Add complete Apify scraper with documentation and tools"

echo.
echo Pushing all files to GitHub...
git push origin main

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Failed to push remaining files!
    pause
    exit /b 1
)

echo.
echo ========================================
echo SUCCESS! 
echo ========================================
echo.
echo All files have been uploaded to:
echo https://github.com/abdulwasay8126/apollo-2.0
echo.
echo Next steps:
echo 1. Visit your repository on GitHub
echo 2. Check that all files are there
echo 3. Update repository description
echo 4. Add topics: apify, apollo-io, scraper
echo.
pause


