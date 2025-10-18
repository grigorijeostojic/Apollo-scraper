# 🚀 Quick Upload Guide - Apollo.io Apify Scraper

## ⚡ Fastest Method (3 Options)

---

## Option 1: Automated Script (Recommended) ✅

### Step 1: Install Git
1. Download: https://git-scm.com/download/windows
2. Install with default settings
3. Restart PowerShell

### Step 2: Run Upload Script

**Right-click on one of these files and select "Run":**
- `setup-git-and-upload.bat` (Windows Batch)
- OR `setup-git-and-upload.ps1` (PowerShell)

**The script will:**
1. ✅ Configure Git
2. ✅ Initialize repository
3. ✅ Add remote (your GitHub repo)
4. ✅ Commit README first
5. ✅ Push README to GitHub
6. ✅ Ask if you want to upload all other files
7. ✅ Upload everything

---

## Option 2: Manual Commands (If Git is Already Installed)

```bash
# Open PowerShell and run these commands:

cd "C:\Cursor Projects\apollo\apollo-email-scraper-main"

# Configure Git (first time only)
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# Initialize
git init

# Add remote
git remote add origin https://github.com/abdulwasay8126/apollo-2.0.git

# Create main branch
git checkout -b main

# Commit README only
git add README.md
git commit -m "Initial commit: Add comprehensive README"
git push -f origin main

# Then add everything else
git add .
git commit -m "Add complete Apify scraper with documentation"
git push origin main
```

**Done! Check: https://github.com/abdulwasay8126/apollo-2.0**

---

## Option 3: GitHub Website (No Git Required)

### Step 1: Delete Old Files
1. Go to https://github.com/abdulwasay8126/apollo-2.0
2. Delete all 6 old files one by one

### Step 2: Upload README
1. Click "Add file" → "Upload files"
2. Drag `README.md`
3. Commit

### Step 3: Upload Everything Else
1. Click "Add file" → "Upload files"
2. Drag all other files
3. Commit

---

## 🎯 What Gets Uploaded

### Core Files (6):
- main.js
- package.json
- Dockerfile
- actor.json
- INPUT_SCHEMA.json
- apify.json

### Documentation (11):
- README.md
- START_HERE.md
- QUICK_START.md
- SETUP_GUIDE.md
- USAGE.md
- DEPLOYMENT.md
- CONTRIBUTING.md
- PROJECT_SUMMARY.md
- PROJECT_STRUCTURE.md
- CONVERSION_COMPLETE.md
- CHANGELOG.md

### Testing (1):
- test-local.js

### Config (2):
- .gitignore
- .dockerignore

### Folders:
- .actor/ (2 files)
- chrome-extension-original/ (5 files)

**Total: 28 files**

---

## ⚠️ Important Notes

### Authentication
When pushing to GitHub, you'll be asked for credentials:
- **Username**: abdulwasay8126
- **Password**: Use a Personal Access Token, NOT your GitHub password

### Get Personal Access Token:
1. Go to: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Give it a name: "Apollo Scraper Upload"
4. Select scope: ✅ `repo` (full control)
5. Click "Generate token"
6. **Copy the token** (you won't see it again!)
7. Use this token as your password when Git asks

---

## ✅ Verification

After uploading, check your repository:
https://github.com/abdulwasay8126/apollo-2.0

You should see:
- ✅ 28 files
- ✅ Beautiful README
- ✅ Complete documentation
- ✅ Ready to deploy to Apify

---

## 🎉 Next Steps

1. ✅ Update repository description on GitHub
2. ✅ Add topics: `apify`, `apollo-io`, `scraper`, `data-extraction`
3. ✅ Enable GitHub Pages (optional)
4. ✅ Deploy to Apify using the QUICK_START.md guide
5. ✅ Start scraping!

---

## Need Help?

- **Git not working?** → See `GIT_SETUP_GUIDE.md`
- **Detailed steps?** → See `UPLOAD_INSTRUCTIONS.md`
- **Script errors?** → Run commands manually (Option 2)

**Choose Option 1 (Automated Script) for easiest upload!**


