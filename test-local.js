/**
 * Local testing script for Apollo.io scraper
 * Run this to test the scraper locally before deploying to Apify
 * 
 * Usage:
 *   node test-local.js
 * 
 * Or with custom input:
 *   node test-local.js --url "https://app.apollo.io/#/people?page=1" --pages 2
 */

import { chromium } from 'playwright';

// Parse command line arguments
const args = process.argv.slice(2);
const getArg = (name, defaultValue) => {
    const index = args.indexOf(name);
    return index !== -1 && args[index + 1] ? args[index + 1] : defaultValue;
};

const input = {
    url: getArg('--url', 'https://app.apollo.io/#/people?page=1'),
    numberOfPages: parseInt(getArg('--pages', '2')),
    timeBetweenPages: parseInt(getArg('--delay', '5'))
};

console.log('🚀 Starting local test...');
console.log('Input:', JSON.stringify(input, null, 2));

// Extract table data function (same as in main.js)
async function extractTableData(page) {
    return await page.evaluate(() => {
        const table = document.querySelector('table');
        if (!table) {
            return [];
        }

        const rows = Array.from(table.querySelectorAll('tr'));
        const data = [];

        for (let i = 1; i < rows.length; i++) {
            const cells = Array.from(rows[i].querySelectorAll('td'));
            if (cells.length === 0) continue;

            const rowData = {};
            
            cells.forEach((cell, index) => {
                const clonedCell = cell.cloneNode(true);
                const elementsToRemove = clonedCell.querySelectorAll('svg, img, button, input[type="checkbox"]');
                elementsToRemove.forEach(el => el.remove());
                
                let text = clonedCell.textContent.trim();
                
                const phoneRegex = /\+\d{11}/g;
                const phoneMatches = text.match(phoneRegex);
                if (phoneMatches) {
                    phoneMatches.forEach(match => {
                        const formatted = match.replace(/(\+\d{1})(\d{3})(\d{3})(\d{4})/, '$1 ($2) $3-$4');
                        text = text.replace(match, formatted);
                    });
                }
                
                text = text.replace(/[^a-zA-Z0-9\s,.@()-]/g, '').replace(/Â/g, '').trim();
                
                switch(index) {
                    case 0: break;
                    case 1:
                        if (text && text !== 'Name') {
                            const names = text.split(' ');
                            rowData.firstName = names[0] || '';
                            rowData.lastName = names.slice(1).join(' ') || '';
                            rowData.fullName = text;
                        }
                        break;
                    case 2: rowData.title = text || ''; break;
                    case 3: rowData.company = text || ''; break;
                    case 4:
                        if (text && text !== 'No email' && text !== 'NA') {
                            rowData.email = text;
                        }
                        break;
                    case 5:
                        if (text && text !== 'Request Mobile Number' && text !== 'NA') {
                            rowData.phone = text;
                        }
                        break;
                    default:
                        rowData[`column_${index}`] = text;
                }
            });

            if (rowData.fullName || rowData.email) {
                data.push(rowData);
            }
        }

        return data;
    });
}

// Main test function
async function runTest() {
    const { url, numberOfPages, timeBetweenPages } = input;

    // Validate
    if (!url.includes('https://app.apollo.io/')) {
        throw new Error('URL must be a valid Apollo.io list URL');
    }

    const maxPages = Math.min(numberOfPages, 100);
    
    console.log(`\n📊 Configuration:`);
    console.log(`   URL: ${url}`);
    console.log(`   Pages: ${maxPages}`);
    console.log(`   Delay: ${timeBetweenPages}s\n`);

    // Launch browser (headless = false for testing, so you can see what's happening)
    console.log('🌐 Launching browser...');
    const browser = await chromium.launch({
        headless: false, // Set to true for headless mode
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    try {
        const context = await browser.newContext({
            userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        });

        const page = await context.newPage();

        // Generate page URLs
        const pageUrls = [];
        let baseUrl = url.replace(/&page=\d+/, '').replace(/\?page=\d+/, '');
        
        for (let i = 1; i <= maxPages; i++) {
            const separator = baseUrl.includes('?') ? '&' : '?';
            const pageUrl = `${baseUrl}${separator}page=${i}`;
            pageUrls.push(pageUrl);
        }

        let allData = [];

        // Scrape each page
        for (let i = 0; i < pageUrls.length; i++) {
            const pageUrl = pageUrls[i];
            console.log(`\n📄 Page ${i + 1}/${pageUrls.length}`);
            console.log(`   URL: ${pageUrl}`);

            try {
                await page.goto(pageUrl, { 
                    waitUntil: 'networkidle',
                    timeout: 60000 
                });

                console.log('   ⏳ Waiting for table...');
                await page.waitForSelector('table', { timeout: 30000 });
                await page.waitForTimeout(3000);

                const pageData = await extractTableData(page);
                
                console.log(`   ✅ Extracted ${pageData.length} contacts`);
                
                // Show first contact as sample
                if (pageData.length > 0) {
                    console.log('   Sample:', JSON.stringify(pageData[0], null, 2));
                }
                
                allData = allData.concat(pageData);

                if (i < pageUrls.length - 1) {
                    console.log(`   ⏸️  Waiting ${timeBetweenPages}s...`);
                    await page.waitForTimeout(timeBetweenPages * 1000);
                }

            } catch (error) {
                console.error(`   ❌ Error: ${error.message}`);
            }
        }

        // Results
        console.log(`\n\n🎉 Test Complete!`);
        console.log(`═══════════════════════════════════════`);
        console.log(`📊 Total contacts scraped: ${allData.length}`);
        console.log(`📄 Pages scraped: ${pageUrls.length}`);
        console.log(`⏱️  Average per page: ${(allData.length / pageUrls.length).toFixed(1)}`);
        
        // Data quality stats
        const withEmail = allData.filter(c => c.email).length;
        const withPhone = allData.filter(c => c.phone).length;
        console.log(`\n📧 Contacts with email: ${withEmail} (${(withEmail/allData.length*100).toFixed(1)}%)`);
        console.log(`📱 Contacts with phone: ${withPhone} (${(withPhone/allData.length*100).toFixed(1)}%)`);
        
        // Save to JSON file
        const fs = await import('fs');
        const filename = `test-results-${Date.now()}.json`;
        fs.writeFileSync(filename, JSON.stringify(allData, null, 2));
        console.log(`\n💾 Results saved to: ${filename}`);
        
        console.log(`\n✅ Test successful! Ready to deploy to Apify.`);

    } catch (error) {
        console.error('\n❌ Test failed:', error);
        throw error;
    } finally {
        await browser.close();
    }
}

// Run the test
runTest().catch(error => {
    console.error('Fatal error:', error);
    process.exit(1);
});



