# 🚀 Deployment Guide for Apollo.io Data Scraper

This guide will walk you through deploying your Apollo.io scraper to Apify's platform for **FREE**.

## 📋 Prerequisites

1. **Apify Account**: Sign up at [apify.com](https://apify.com) (free tier includes $5/month credit)
2. **Git Repository**: Your code should be in a Git repository (GitHub, GitLab, or Bitbucket)
3. **Apollo.io Account**: You'll need login credentials for Apollo.io

## 🎯 Method 1: Deploy via Apify Console (Recommended)

### Step 1: Push to Git

```bash
git init
git add .
git commit -m "Initial commit - Apollo.io scraper"
git remote add origin <your-git-url>
git push -u origin main
```

### Step 2: Create Actor on Apify

1. Log into [Apify Console](https://console.apify.com)
2. Click **Actors** in the left menu
3. Click **Create new** → **From Git repository**
4. Fill in the form:
   - **Git URL**: Your repository URL
   - **Name**: `apollo-data-scraper`
   - **Title**: `Apollo.io Data Scraper`
   - **Build tag**: `latest`

### Step 3: Build the Actor

1. Click **Build** button
2. Wait for the build to complete (usually 2-3 minutes)
3. You'll see a green checkmark when done

### Step 4: Test Run

1. Click **Start** button
2. Fill in the input:
   ```json
   {
     "url": "https://app.apollo.io/#/people?page=1",
     "numberOfPages": 2,
     "timeBetweenPages": 5
   }
   ```
3. Click **Start**
4. Monitor the run in the console

### Step 5: View Results

1. Once completed, click on the **Dataset** tab
2. Download as CSV, JSON, Excel, or HTML
3. Use the API or webhook to integrate with other tools

## 🎯 Method 2: Deploy via Apify CLI

### Step 1: Install Apify CLI

```bash
npm install -g apify-cli
```

### Step 2: Login to Apify

```bash
apify login
```

This will open a browser to authenticate.

### Step 3: Initialize Actor

```bash
# In your project directory
apify init
```

Select "Use existing files" when prompted.

### Step 4: Deploy

```bash
apify push
```

This will:
- Create a new actor on Apify
- Upload your code
- Build the Docker image
- Make it ready to run

### Step 5: Run from CLI

```bash
apify call
```

Or with custom input:

```bash
apify call --input '{
  "url": "https://app.apollo.io/#/people?page=1",
  "numberOfPages": 5,
  "timeBetweenPages": 5
}'
```

## 🎯 Method 3: Deploy via API

### Step 1: Get Your API Token

1. Go to [Apify Console](https://console.apify.com)
2. Click **Settings** → **Integrations**
3. Copy your **API token**

### Step 2: Create Actor via API

```javascript
const ApifyClient = require('apify-client');

const client = new ApifyClient({
    token: 'YOUR_API_TOKEN',
});

// Create actor
await client.actors().create({
    name: 'apollo-data-scraper',
    title: 'Apollo.io Data Scraper',
    description: 'Scrape contacts from Apollo.io',
    versions: [{
        versionNumber: '0.1',
        sourceType: 'GIT_REPO',
        gitRepoUrl: 'https://github.com/your-username/apollo-scraper',
    }],
});
```

### Step 3: Run the Actor

```javascript
const run = await client.actor('YOUR_ACTOR_ID').call({
    url: 'https://app.apollo.io/#/people?page=1',
    numberOfPages: 5,
    timeBetweenPages: 5,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

## 🔧 Configuration Options

### Memory Settings

For optimal free-tier usage:

```json
{
  "defaultRunOptions": {
    "build": "latest",
    "memoryMbytes": 512,
    "timeoutSecs": 3600
  }
}
```

### Proxy Configuration

Use Apify's residential proxies (included in free tier):

```json
{
  "proxyConfiguration": {
    "useApifyProxy": true,
    "apifyProxyGroups": ["RESIDENTIAL"]
  }
}
```

## 📅 Scheduling (Free Feature)

### Via Console

1. Go to your Actor
2. Click **Schedules** tab
3. Click **Create new**
4. Set schedule (e.g., "Daily at 9 AM")
5. Add input configuration

### Via API

```javascript
await client.schedules().create({
    name: 'Daily Apollo Scrape',
    isEnabled: true,
    cronExpression: '0 9 * * *', // Daily at 9 AM
    actions: [{
        type: 'RUN_ACTOR',
        actorId: 'YOUR_ACTOR_ID',
        input: {
            url: 'https://app.apollo.io/#/people?page=1',
            numberOfPages: 10,
            timeBetweenPages: 5,
        },
    }],
});
```

## 🔐 Authentication Setup

Apollo.io requires authentication. Here are your options:

### Option 1: Use Cookies (Recommended)

1. Log into Apollo.io in your browser
2. Open Developer Tools (F12)
3. Go to Application → Cookies
4. Copy all cookies for `apollo.io`
5. Add to your actor:

```javascript
// In main.js, before page.goto()
await context.addCookies([
    {
        name: 'cookie_name',
        value: 'cookie_value',
        domain: '.apollo.io',
        path: '/',
    },
    // ... more cookies
]);
```

### Option 2: Use API Key (If Available)

Some users have API access. Check Apollo.io docs for details.

### Option 3: Headful Login

For testing, you can use headed mode:

```javascript
const browser = await chromium.launch({
    headless: false, // Opens visible browser
});
```

## 💰 Cost Optimization

### Free Tier Limits
- **$5/month** in platform credits
- **1 parallel actor** run
- **7-day** data retention
- **Residential proxies** included

### Tips to Stay Free
1. **Batch scraping**: Scrape more pages per run
2. **Use schedules**: Run during off-peak hours
3. **Optimize memory**: Use 256-512 MB (sufficient for most cases)
4. **Clean data**: Only store what you need
5. **Export quickly**: Download data and delete old datasets

### Cost Calculator
- **Per run**: ~$0.0001-0.0005 (depends on pages)
- **100 contacts**: ~$0.01
- **1,000 contacts**: ~$0.10
- **10,000 contacts**: ~$1.00

With $5/month, you can scrape **50,000-100,000 contacts for FREE!**

## 🐛 Troubleshooting Deployment

### Build Fails

**Error**: `Cannot find module 'apify'`
**Solution**: Make sure `package.json` has all dependencies

**Error**: `Dockerfile not found`
**Solution**: Ensure `Dockerfile` is in the root directory

### Run Fails

**Error**: `Navigation timeout`
**Solution**: Increase timeout in main.js or check if URL is accessible

**Error**: `No table found`
**Solution**: You need to be authenticated to Apollo.io

**Error**: `Proxy error`
**Solution**: Enable Apify proxy in input configuration

### Memory Issues

**Error**: `Out of memory`
**Solution**: Reduce `numberOfPages` or increase memory allocation

## 📊 Monitoring & Alerts

### Email Notifications

Set up in Apify Console:
1. Go to **Settings** → **Notifications**
2. Enable email alerts for:
   - Run failures
   - Build failures
   - Dataset size limits

### Webhooks

```javascript
await client.webhooks().create({
    eventTypes: ['ACTOR.RUN.SUCCEEDED'],
    requestUrl: 'https://your-webhook-url.com',
    payloadTemplate: '{"message":"Scraping completed!"}',
});
```

## 🔄 Updating Your Actor

### Via Git (Automatic)

1. Make changes to your code
2. Commit and push:
   ```bash
   git add .
   git commit -m "Update scraping logic"
   git push
   ```
3. In Apify Console, click **Build** to rebuild

### Via CLI

```bash
apify push
```

### Versioning

Create versions for major changes:

```bash
apify push --version-number 1.0
apify push --version-number 1.1
```

## 📖 Next Steps

1. **Test thoroughly**: Run with different URLs and page counts
2. **Set up monitoring**: Enable email alerts
3. **Schedule runs**: Automate your data collection
4. **Integrate**: Connect to Google Sheets, Airtable, or your CRM
5. **Share**: Make your actor public to help others (optional)

## 🆘 Getting Help

- **Apify Docs**: [docs.apify.com](https://docs.apify.com)
- **Discord**: [Apify Discord Community](https://discord.com/invite/jyEM2PRvMU)
- **Forum**: [community.apify.com](https://community.apify.com)
- **Support**: support@apify.com

---

**Happy Scraping! 🎉**



