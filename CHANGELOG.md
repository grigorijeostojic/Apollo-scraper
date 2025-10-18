# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-10-09

### Added
- Initial release of Apollo.io Data Scraper for Apify
- Converted Chrome extension to cloud-based Apify actor
- Support for scraping multiple pages (up to 100)
- Configurable delays between pages
- Automatic phone number formatting
- Data extraction for:
  - First Name
  - Last Name
  - Full Name
  - Email
  - Phone Number
  - Job Title
  - Company Name
- Apify proxy support for better reliability
- Comprehensive error handling
- Dataset export in multiple formats (CSV, JSON, Excel, HTML)
- Free tier optimization
- Docker containerization
- Input validation
- Detailed logging and progress tracking

### Features from Original Extension
- Table data extraction from Apollo.io
- Special character cleaning
- Phone number formatting (+1 (555) 123-4567)
- Empty field handling ("No email", "NA", etc.)
- SVG/image/button removal from scraped data

### Documentation
- Comprehensive README with usage examples
- Deployment guide for Apify platform
- Usage guide with real-world examples
- Troubleshooting section
- Cost calculator
- Integration examples (API, Zapier, Make.com, Google Sheets)

### Developer Tools
- Local testing script (test-local.js)
- Example input configurations
- .gitignore and .dockerignore
- apify.json for CLI deployment

### Improvements Over Extension
- No browser dependency
- Runs in the cloud
- Fully automated (no manual clicks)
- Schedulable runs
- API access
- Webhook support
- Better error handling
- Parallel processing capability
- No installation required

## [Unreleased]

### Planned Features
- Cookie-based authentication
- Custom column mapping
- Data filtering options
- Duplicate detection
- CRM integration (Salesforce, HubSpot)
- Email validation
- Company enrichment
- Export to Google Sheets directly
- Slack/Discord notifications
- Retry logic for failed pages
- Resume capability for interrupted runs

---

## Version History

- **v1.0.0** (2024-10-09) - Initial release, feature-complete Apify actor
- **v0.1.0** (Original) - Chrome extension version by Liveupx



