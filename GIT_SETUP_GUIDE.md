# 🚀 Git Setup & Repository Upload Guide

## Step 1: Install Git (If Not Installed)

### Download Git for Windows
1. Go to: https://git-scm.com/download/windows
2. Download the installer
3. Run the installer (use default settings)
4. Restart your terminal/PowerShell

### Verify Installation
```bash
git --version
```

---

## Step 2: Configure Git (First Time Only)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## Step 3: Clean Your GitHub Repository

### Option A: Via GitHub Website (Easiest - No Git Required)

1. Go to: https://github.com/abdulwasay8126/apollo-2.0
2. Delete all existing files:
   - Click on each file
   - Click the trash icon (🗑️)
   - Commit the deletion
3. Upload new README.md:
   - Click "Add file" → "Upload files"
   - Drag `README.md` from this project
   - Commit the changes

### Option B: Via Git Command Line (After Installing Git)

```bash
# Navigate to your project
cd "C:\Cursor Projects\apollo\apollo-email-scraper-main"

# Initialize git (if not already)
git init

# Add your remote repository
git remote add origin https://github.com/abdulwasay8126/apollo-2.0.git

# Create a new branch
git checkout -b main

# Stage only README first
git add README.md

# Commit
git commit -m "Initial commit: Add comprehensive README"

# Force push to clean the repository
git push -f origin main
```

---

## Step 4: Add All Other Files

### After README is uploaded:

```bash
# Stage all files
git add .

# Commit everything
git commit -m "Add complete Apify scraper with documentation"

# Push to GitHub
git push origin main
```

---

## Step 5: Verify on GitHub

Go to: https://github.com/abdulwasay8126/apollo-2.0

You should see all your new files!

---

## Quick Commands Reference

```bash
# Check status
git status

# Stage specific file
git add filename.js

# Stage all files
git add .

# Commit with message
git commit -m "Your message here"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main
```

---

## Troubleshooting

### Error: "Git is not recognized"
- Install Git from git-scm.com
- Restart terminal

### Error: "Permission denied"
- Set up SSH key or use HTTPS with personal access token
- See: https://docs.github.com/en/authentication

### Error: "Repository not found"
- Check repository URL
- Make sure you have access

---

**Need help?** Open an issue on GitHub!


