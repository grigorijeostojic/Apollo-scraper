# 🚀 Apollo.io Data Scraper - Apify Actor

![Apollo Scraper](https://img.shields.io/badge/Apify-Actor-00D4AA?style=for-the-badge)
![Free Tier](https://img.shields.io/badge/Free-Tier%20Compatible-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)

A powerful and completely **FREE** Apify actor that scrapes contact data from Apollo.io lists. Extract names, emails, phone numbers, job titles, companies, and more with just a URL and page count!

**🎉 Converted from Chrome Extension to Cloud-Based Scraper!**

> 👋 **First time here?** Read **[START_HERE.md](START_HERE.md)** to choose your path!  
> ⚡ **Want to start now?** Jump to **[QUICK_START.md](QUICK_START.md)** for 5-minute setup!

## ✨ Features

- 🎯 **Simple Input**: Just provide an Apollo.io list URL and number of pages
- 💰 **Completely Free**: Designed to run on Apify's free tier
- 📊 **Rich Data**: Extract first name, last name, email, phone, title, company, and more
- ⚡ **Fast & Reliable**: Uses Playwright for stable scraping
- 🔄 **Rate Limiting**: Configurable delays between pages to avoid blocks
- 📥 **Multiple Export Formats**: Download as CSV, JSON, Excel, or HTML
- 🛡️ **Proxy Support**: Built-in Apify proxy support for better reliability

## 📖 Documentation Index

| Document | Description | For Who? |
|----------|-------------|----------|
| **[QUICK_START.md](QUICK_START.md)** | Get started in 5 minutes | Everyone |
| **[SETUP_GUIDE.md](SETUP_GUIDE.md)** | Complete setup instructions | Beginners |
| **[README.md](README.md)** | Main documentation (this file) | Everyone |
| **[USAGE.md](USAGE.md)** | Detailed usage & examples | Users |
| **[DEPLOYMENT.md](DEPLOYMENT.md)** | How to deploy to Apify | DevOps |
| **[CONTRIBUTING.md](CONTRIBUTING.md)** | How to contribute | Developers |
| **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** | Technical overview | Developers |
| **[CHANGELOG.md](CHANGELOG.md)** | Version history | Everyone |

## 🚀 How to Use

### Method 1: Using Apify Console (Easiest)

1. **Go to Apify**: Visit [apify.com](https://apify.com) and create a free account
2. **Create Actor**: Click on "Actors" → "Create new" → "Import from Git"
3. **Import This Repo**: Paste your repository URL
4. **Build & Run**: Click "Build" and then "Start"

### Method 2: Using Apify API

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({
    token: 'YOUR_APIFY_TOKEN',
});

const input = {
    url: "https://app.apollo.io/#/people?page=1",
    numberOfPages: 5,
    timeBetweenPages: 5
};

const run = await client.actor("YOUR_ACTOR_ID").call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();

console.log(items);
```

### Method 3: Run Locally

1. **Clone this repository**
   ```bash
   git clone <your-repo-url>
   cd apollo-data-scraper
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Set up input** - Create a file `input.json`:
   ```json
   {
     "url": "https://app.apollo.io/#/people?page=1",
     "numberOfPages": 5,
     "timeBetweenPages": 5
   }
   ```

4. **Run the actor**
   ```bash
   npm start
   ```

## 📋 Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `url` | String | ✅ Yes | - | Apollo.io list URL (must start with https://app.apollo.io/) |
| `numberOfPages` | Integer | ✅ Yes | 1 | Number of pages to scrape (1-100) |
| `timeBetweenPages` | Integer | ❌ No | 5 | Delay in seconds between pages (2-30) |
| `proxyConfiguration` | Object | ❌ No | `{useApifyProxy: true}` | Proxy settings for the scraper |

### Example Input

```json
{
  "url": "https://app.apollo.io/#/people?finderViewId=123456&page=1",
  "numberOfPages": 10,
  "timeBetweenPages": 5
}
```

## 📤 Output Format

The actor saves data to an Apify dataset. Each contact is saved as:

```json
{
  "firstName": "John",
  "lastName": "Doe",
  "fullName": "John Doe",
  "email": "john.doe@company.com",
  "phone": "+1 (555) 123-4567",
  "title": "Software Engineer",
  "company": "Tech Corp"
}
```

### Export Options

You can download the scraped data in multiple formats:
- **CSV** - Perfect for Excel and Google Sheets
- **JSON** - For developers and APIs
- **Excel** - Native XLSX format
- **HTML** - For viewing in browser
- **RSS** - For feed readers

## 💡 Tips for Best Results

1. **Start Small**: Test with 1-2 pages first to ensure your URL works
2. **Use Delays**: Keep `timeBetweenPages` at 5+ seconds to avoid rate limiting
3. **Check URL**: Make sure you're logged into Apollo.io and the URL is accessible
4. **Free Tier**: On Apify's free tier, you get $5/month credit which is enough for thousands of contacts
5. **Proxy Usage**: Enable Apify proxy for better reliability (included in free tier)

## 🆓 Running on Free Tier

This actor is optimized to run on **Apify's free tier**:

- **Free Credits**: $5/month (plenty for most use cases)
- **Memory**: Uses minimal memory (256 MB is enough)
- **Runtime**: Efficient scraping to minimize compute time
- **Storage**: Datasets are free on Apify

**Estimated Costs** (on free tier):
- Scraping 100 contacts ≈ $0.01-0.02
- Scraping 1,000 contacts ≈ $0.10-0.20
- With $5 free monthly credit, you can scrape **20,000-50,000 contacts/month for FREE!**

## ⚠️ Important Notes

### Authentication Required

**You need to be logged into Apollo.io** for this scraper to work. There are two ways to handle this:

#### Option 1: Manual Login (Recommended for Testing)
1. Run the actor in headed mode (set `headless: false` in main.js)
2. The browser will open - log into Apollo.io manually
3. The scraper will then access your lists

#### Option 2: Using Cookies (For Production)
1. Log into Apollo.io in your browser
2. Export your cookies using a browser extension
3. Add cookie support to the actor (modify main.js to inject cookies)

### Legal & Ethical Use

- ✅ Only scrape data you have permission to access
- ✅ Respect Apollo.io's Terms of Service
- ✅ Use reasonable delays between requests
- ✅ Don't overload their servers
- ⚠️ This tool is for personal/research use
- ❌ Don't use for spam or unauthorized purposes

## 🛠️ Development

### Project Structure

```
apollo-data-scraper/
├── actor.json           # Actor configuration
├── INPUT_SCHEMA.json    # Input field definitions
├── main.js             # Main scraping logic
├── package.json        # Dependencies
├── Dockerfile          # Docker configuration
└── README.md           # This file
```

### Key Dependencies

- **apify** (^3.1.0) - Apify SDK for actor development
- **playwright** (^1.40.0) - Browser automation

### Customization

You can modify `main.js` to:
- Extract additional fields from the table
- Change the data structure
- Add custom filters
- Implement different scraping strategies

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| "No table found" | Make sure you're logged into Apollo.io and the URL is valid |
| "No data scraped" | Check if the page requires authentication or has changed structure |
| Rate limiting | Increase `timeBetweenPages` to 10+ seconds |
| Timeout errors | Increase timeout values in main.js |
| Actor fails to build | Make sure all files are committed to your repository |

## 📚 Complete Documentation

- 📖 **[README.md](README.md)** (you are here) - Main documentation
- ⚡ **[QUICK_START.md](QUICK_START.md)** - Get started in 5 minutes
- 📊 **[USAGE.md](USAGE.md)** - Detailed usage examples and best practices
- 🚀 **[DEPLOYMENT.md](DEPLOYMENT.md)** - Complete deployment guide
- 🤝 **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute to this project
- 📝 **[CHANGELOG.md](CHANGELOG.md)** - Version history and updates
- 📋 **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Technical overview

## 📊 Comparison with Browser Extension

| Feature | Browser Extension | Apify Actor |
|---------|------------------|-------------|
| **Installation** | Chrome only | Works anywhere |
| **Automation** | Manual clicks | Fully automated |
| **Scheduling** | No | Yes (free schedules) |
| **API Access** | No | Yes |
| **Large Datasets** | Slow | Fast & parallel |
| **Cost** | Free | Free tier available |
| **Reliability** | Browser dependent | Cloud-based |

👉 **See [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) for detailed comparison**

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## 🙏 Acknowledgments

- Original Chrome extension by [Liveupx](https://www.youtube.com/@liveupx)
- Converted to Apify Actor for cloud automation
- Built with [Apify SDK](https://sdk.apify.com/) and [Playwright](https://playwright.dev/)

## 📬 Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/your-repo/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/your-repo/discussions)
- 📧 **Email**: your-email@example.com
- ☕ **Donate**: [Buy Me a Coffee](https://www.buymeacoffee.com/yourusername)

---

**Made with ❤️ for the data community**

*Disclaimer: This tool is for educational and research purposes. Always respect website terms of service and data privacy laws.*
