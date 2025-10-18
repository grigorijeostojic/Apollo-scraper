# Apollo.io Apify Scraper - Git Upload Script (PowerShell)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Apollo.io Apify Scraper - Git Upload" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Git is installed
try {
    $gitVersion = git --version
    Write-Host "[OK] Git is installed: $gitVersion" -ForegroundColor Green
    Write-Host ""
} catch {
    Write-Host "[ERROR] Git is not installed!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Git first:" -ForegroundColor Yellow
    Write-Host "1. Go to: https://git-scm.com/download/windows"
    Write-Host "2. Download and install Git"
    Write-Host "3. Restart PowerShell"
    Write-Host "4. Run this script again"
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

# Navigate to project directory
Set-Location "C:\Cursor Projects\apollo\apollo-email-scraper-main"
Write-Host "Current directory: $(Get-Location)" -ForegroundColor Cyan
Write-Host ""

# Configure Git
Write-Host "Setting up Git configuration..." -ForegroundColor Cyan
$gitName = Read-Host "Enter your name (for Git commits)"
$gitEmail = Read-Host "Enter your email (for Git commits)"

git config --global user.name "$gitName"
git config --global user.email "$gitEmail"
Write-Host ""

# Step 1: Initialize Git
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Step 1: Initialize Git Repository" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

if (-not (Test-Path ".git")) {
    git init
    Write-Host "[OK] Git repository initialized" -ForegroundColor Green
} else {
    Write-Host "[OK] Git repository already exists" -ForegroundColor Green
}
Write-Host ""

# Step 2: Add Remote
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Step 2: Add Remote Repository" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

git remote remove origin 2>$null
git remote add origin https://github.com/abdulwasay8126/apollo-2.0.git
Write-Host "[OK] Remote repository added" -ForegroundColor Green
Write-Host ""

# Step 3: Create Main Branch
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Step 3: Create Main Branch" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

git checkout -b main 2>$null
if ($LASTEXITCODE -ne 0) {
    git checkout main
}
Write-Host "[OK] On main branch" -ForegroundColor Green
Write-Host ""

# Step 4: Stage README
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Step 4: Stage README.md ONLY" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

git add README.md
Write-Host "[OK] README.md staged" -ForegroundColor Green
Write-Host ""

# Step 5: Commit README
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Step 5: Commit README" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

git commit -m "Initial commit: Add comprehensive Apify scraper README"
Write-Host "[OK] README committed" -ForegroundColor Green
Write-Host ""

# Step 6: Push README
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Step 6: Push README to GitHub" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "IMPORTANT: This will REPLACE all files in your GitHub repository!" -ForegroundColor Yellow
Write-Host "Repository: https://github.com/abdulwasay8126/apollo-2.0" -ForegroundColor Yellow
Write-Host ""

$confirm = Read-Host "Are you sure you want to continue? (yes/no)"

if ($confirm -ne "yes") {
    Write-Host ""
    Write-Host "Upload cancelled. No changes made to GitHub." -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 0
}

Write-Host ""
Write-Host "Pushing to GitHub (you may be asked for credentials)..." -ForegroundColor Cyan
git push -f origin main

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "[ERROR] Failed to push to GitHub!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Possible reasons:" -ForegroundColor Yellow
    Write-Host "1. Authentication failed - you may need a Personal Access Token"
    Write-Host "2. Network issue"
    Write-Host "3. Repository doesn't exist"
    Write-Host ""
    Write-Host "To fix authentication:" -ForegroundColor Yellow
    Write-Host "1. Go to: https://github.com/settings/tokens"
    Write-Host "2. Generate new token (classic)"
    Write-Host "3. Give it 'repo' permissions"
    Write-Host "4. Use the token as your password when pushing"
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "[OK] README successfully pushed to GitHub!" -ForegroundColor Green
Write-Host ""

# Step 7: Add remaining files
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Step 7: Add All Other Files" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$addAll = Read-Host "Do you want to add all other files now? (yes/no)"

if ($addAll -ne "yes") {
    Write-Host ""
    Write-Host "Stopping here. README is uploaded." -ForegroundColor Yellow
    Write-Host "Run this script again to upload remaining files." -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 0
}

Write-Host ""
Write-Host "Staging all files..." -ForegroundColor Cyan
git add .

Write-Host ""
Write-Host "Committing all files..." -ForegroundColor Cyan
git commit -m "Add complete Apify scraper with documentation and tools"

Write-Host ""
Write-Host "Pushing all files to GitHub..." -ForegroundColor Cyan
git push origin main

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "[ERROR] Failed to push remaining files!" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "SUCCESS!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "All files have been uploaded to:" -ForegroundColor Cyan
Write-Host "https://github.com/abdulwasay8126/apollo-2.0" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Visit your repository on GitHub"
Write-Host "2. Check that all files are there"
Write-Host "3. Update repository description"
Write-Host "4. Add topics: apify, apollo-io, scraper"
Write-Host ""
Read-Host "Press Enter to exit"


