# 🛠️ Complete Setup Guide - Apollo.io Data Scraper

This comprehensive guide covers every step to get your Apollo.io scraper up and running.

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Deployment to Apify](#deployment-to-apify)
3. [Local Development Setup](#local-development-setup)
4. [Configuration](#configuration)
5. [Testing](#testing)
6. [Scheduling Automated Runs](#scheduling)
7. [Troubleshooting](#troubleshooting)

---

## 1️⃣ Prerequisites

### Required Accounts

✅ **Apify Account** (Free)
- Go to [apify.com](https://apify.com)
- Click "Sign up for free"
- Confirm your email
- You get $5/month free credit

✅ **Apollo.io Account** (Required for scraping)
- Sign up at [apollo.io](https://www.apollo.io)
- Log in before using the scraper
- Make sure you have access to lists

✅ **GitHub Account** (For deployment)
- Sign up at [github.com](https://github.com)
- Free account works perfectly

### Optional but Recommended

- Git installed locally
- Node.js 18+ (for local testing)
- VS Code or code editor (for customization)

---

## 2️⃣ Deployment to Apify (Cloud)

### Option A: Via Apify Console (Easiest - No Code Required)

#### Step 1: Get the Code

1. Go to this repository on GitHub
2. Click **"Fork"** button (top right)
3. This creates a copy in your GitHub account

#### Step 2: Create Apify Actor

1. Log into [Apify Console](https://console.apify.com)
2. Click **"Actors"** in left sidebar
3. Click **"Create new"** button
4. Select **"From Git repository"**

#### Step 3: Configure Actor

Fill in the form:

```
Git URL: https://github.com/YOUR_USERNAME/apollo-data-scraper
Name: apollo-data-scraper
Title: Apollo.io Data Scraper
Build tag: latest
```

Click **"Create"**

#### Step 4: Build the Actor

1. Click **"Build"** button
2. Wait 2-3 minutes for Docker image to build
3. Look for green checkmark ✅

#### Step 5: Run Your First Scrape

1. Click **"Start"** button
2. Enter this input:

```json
{
  "url": "https://app.apollo.io/#/people?page=1",
  "numberOfPages": 2,
  "timeBetweenPages": 5
}
```

3. Click **"Start"**
4. Wait for completion (~30-60 seconds)

#### Step 6: Get Your Data

1. Click **"Dataset"** tab
2. Click **"Export"**
3. Choose **"CSV"** format
4. Download your contacts! 🎉

---

### Option B: Via Apify CLI (For Developers)

#### Step 1: Install Apify CLI

```bash
npm install -g apify-cli
```

#### Step 2: Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/apollo-data-scraper.git
cd apollo-data-scraper
```

#### Step 3: Login to Apify

```bash
apify login
```

This opens a browser for authentication.

#### Step 4: Deploy

```bash
apify push
```

This will:
- Create actor on Apify
- Upload your code
- Build Docker image
- Make it ready to run

#### Step 5: Run from CLI

```bash
apify call --input '{
  "url": "https://app.apollo.io/#/people?page=1",
  "numberOfPages": 5,
  "timeBetweenPages": 5
}'
```

---

## 3️⃣ Local Development Setup

### Step 1: Install Dependencies

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/apollo-data-scraper.git
cd apollo-data-scraper

# Install npm packages
npm install
```

### Step 2: Configure Input

Edit `.actor/input.json`:

```json
{
  "url": "https://app.apollo.io/#/people?page=1",
  "numberOfPages": 2,
  "timeBetweenPages": 5
}
```

### Step 3: Run Locally

```bash
# Quick test (1 page, visible browser)
npm run test:quick

# Full test (5 pages)
npm run test:full

# Custom test
node test-local.js --url "YOUR_URL" --pages 10 --delay 5

# Run as Apify actor (production mode)
npm start
```

---

## 4️⃣ Configuration

### Input Parameters Explained

#### url (Required)
```json
"url": "https://app.apollo.io/#/people?finderViewId=12345&page=1"
```

- Must start with `https://app.apollo.io/`
- Should be a list or search URL
- Get it from your Apollo.io browser address bar

#### numberOfPages (Required)
```json
"numberOfPages": 10
```

- Minimum: 1
- Maximum: 100
- Each page has ~25 contacts
- 10 pages = ~250 contacts

#### timeBetweenPages (Optional)
```json
"timeBetweenPages": 5
```

- Minimum: 2 seconds
- Maximum: 30 seconds
- Recommended: 5-6 seconds
- Higher = safer, lower = faster

#### proxyConfiguration (Optional)
```json
"proxyConfiguration": {
  "useApifyProxy": true
}
```

- Recommended for reliability
- Included in free tier
- Prevents IP blocking

### Full Input Example

```json
{
  "url": "https://app.apollo.io/#/people?page=1",
  "numberOfPages": 20,
  "timeBetweenPages": 6,
  "proxyConfiguration": {
    "useApifyProxy": true,
    "apifyProxyGroups": ["RESIDENTIAL"]
  }
}
```

---

## 5️⃣ Testing

### Local Testing Workflow

#### 1. Quick Test (1 page)

```bash
npm run test:quick
```

**Purpose**: Verify URL works and data format is correct  
**Time**: ~10 seconds  
**Output**: JSON file with ~25 contacts

#### 2. Small Test (2-5 pages)

```bash
npm run test:full
```

**Purpose**: Test pagination and delays  
**Time**: ~30-60 seconds  
**Output**: JSON file with ~50-125 contacts

#### 3. Full Test (10+ pages)

```bash
node test-local.js --pages 10 --delay 5
```

**Purpose**: Production-like test  
**Time**: ~1-2 minutes  
**Output**: JSON file with ~250 contacts

### Validation Checklist

After each test, verify:

- [ ] All contacts have `fullName`
- [ ] Phone numbers are formatted correctly
- [ ] Emails look valid (if present)
- [ ] No weird characters in names
- [ ] Company names are clean
- [ ] Job titles are readable
- [ ] No duplicate contacts
- [ ] JSON file saved successfully

---

## 6️⃣ Scheduling Automated Runs

### Via Apify Console

#### Step 1: Create Schedule

1. Go to your Actor in Apify Console
2. Click **"Schedules"** tab
3. Click **"Create new"**

#### Step 2: Configure Schedule

```
Name: Daily Apollo Scrape
Cron expression: 0 9 * * *  (9 AM daily)
Timezone: Your timezone

Input:
{
  "url": "https://app.apollo.io/#/people?page=1",
  "numberOfPages": 20,
  "timeBetweenPages": 5
}
```

#### Step 3: Enable

- Toggle **"Enabled"** to ON
- Click **"Save"**

### Schedule Examples

```bash
# Every day at 9 AM
0 9 * * *

# Every Monday at 10 AM
0 10 * * 1

# Every hour
0 * * * *

# Every 6 hours
0 */6 * * *

# First day of month at midnight
0 0 1 * *
```

### Via API

```javascript
const { ApifyClient } = require('apify-client');
const client = new ApifyClient({ token: 'YOUR_TOKEN' });

await client.schedules().create({
  name: 'Daily Apollo Scrape',
  isEnabled: true,
  cronExpression: '0 9 * * *',
  timezone: 'America/New_York',
  actions: [{
    type: 'RUN_ACTOR',
    actorId: 'YOUR_ACTOR_ID',
    input: {
      url: 'https://app.apollo.io/#/people?page=1',
      numberOfPages: 20,
      timeBetweenPages: 5
    }
  }]
});
```

---

## 7️⃣ Troubleshooting

### Common Issues & Solutions

#### Issue: "No table found on the page"

**Symptoms**: Actor completes but returns 0 contacts

**Causes**:
- Not logged into Apollo.io
- Wrong URL format
- Apollo.io page structure changed

**Solutions**:
1. Verify the URL works in your browser
2. Make sure you're logged into Apollo.io
3. Check URL starts with `https://app.apollo.io/`
4. Try a different list URL

---

#### Issue: Actor build fails

**Symptoms**: Build error in Apify Console

**Causes**:
- Missing files in repository
- Syntax errors in code
- Wrong Node.js version

**Solutions**:
1. Check all files are committed to Git
2. Verify `package.json` exists
3. Make sure `Dockerfile` is present
4. Check Apify build logs for details

```bash
# Verify files locally
git status
git add .
git commit -m "Fix missing files"
git push
```

---

#### Issue: Timeout errors

**Symptoms**: "Navigation timeout" or "Waiting for selector timeout"

**Causes**:
- Slow network connection
- Apollo.io is slow to respond
- Page requires more time to load

**Solutions**:

1. **Increase timeout in main.js**:
```javascript
await page.goto(pageUrl, { 
    waitUntil: 'networkidle',
    timeout: 120000  // Changed from 60000 to 120000
});
```

2. **Increase selector timeout**:
```javascript
await page.waitForSelector('table', { 
    timeout: 60000  // Changed from 30000
});
```

3. **Add more wait time**:
```javascript
await page.waitForTimeout(5000);  // Wait 5 seconds
```

---

#### Issue: "No data scraped" / Empty dataset

**Symptoms**: Run completes successfully but dataset is empty

**Causes**:
- Authentication required
- Credits exhausted on Apollo.io
- Page structure different than expected

**Solutions**:
1. Check Apollo.io account status
2. Verify you can see contacts manually
3. Try a different list
4. Check if you have credits available
5. Increase delays: `"timeBetweenPages": 10`

---

#### Issue: Missing emails or phone numbers

**Symptoms**: Contacts have names but no emails/phones

**This is NORMAL!**

**Reasons**:
- Apollo.io requires credits to reveal contact info
- Some contacts don't have public emails/phones
- Privacy settings prevent data sharing

**What to do**:
- Check your Apollo.io credits
- Upgrade your Apollo.io plan
- Accept that some data may be incomplete

---

#### Issue: Rate limiting / IP blocked

**Symptoms**: 
- Requests fail after a few pages
- "Too many requests" error
- Slow response times

**Solutions**:
1. Increase delay between pages:
```json
{
  "timeBetweenPages": 10
}
```

2. Enable Apify proxy:
```json
{
  "proxyConfiguration": {
    "useApifyProxy": true
  }
}
```

3. Run during off-peak hours
4. Split into smaller runs

---

#### Issue: Out of memory

**Symptoms**: "JavaScript heap out of memory"

**Solutions**:

1. **Reduce pages per run**:
```json
{
  "numberOfPages": 50  // Instead of 100
}
```

2. **Increase memory in Apify** (Console → Run options):
```
Memory: 512 MB → 1024 MB
```

3. **Process in batches**:
- Run 1: Pages 1-50
- Run 2: Pages 51-100

---

### Getting Help

If you're still stuck:

1. **Check documentation**:
   - README.md
   - USAGE.md
   - PROJECT_SUMMARY.md

2. **Search GitHub Issues**:
   - Someone may have had the same problem
   - Check closed issues too

3. **Create an Issue**:
   - Include error logs
   - Share your input configuration
   - Describe what you've tried

4. **Apify Support**:
   - [Apify Discord](https://discord.com/invite/jyEM2PRvMU)
   - [Community Forum](https://community.apify.com)
   - support@apify.com

---

## 🎓 Next Steps

Once setup is complete:

1. ✅ **Schedule regular runs** - Automate your data collection
2. ✅ **Set up webhooks** - Get notified when scraping completes
3. ✅ **Integrate with tools** - Connect to Zapier, Make.com, or your CRM
4. ✅ **Customize the code** - Add your own features
5. ✅ **Share feedback** - Help us improve!

---

## 📚 Additional Resources

- [Apify Documentation](https://docs.apify.com)
- [Playwright Documentation](https://playwright.dev)
- [Apollo.io Help Center](https://help.apollo.io)
- [Cron Expression Guide](https://crontab.guru)

---

**You're all set! Happy scraping! 🚀**

Need quick help? Check [QUICK_START.md](QUICK_START.md) for the 5-minute version.



