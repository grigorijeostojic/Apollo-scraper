# 📖 Usage Guide - Apollo.io Data Scraper

## Quick Start Examples

### Example 1: Basic Scraping (5 pages)

```json
{
  "url": "https://app.apollo.io/#/people?page=1",
  "numberOfPages": 5,
  "timeBetweenPages": 5
}
```

**Expected Output**: ~125 contacts (25 per page)

### Example 2: Large Dataset (50 pages)

```json
{
  "url": "https://app.apollo.io/#/people?finderViewId=12345&page=1",
  "numberOfPages": 50,
  "timeBetweenPages": 6
}
```

**Expected Output**: ~1,250 contacts
**Runtime**: ~5-7 minutes

### Example 3: Maximum Scrape (100 pages)

```json
{
  "url": "https://app.apollo.io/#/people?finderViewId=12345&page=1",
  "numberOfPages": 100,
  "timeBetweenPages": 5
}
```

**Expected Output**: ~2,500 contacts
**Runtime**: ~8-10 minutes

## 🎯 Finding Your Apollo.io List URL

### Method 1: From Saved Lists

1. Log into Apollo.io
2. Go to **Saved Lists** or **People**
3. Apply your filters (location, job title, company, etc.)
4. Click **Save** to create a list
5. Copy the URL from your browser's address bar
6. It should look like: `https://app.apollo.io/#/people?finderViewId=123456&page=1`

### Method 2: From Search

1. Go to Apollo.io **Search**
2. Apply filters (industry, location, seniority, etc.)
3. Wait for results to load
4. Copy the URL from the browser
5. Make sure it contains search parameters

### ✅ Valid URL Examples

```
✅ https://app.apollo.io/#/people?page=1
✅ https://app.apollo.io/#/people?finderViewId=12345&page=1
✅ https://app.apollo.io/#/people?prospectedByCurrentTeam[]=yes&page=1
```

### ❌ Invalid URL Examples

```
❌ https://www.apollo.io/ (homepage)
❌ https://app.apollo.io/#/settings (not a list)
❌ https://linkedin.com/... (different site)
```

## 📊 Understanding the Output

### Output Structure

Each scraped contact includes:

```json
{
  "firstName": "John",
  "lastName": "Doe",
  "fullName": "John Doe",
  "email": "john.doe@company.com",
  "phone": "+1 (555) 123-4567",
  "title": "Software Engineer",
  "company": "Tech Corp Inc"
}
```

### Field Descriptions

| Field | Description | Always Present? |
|-------|-------------|-----------------|
| `firstName` | First name of contact | ✅ Yes |
| `lastName` | Last name of contact | ⚠️ Usually |
| `fullName` | Complete name | ✅ Yes |
| `email` | Email address | ⚠️ If available |
| `phone` | Phone number (formatted) | ⚠️ If available |
| `title` | Job title | ⚠️ Usually |
| `company` | Company name | ⚠️ Usually |

### Missing Data

Some fields may be empty if:
- Apollo.io doesn't have the data
- You don't have credits to reveal the info
- The contact opted out

Example with missing data:
```json
{
  "firstName": "Jane",
  "lastName": "Smith",
  "fullName": "Jane Smith",
  "title": "Marketing Manager",
  "company": "StartupCo"
  // email and phone missing
}
```

## 💾 Exporting Data

### Via Apify Console

1. After the run completes, go to **Dataset** tab
2. Click **Export** button
3. Choose format:
   - **CSV** - Best for Excel/Google Sheets
   - **JSON** - Best for developers
   - **Excel** - Native .xlsx format
   - **HTML** - View in browser
   - **XML** - For legacy systems

### Via API

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: 'YOUR_TOKEN' });

// Get dataset items
const { items } = await client
  .dataset('YOUR_DATASET_ID')
  .listItems();

// Export as CSV
const csvUrl = `https://api.apify.com/v2/datasets/YOUR_DATASET_ID/items?format=csv`;

// Export as JSON
const jsonUrl = `https://api.apify.com/v2/datasets/YOUR_DATASET_ID/items?format=json`;
```

### Download to File

```bash
# CSV format
curl "https://api.apify.com/v2/datasets/YOUR_DATASET_ID/items?format=csv&token=YOUR_TOKEN" > contacts.csv

# JSON format
curl "https://api.apify.com/v2/datasets/YOUR_DATASET_ID/items?format=json&token=YOUR_TOKEN" > contacts.json

# Excel format
curl "https://api.apify.com/v2/datasets/YOUR_DATASET_ID/items?format=xlsx&token=YOUR_TOKEN" > contacts.xlsx
```

## 🔄 Integration Examples

### Google Sheets Integration

Use Apify's Google Sheets integration:

1. Go to your Actor run
2. Click **Integrations** → **Google Sheets**
3. Authorize your Google account
4. Select/create a spreadsheet
5. Map fields
6. Click **Export**

### Webhook Integration

Send data to your webhook after scraping:

```javascript
const run = await client.actor('YOUR_ACTOR_ID').call(input, {
  webhooks: [{
    eventTypes: ['ACTOR.RUN.SUCCEEDED'],
    requestUrl: 'https://your-webhook.com/apollo-data',
  }],
});
```

### Zapier Integration

1. Create a Zap in Zapier
2. Trigger: **Apify - New Dataset Item**
3. Configure with your Actor
4. Action: Send to CRM, Email, etc.

### Make.com (Integromat)

1. Create a scenario
2. Add **Apify** module
3. Choose **Watch Actor Run**
4. Connect to your CRM or database

## ⚙️ Advanced Configuration

### Custom Column Extraction

Modify `main.js` to extract additional columns:

```javascript
// In extractTableData function
switch(index) {
    case 7: // Location column
        rowData.location = text || '';
        break;
    case 8: // Industry column
        rowData.industry = text || '';
        break;
}
```

### Filter by Email Availability

```javascript
// Only save contacts with emails
if (rowData.fullName && rowData.email) {
    data.push(rowData);
}
```

### Custom Phone Formatting

```javascript
// Change phone format to international
const formatted = match.replace(
    /(\+\d{1})(\d{3})(\d{3})(\d{4})/, 
    '$1-$2-$3-$4'
);
```

## 📈 Best Practices

### 1. Start Small
```json
{
  "numberOfPages": 1,
  "timeBetweenPages": 5
}
```
Test with 1 page first to verify the URL and output format.

### 2. Optimal Delay
```json
{
  "timeBetweenPages": 5
}
```
5-6 seconds is ideal. Too fast = risk of blocking, too slow = wastes time.

### 3. Batch Processing
Instead of:
- 10 runs × 10 pages each

Do:
- 1 run × 100 pages

This saves on startup time and costs.

### 4. Use Schedules
Schedule daily/weekly scrapes instead of manual runs:
- Consistent data updates
- Automated workflow
- No manual intervention

## 🚨 Common Issues & Solutions

### Issue: "No table found on the page"

**Causes**:
- Not logged into Apollo.io
- Wrong URL format
- Page structure changed

**Solutions**:
1. Verify you're logged in
2. Check URL starts with `https://app.apollo.io/`
3. Try the URL manually in browser first

### Issue: "No data scraped"

**Causes**:
- Page requires authentication
- Credits exhausted on Apollo.io
- Rate limiting

**Solutions**:
1. Check Apollo.io account status
2. Increase `timeBetweenPages` to 10+
3. Use Apify proxy

### Issue: "Timeout error"

**Causes**:
- Slow network
- Apollo.io is slow
- Page requires more time to load

**Solutions**:
1. Increase timeout in `main.js`:
   ```javascript
   await page.goto(pageUrl, { 
       waitUntil: 'networkidle',
       timeout: 120000  // 2 minutes
   });
   ```

### Issue: "Missing emails/phones"

**Causes**:
- Apollo.io credits required
- Data not available
- Privacy settings

**Solutions**:
- This is expected behavior
- Check your Apollo.io credits
- Some contacts don't have public data

## 💰 Cost Examples

Based on Apify pricing (with $5 free monthly credit):

| Contacts | Pages | Est. Cost | Free Tier? |
|----------|-------|-----------|------------|
| 25 | 1 | $0.001 | ✅ Yes |
| 250 | 10 | $0.01 | ✅ Yes |
| 1,250 | 50 | $0.05 | ✅ Yes |
| 2,500 | 100 | $0.10 | ✅ Yes |
| 25,000 | 1,000 | $1.00 | ✅ Yes |
| 50,000 | 2,000 | $2.00 | ✅ Yes |
| 100,000 | 4,000 | $4.00 | ✅ Yes |

**Note**: Costs are estimates. Actual costs depend on:
- Run duration
- Memory usage
- Proxy usage
- Network speed

## 📞 Support

Need help? Check these resources:

1. **Documentation**: Read `README.md` and `DEPLOYMENT.md`
2. **GitHub Issues**: Report bugs or request features
3. **Apify Discord**: Get help from the community
4. **Email**: Contact support

---

**Happy scraping! 🎉**



