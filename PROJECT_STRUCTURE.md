# 📁 Project Structure

Complete visual guide to all files and folders in this project.

---

## 🗂️ Directory Tree

```
apollo-data-scraper/
│
├── 📄 START_HERE.md              ⭐ START HERE - Choose your path
│
├── 🎯 CORE APIFY ACTOR FILES
│   ├── main.js                    Main scraping logic (Node.js + Playwright)
│   ├── package.json               Dependencies and npm scripts
│   ├── Dockerfile                 Docker configuration for Apify
│   ├── actor.json                 Apify actor configuration
│   ├── INPUT_SCHEMA.json          Input field definitions & validation
│   └── apify.json                 Apify CLI configuration
│
├── 📚 DOCUMENTATION (10 FILES!)
│   ├── START_HERE.md             ⭐ Entry point - choose your path
│   ├── QUICK_START.md            ⚡ 5-minute setup guide
│   ├── SETUP_GUIDE.md            📖 Complete setup instructions
│   ├── README.md                 📘 Main documentation
│   ├── USAGE.md                  📊 Detailed usage examples
│   ├── DEPLOYMENT.md             🚀 Deployment to Apify guide
│   ├── CONTRIBUTING.md           🤝 How to contribute
│   ├── PROJECT_SUMMARY.md        📋 Technical overview
│   ├── CHANGELOG.md              📝 Version history
│   ├── CONVERSION_COMPLETE.md    ✅ Conversion summary
│   └── PROJECT_STRUCTURE.md      📁 This file
│
├── 🧪 TESTING & DEVELOPMENT
│   ├── test-local.js             Local testing script with CLI args
│   └── .actor/
│       ├── input.json            Example input configuration
│       └── actor.json            Actor metadata for Apify
│
├── 🔧 CONFIGURATION FILES
│   ├── .gitignore                Git ignore patterns
│   └── .dockerignore             Docker ignore patterns
│
├── 📜 ORIGINAL CHROME EXTENSION
│   └── chrome-extension-original/
│       ├── manifest.json         Chrome extension manifest
│       ├── popup.html            Extension popup UI
│       ├── popup.js              Extension scraping logic
│       ├── clip.png              Extension icon
│       └── README.md             Original extension docs
│
└── 📄 LICENSE
    └── LICENSE.md                MIT License
```

---

## 📄 File Descriptions

### 🎯 Core Files (Must Have)

| File | Purpose | Lines | Required? |
|------|---------|-------|-----------|
| **main.js** | Main scraping logic | ~200 | ✅ Yes |
| **package.json** | Dependencies & scripts | ~30 | ✅ Yes |
| **Dockerfile** | Docker build config | ~20 | ✅ Yes |
| **actor.json** | Apify configuration | ~50 | ✅ Yes |
| **INPUT_SCHEMA.json** | Input validation | ~60 | ✅ Yes |

### 📚 Documentation Files

| File | Purpose | Audience | Pages |
|------|---------|----------|-------|
| **START_HERE.md** | Entry point | Everyone | 2 |
| **QUICK_START.md** | 5-min guide | Beginners | 4 |
| **SETUP_GUIDE.md** | Complete setup | All levels | 10 |
| **README.md** | Main docs | Everyone | 8 |
| **USAGE.md** | Usage examples | Users | 12 |
| **DEPLOYMENT.md** | Deployment | DevOps | 10 |
| **CONTRIBUTING.md** | Contribute | Developers | 8 |
| **PROJECT_SUMMARY.md** | Tech overview | Developers | 15 |
| **CHANGELOG.md** | History | Everyone | 2 |
| **CONVERSION_COMPLETE.md** | Summary | Everyone | 5 |

**Total Documentation**: 10 files, ~76 pages! 📖

### 🧪 Testing Files

| File | Purpose | Usage |
|------|---------|-------|
| **test-local.js** | Local testing | `npm run test` |
| **.actor/input.json** | Example input | Reference |
| **.actor/actor.json** | Actor metadata | Apify setup |

### 🔧 Config Files

| File | Purpose |
|------|---------|
| **.gitignore** | Git ignore rules |
| **.dockerignore** | Docker ignore rules |
| **apify.json** | CLI configuration |

### 📜 Original Extension

| File | Purpose |
|------|---------|
| **manifest.json** | Extension config |
| **popup.html** | UI layout |
| **popup.js** | Scraping logic |
| **clip.png** | Icon |

---

## 🎯 Quick Navigation

### I Want To...

#### ...Start Immediately
→ Read **[START_HERE.md](START_HERE.md)**

#### ...Set Up in 5 Minutes
→ Read **[QUICK_START.md](QUICK_START.md)**

#### ...Understand Everything
→ Read **[README.md](README.md)**

#### ...See Usage Examples
→ Read **[USAGE.md](USAGE.md)**

#### ...Deploy to Apify
→ Read **[DEPLOYMENT.md](DEPLOYMENT.md)**

#### ...Contribute Code
→ Read **[CONTRIBUTING.md](CONTRIBUTING.md)**

#### ...See Technical Details
→ Read **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)**

#### ...Test Locally
→ Run `npm run test:quick`

#### ...Modify the Scraper
→ Edit **main.js**

---

## 📊 File Statistics

### By Category

| Category | Files | Total Lines |
|----------|-------|-------------|
| Core Code | 6 | ~400 |
| Documentation | 11 | ~3,000 |
| Testing | 3 | ~200 |
| Config | 3 | ~50 |
| Original | 5 | ~250 |
| **TOTAL** | **28** | **~3,900** |

### By Type

| Type | Count | Purpose |
|------|-------|---------|
| JavaScript | 2 | Scraping logic & testing |
| JSON | 6 | Configuration |
| Markdown | 11 | Documentation |
| Docker | 2 | Containerization |
| HTML | 1 | Extension UI (original) |
| Image | 1 | Extension icon (original) |

---

## 🔍 Detailed Breakdown

### main.js (Core Scraper)

```javascript
// Structure:
1. Imports (Apify SDK, Playwright)
2. extractTableData() - Extract data from tables
3. Actor.main() - Main scraping logic
   - Input validation
   - Browser setup
   - Page iteration
   - Data extraction
   - Dataset storage
```

**Key Functions**:
- `extractTableData()` - Parse HTML tables
- `Actor.main()` - Main execution flow
- Data cleaning & formatting
- Phone number formatting
- Error handling

### package.json (Dependencies)

```json
{
  "dependencies": {
    "apify": "^3.1.0",      // Apify SDK
    "playwright": "^1.40.0"  // Browser automation
  },
  "scripts": {
    "start": "node main.js",           // Production run
    "test": "node test-local.js",      // Local test
    "test:quick": "... --pages 1",     // Quick test
    "test:full": "... --pages 5"       // Full test
  }
}
```

### INPUT_SCHEMA.json (User Inputs)

```json
{
  "url": "Apollo.io list URL (required)",
  "numberOfPages": "1-100 pages (required)",
  "timeBetweenPages": "2-30 seconds (optional)",
  "proxyConfiguration": "Proxy settings (optional)"
}
```

### test-local.js (Testing Tool)

**Features**:
- Command-line arguments
- Visible browser mode
- Progress logging
- Data quality stats
- JSON export
- Sample output

**Usage**:
```bash
npm run test:quick              # 1 page test
npm run test:full               # 5 pages test
node test-local.js --pages 10   # Custom test
```

---

## 🎨 Visual Flow

```
USER INPUT
    ↓
[INPUT_SCHEMA.json] validates
    ↓
[main.js] processes
    ↓
[Playwright] launches browser
    ↓
[Apollo.io] scrapes data
    ↓
[Dataset] stores results
    ↓
USER DOWNLOADS (CSV/JSON/Excel)
```

---

## 📦 What Gets Deployed

When you deploy to Apify, these files are used:

```
Deployment Package:
├── main.js              ✅ (Execution)
├── package.json         ✅ (Dependencies)
├── Dockerfile           ✅ (Container)
├── actor.json           ✅ (Config)
├── INPUT_SCHEMA.json    ✅ (Input UI)
└── README.md            ✅ (Docs)

NOT deployed:
├── test-local.js        ❌ (Local only)
├── chrome-extension-*   ❌ (Reference)
└── *.md files           ❌ (Optional)
```

---

## 🔄 Development Workflow

```
1. EDIT CODE
   ↓ main.js
   
2. TEST LOCALLY
   ↓ npm run test:quick
   
3. COMMIT & PUSH
   ↓ git push
   
4. BUILD ON APIFY
   ↓ Apify Console
   
5. RUN & GET DATA
   ↓ Download results
```

---

## 📝 Maintenance

### Files You Might Edit

| File | Reason to Edit |
|------|----------------|
| **main.js** | Change scraping logic |
| **INPUT_SCHEMA.json** | Add input fields |
| **test-local.js** | Modify testing |
| **package.json** | Update dependencies |
| **README.md** | Update docs |

### Files You Shouldn't Edit

| File | Why Not |
|------|---------|
| **Dockerfile** | Standard Apify setup |
| **actor.json** | Core config |
| **.gitignore** | Standard ignores |

---

## 🎓 Learning Resources

### For Each File Type

**JavaScript (.js)**
- [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Node.js Docs](https://nodejs.org/docs)
- [Playwright Docs](https://playwright.dev)

**JSON**
- [JSON Tutorial](https://www.json.org)
- [Apify Input Schema](https://docs.apify.com/actors/development/input-schema)

**Markdown (.md)**
- [Markdown Guide](https://www.markdownguide.org)

**Docker**
- [Docker Docs](https://docs.docker.com)
- [Apify Dockerfile](https://docs.apify.com/actors/development/build)

---

## ✅ Checklist for New Users

- [ ] Read START_HERE.md
- [ ] Choose a path (Quick/Setup/Complete)
- [ ] Install dependencies (`npm install`)
- [ ] Test locally (`npm run test:quick`)
- [ ] Deploy to Apify
- [ ] Run first scrape
- [ ] Download data
- [ ] Set up schedule
- [ ] Integrate with tools

---

## 🎯 Success Metrics

### What's Included

✅ **28 total files**  
✅ **11 documentation files** (~3,000 lines)  
✅ **6 core code files** (~400 lines)  
✅ **3 testing files**  
✅ **Production-ready**  
✅ **Free tier optimized**  
✅ **Fully documented**  

---

**Need help navigating?** Start with [START_HERE.md](START_HERE.md)! 👋



