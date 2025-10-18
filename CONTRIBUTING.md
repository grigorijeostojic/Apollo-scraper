# 🤝 Contributing to Apollo.io Data Scraper

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## 🌟 Ways to Contribute

- 🐛 **Report bugs** - Found an issue? Let us know!
- 💡 **Suggest features** - Have an idea? We'd love to hear it!
- 📝 **Improve documentation** - Help others understand the project better
- 🔧 **Submit code** - Fix bugs or implement new features
- 🧪 **Write tests** - Help us maintain quality
- 📣 **Spread the word** - Star the repo, share with others

## 🚀 Getting Started

### Prerequisites

- Node.js 18+ installed
- npm or yarn
- Git
- Apify account (for testing on the platform)
- Apollo.io account (for testing scraping functionality)

### Local Development Setup

1. **Fork the repository**
   ```bash
   # Click "Fork" on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/apollo-data-scraper.git
   cd apollo-data-scraper
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Create a test input file**
   ```bash
   # Edit .actor/input.json with your test data
   {
     "url": "https://app.apollo.io/#/people?page=1",
     "numberOfPages": 2,
     "timeBetweenPages": 5
   }
   ```

4. **Run locally**
   ```bash
   # Test the scraper
   node test-local.js
   
   # Or run the actor
   npm start
   ```

## 📋 Development Workflow

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

Branch naming conventions:
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation changes
- `refactor/` - Code refactoring
- `test/` - Test additions/changes

### 2. Make Your Changes

- Write clean, readable code
- Follow the existing code style
- Add comments for complex logic
- Update documentation if needed

### 3. Test Your Changes

```bash
# Run local test
node test-local.js --url "YOUR_TEST_URL" --pages 2

# Test different scenarios
node test-local.js --pages 1 --delay 3
node test-local.js --pages 5 --delay 10
```

### 4. Commit Your Changes

```bash
git add .
git commit -m "Description of your changes"
```

Commit message format:
```
type: Brief description

Longer explanation if needed
- Bullet points for details
- More details

Fixes #issue_number (if applicable)
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:
```
feat: Add email validation before saving contacts

fix: Handle timeout errors gracefully
- Increased default timeout to 60s
- Added retry logic for failed pages
Fixes #123

docs: Update README with new examples
```

### 5. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then go to GitHub and create a Pull Request.

## 🎯 Coding Standards

### JavaScript Style Guide

```javascript
// ✅ Good
async function extractTableData(page) {
    const data = await page.evaluate(() => {
        // Implementation
    });
    return data;
}

// ❌ Avoid
async function extractTableData(page) 
{
  const data=await page.evaluate(()=>{
    // Implementation
  })
  return data
}
```

### Best Practices

1. **Use async/await** instead of callbacks
2. **Handle errors** with try/catch
3. **Log important steps** for debugging
4. **Validate inputs** before processing
5. **Comment complex logic**
6. **Keep functions small** and focused
7. **Use meaningful variable names**

### Example: Good Code

```javascript
async function scrapePage(page, url, pageNumber) {
    try {
        console.log(`Scraping page ${pageNumber}: ${url}`);
        
        // Navigate with timeout
        await page.goto(url, { 
            waitUntil: 'networkidle',
            timeout: 60000 
        });
        
        // Wait for content
        await page.waitForSelector('table', { timeout: 30000 });
        
        // Extract data
        const data = await extractTableData(page);
        console.log(`Extracted ${data.length} contacts`);
        
        return data;
        
    } catch (error) {
        console.error(`Error scraping page ${pageNumber}:`, error.message);
        throw error;
    }
}
```

## 🧪 Testing

### Manual Testing Checklist

Before submitting a PR, test:

- [ ] Scraping with 1 page works
- [ ] Scraping with multiple pages works
- [ ] Different time delays work
- [ ] Error handling works (invalid URL, timeout, etc.)
- [ ] Data is correctly formatted
- [ ] Phone numbers are properly formatted
- [ ] Empty fields are handled correctly
- [ ] Special characters are removed

### Test Scenarios

1. **Valid input**
   ```json
   {"url": "https://app.apollo.io/#/people?page=1", "numberOfPages": 2}
   ```

2. **Invalid URL**
   ```json
   {"url": "https://google.com", "numberOfPages": 1}
   ```

3. **Large dataset**
   ```json
   {"url": "https://app.apollo.io/#/people?page=1", "numberOfPages": 50}
   ```

4. **Edge cases**
   - Empty table
   - Slow loading page
   - Network interruption
   - Authentication required

## 📝 Documentation

When adding features, update:

1. **README.md** - Main documentation
2. **USAGE.md** - Usage examples
3. **DEPLOYMENT.md** - Deployment instructions (if applicable)
4. **CHANGELOG.md** - Add your changes
5. **Code comments** - Explain complex logic

## 🐛 Bug Reports

Good bug reports include:

1. **Title** - Clear, descriptive summary
2. **Description** - What happened vs what you expected
3. **Steps to reproduce** - How to recreate the issue
4. **Environment** - OS, Node version, Apify platform, etc.
5. **Screenshots/logs** - If applicable
6. **Input configuration** - What input caused the issue

### Bug Report Template

```markdown
## Bug Description
A clear description of what the bug is.

## To Reproduce
Steps to reproduce the behavior:
1. Use this input: `{"url": "...", "numberOfPages": 5}`
2. Run the actor
3. See error

## Expected Behavior
What you expected to happen.

## Actual Behavior
What actually happened.

## Environment
- Node.js version: 18.x
- Playwright version: 1.40.0
- Apify platform: Yes/No
- OS: Windows 10 / macOS / Linux

## Logs
```
Paste relevant logs here
```

## Screenshots
If applicable, add screenshots.

## Additional Context
Any other context about the problem.
```

## 💡 Feature Requests

When suggesting features:

1. **Problem** - Describe the problem you're trying to solve
2. **Solution** - Propose a solution
3. **Alternatives** - Any alternative solutions considered
4. **Use cases** - Real-world examples

### Feature Request Template

```markdown
## Problem
Describe the problem this feature would solve.

## Proposed Solution
How should this feature work?

## Alternatives Considered
What other solutions did you consider?

## Use Cases
- Use case 1
- Use case 2

## Additional Context
Any mockups, examples, or references.
```

## 🎨 Feature Development Guidelines

### Adding a New Feature

1. **Create an issue** first to discuss the feature
2. **Wait for approval** before starting work
3. **Create a branch** from `main`
4. **Implement the feature** following coding standards
5. **Test thoroughly** with various inputs
6. **Update documentation** 
7. **Submit a PR** with clear description

### Example: Adding Email Validation

```javascript
// 1. Add helper function
function isValidEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

// 2. Use in extraction logic
if (text && text !== 'No email' && text !== 'NA') {
    if (isValidEmail(text)) {
        rowData.email = text;
    } else {
        console.warn(`Invalid email format: ${text}`);
    }
}

// 3. Update INPUT_SCHEMA.json if needed
{
    "validateEmails": {
        "title": "Validate Emails",
        "type": "boolean",
        "description": "Only save contacts with valid email addresses",
        "default": false
    }
}

// 4. Update README.md with new feature
// 5. Add to CHANGELOG.md
```

## 🔍 Code Review Process

### For Contributors

- Respond to feedback promptly
- Be open to suggestions
- Make requested changes
- Keep the PR focused on one feature/fix

### For Reviewers

- Be respectful and constructive
- Explain why changes are needed
- Approve when ready
- Test the changes if possible

## 📦 Release Process

1. Update version in `package.json`
2. Update `CHANGELOG.md` with changes
3. Create a git tag: `git tag v1.1.0`
4. Push tag: `git push --tags`
5. Create GitHub release
6. Deploy to Apify

## 🏆 Recognition

Contributors will be:
- Added to CONTRIBUTORS.md
- Mentioned in release notes
- Thanked in the community

## ❓ Questions?

- 💬 Open a [GitHub Discussion](https://github.com/your-repo/discussions)
- 🐛 Create an [Issue](https://github.com/your-repo/issues)
- 📧 Email: your-email@example.com

## 📜 Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone.

### Our Standards

**Positive behavior:**
- Using welcoming language
- Being respectful
- Accepting constructive criticism
- Focusing on what's best for the community

**Unacceptable behavior:**
- Harassment or discriminatory language
- Trolling or insulting comments
- Publishing others' private information
- Other unprofessional conduct

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing! 🎉**

Your help makes this project better for everyone.



