# ⚡ Quick Start Guide - Apollo.io Data Scraper

Get started in just 5 minutes! 🚀

## 🎯 What You'll Need

- ✅ Apify account (free - [sign up here](https://apify.com))
- ✅ Apollo.io account with access to lists
- ✅ 5 minutes of your time

## 🚀 Option 1: Deploy to Apify (Fastest - No Coding Required)

### Step 1: Get the Code (30 seconds)

1. Click the **Fork** button on this GitHub repository
2. Or download as ZIP and upload to your GitHub account

### Step 2: Create Actor on Apify (2 minutes)

1. Go to [Apify Console](https://console.apify.com)
2. Click **Actors** → **Create new**
3. Select **From Git repository**
4. Enter your repository URL
5. Click **Create**

### Step 3: Build & Run (2 minutes)

1. Click **Build** and wait ~2 minutes
2. Once built, click **Start**
3. Enter your input:
   ```json
   {
     "url": "https://app.apollo.io/#/people?page=1",
     "numberOfPages": 2,
     "timeBetweenPages": 5
   }
   ```
4. Click **Start**

### Step 4: Get Your Data (30 seconds)

1. Wait for the run to complete
2. Click **Dataset** tab
3. Click **Export** → Choose **CSV**
4. Download your contacts! 🎉

**Total time: ~5 minutes**

---

## 🖥️ Option 2: Run Locally (For Developers)

### Step 1: Clone & Install (1 minute)

```bash
git clone https://github.com/YOUR_USERNAME/apollo-data-scraper.git
cd apollo-data-scraper
npm install
```

### Step 2: Test (1 minute)

```bash
# Quick test with 1 page
npm run test:quick

# Or full test with 5 pages
npm run test:full
```

### Step 3: Customize (Optional)

Edit `.actor/input.json`:

```json
{
  "url": "YOUR_APOLLO_LIST_URL",
  "numberOfPages": 10,
  "timeBetweenPages": 5
}
```

### Step 4: Run

```bash
npm start
```

**Total time: ~3 minutes**

---

## 📊 Getting Your Apollo.io URL

1. Log into Apollo.io
2. Go to **People** or **Saved Lists**
3. Apply filters (job title, location, etc.)
4. Copy the URL from your browser
5. Make sure it looks like: `https://app.apollo.io/#/people?...`

---

## 💡 Your First Scrape - Best Practices

### Start Small

```json
{
  "url": "https://app.apollo.io/#/people?page=1",
  "numberOfPages": 1,
  "timeBetweenPages": 5
}
```

**Why?** Test that everything works before scraping hundreds of pages.

### Then Scale Up

```json
{
  "url": "https://app.apollo.io/#/people?page=1",
  "numberOfPages": 20,
  "timeBetweenPages": 5
}
```

**Result**: ~500 contacts in 2-3 minutes

### Go Big

```json
{
  "url": "https://app.apollo.io/#/people?page=1",
  "numberOfPages": 100,
  "timeBetweenPages": 5
}
```

**Result**: ~2,500 contacts in 8-10 minutes

---

## 📥 Exporting Your Data

### CSV (for Excel/Google Sheets)

1. Click **Export** → **CSV**
2. Open in Excel or Google Sheets
3. Start reaching out to contacts!

### JSON (for Developers)

```javascript
// Get via API
const response = await fetch(
  'https://api.apify.com/v2/datasets/YOUR_DATASET_ID/items?format=json&token=YOUR_TOKEN'
);
const contacts = await response.json();
```

### Direct Integrations

- **Google Sheets** - Auto-sync to spreadsheet
- **Zapier** - Connect to CRM
- **Make.com** - Build automation workflows
- **Webhooks** - Send to your app

---

## 🆓 Free Tier Limits

Apify's free tier includes:

- ✅ **$5/month** in platform credits
- ✅ **50,000+ contacts/month** for FREE
- ✅ **Unlimited** dataset exports
- ✅ **7-day** data retention
- ✅ **Residential proxies** included

### Cost Examples

| Contacts | Cost | Free Tier? |
|----------|------|------------|
| 100 | $0.01 | ✅ Yes |
| 1,000 | $0.10 | ✅ Yes |
| 10,000 | $1.00 | ✅ Yes |
| 50,000 | $5.00 | ✅ Yes |

---

## 🔥 Common Use Cases

### 1. Lead Generation

Scrape potential customers by:
- Job title (e.g., "Marketing Manager")
- Industry (e.g., "SaaS")
- Location (e.g., "San Francisco")
- Company size (e.g., "50-200 employees")

### 2. Sales Prospecting

Build targeted lists for:
- Cold outreach campaigns
- Account-based marketing
- Territory planning
- Competitive intelligence

### 3. Market Research

Analyze:
- Company distributions
- Title hierarchies
- Contact availability
- Market segments

### 4. CRM Enrichment

- Import contacts to your CRM
- Enrich existing records
- Find missing emails/phones
- Update outdated information

---

## ⚠️ Important Notes

### Authentication Required

You need to be logged into Apollo.io. For automated runs, you'll need to:

1. **Option A**: Use the scraper immediately after logging in
2. **Option B**: Add cookie authentication (see README.md)

### Rate Limiting

- Use **5+ seconds** between pages
- Don't run multiple scrapers simultaneously
- Respect Apollo.io's terms of service

### Data Quality

- Some contacts may not have emails/phones
- This depends on your Apollo.io plan
- Empty fields are normal and expected

---

## 🐛 Quick Troubleshooting

### "No table found"

**Fix**: Make sure you're logged into Apollo.io and the URL is correct.

### "No data scraped"

**Fix**: Check if the page requires authentication or increase delay.

### "Timeout error"

**Fix**: Your network might be slow. Increase timeout in code.

---

## 📞 Get Help

- 📖 **Full docs**: Read `README.md`
- 💬 **Questions**: Open a GitHub issue
- 🐛 **Bugs**: Report in Issues
- 💡 **Ideas**: Start a Discussion

---

## 🎉 What's Next?

1. ✅ **Schedule runs** - Automate daily/weekly
2. ✅ **Set up webhooks** - Get notified on completion
3. ✅ **Connect to CRM** - Auto-import contacts
4. ✅ **Build workflows** - Use Zapier/Make.com
5. ✅ **Share feedback** - Help us improve!

---

**You're all set! Happy scraping! 🚀**

Need more details? Check out:
- 📖 `README.md` - Full documentation
- 📊 `USAGE.md` - Advanced examples
- 🚀 `DEPLOYMENT.md` - Deployment guide
- 🤝 `CONTRIBUTING.md` - How to contribute



