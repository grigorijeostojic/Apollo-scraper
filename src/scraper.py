"""
Core scraping logic for Apollo.io
Handles browser automation, login, navigation, and data extraction.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import getpass
from typing import List, Dict, Optional, Any
from tqdm import tqdm

from src.config import Config
from src.utils import random_delay, retry_on_failure, log_message, is_valid_url
from src.parser import (
    parse_search_results, parse_contact_profile,
    parse_company_profile, detect_page_type
)


class ApolloScraper:
    """Main scraper class for Apollo.io"""
    
    def __init__(self, headless: bool = True, use_proxy: bool = False, proxy_url: str = None):
        """
        Initialize the Apollo scraper.
        
        Args:
            headless: Run browser in headless mode
            use_proxy: Use proxy settings
            proxy_url: Proxy URL to use
        """
        self.driver = None
        self.headless = headless
        self.use_proxy = use_proxy
        self.proxy_url = proxy_url
        self.logged_in = False
        
    def setup_driver(self):
        """Setup and configure the Selenium WebDriver"""
        log_message("Setting up Chrome WebDriver...", 'INFO')
        
        chrome_options = Options()
        
        # Headless mode
        if self.headless:
            chrome_options.add_argument('--headless=new')
            log_message("Running in headless mode", 'INFO')
        
        # Anti-detection measures
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # Set random user agent
        user_agent = Config.get_random_user_agent()
        chrome_options.add_argument(f'user-agent={user_agent}')
        log_message(f"Using user agent: {user_agent[:50]}...", 'DEBUG')
        
        # Additional stealth options
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--start-maximized')
        
        # Proxy configuration
        if self.use_proxy and self.proxy_url:
            chrome_options.add_argument(f'--proxy-server={self.proxy_url}')
            log_message(f"Using proxy: {self.proxy_url[:50]}...", 'INFO')
        
        # Disable images for faster loading (optional)
        # chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        
        # Setup driver with automatic driver management
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Set page load timeout
        self.driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
        
        # Remove webdriver flag
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        log_message("WebDriver setup complete", 'SUCCESS')
    
    @retry_on_failure(max_retries=3)
    def login(self, email: str = None, password: str = None, use_saved_cookies: bool = True):
        """
        Login to Apollo.io account.
        
        Args:
            email: Apollo email (uses Config or prompts if not provided)
            password: Apollo password (uses Config or prompts if not provided)
            use_saved_cookies: Try to use saved cookies first
        
        Returns:
            True if login successful
        """
        if not self.driver:
            self.setup_driver()
        
        # Try to use saved cookies first
        if use_saved_cookies:
            log_message("Attempting to use saved session cookies...", 'INFO')
            self.driver.get(Config.APOLLO_BASE_URL)
            random_delay(2, 4)
            
            if load_cookies(self.driver):
                self.driver.refresh()
                random_delay(3, 5)
                
                # Check if we're logged in
                if self._is_logged_in():
                    log_message("Successfully logged in using saved cookies!", 'SUCCESS')
                    self.logged_in = True
                    return True
                else:
                    log_message("Saved cookies invalid, proceeding with login...", 'WARNING')
        
        # Get credentials
        email = email or Config.APOLLO_EMAIL
        password = password or Config.APOLLO_PASSWORD
        
        if not email:
            email = input("Enter your Apollo.io email: ")
        if not password:
            password = getpass.getpass("Enter your Apollo.io password: ")
        
        log_message(f"Logging in as {email}...", 'INFO')
        
        # Navigate to login page
        self.driver.get(Config.APOLLO_LOGIN_URL)
        random_delay(3, 5)
        
        try:
            # Wait for login form to load
            email_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='email'], input[type='email'], input[placeholder*='email' i]"))
            )
            
            # Enter email
            email_field.clear()
            email_field.send_keys(email)
            random_delay(1, 2)
            
            # Enter password
            password_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='password'], input[type='password']")
            password_field.clear()
            password_field.send_keys(password)
            random_delay(1, 2)
            
            # Click login button
            login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'], button:contains('Sign in'), button:contains('Log in')")
            login_button.click()
            
            log_message("Login form submitted, waiting for response...", 'INFO')
            random_delay(5, 8)
            
            # Check for CAPTCHA
            if self._check_for_captcha():
                log_message("CAPTCHA detected! Please solve it manually in the browser window.", 'WARNING')
                input("Press Enter after you've solved the CAPTCHA...")
                random_delay(2, 4)
            
            # Verify login success
            if self._is_logged_in():
                log_message("Login successful!", 'SUCCESS')
                self.logged_in = True
                
                # Save cookies for future use
                save_cookies(self.driver)
                
                return True
            else:
                # Check for error messages
                error_elem = self.driver.find_elements(By.CSS_SELECTOR, ".error, .alert, [class*='error']")
                if error_elem:
                    error_text = error_elem[0].text
                    log_message(f"Login failed: {error_text}", 'ERROR')
                else:
                    log_message("Login failed: Unknown error", 'ERROR')
                return False
                
        except TimeoutException:
            log_message("Login form not found - page structure may have changed", 'ERROR')
            return False
        except Exception as e:
            log_message(f"Login error: {str(e)}", 'ERROR')
            return False
    
    def _is_logged_in(self) -> bool:
        """Check if currently logged into Apollo"""
        try:
            # Check for elements that only appear when logged in
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='user'], [class*='profile'], [data-cy*='user']"))
            )
            return True
        except:
            # Check URL
            current_url = self.driver.current_url
            return 'login' not in current_url.lower() and 'app.apollo.io' in current_url
    
    def _check_for_captcha(self) -> bool:
        """Check if CAPTCHA is present on page"""
        captcha_indicators = [
            "recaptcha", "captcha", "hcaptcha", "challenge"
        ]
        page_source = self.driver.page_source.lower()
        return any(indicator in page_source for indicator in captcha_indicators)
    
    def scrape_url(self, url: str, follow_links: bool = True, max_pages: int = None, min_delay: int = 3, max_delay: int = 7) -> List[Dict[str, Any]]:
        """
        Scrape data from a given Apollo.io URL.
        
        Args:
            url: Apollo.io URL to scrape
            follow_links: Follow links to detail pages for enrichment
            max_pages: Maximum number of pages to scrape (for search results)
        
        Returns:
            List of extracted data dictionaries
        """
        if not is_valid_url(url):
            log_message(f"Invalid Apollo.io URL: {url}", 'ERROR')
            return []
        
        if not self.logged_in:
            log_message("Not logged in! Please login first.", 'ERROR')
            return []
        
        log_message(f"Navigating to: {url}", 'INFO')
        self.driver.get(url)
        random_delay(min_delay, max_delay)
        
        # Detect page type
        page_html = self.driver.page_source
        page_type = detect_page_type(page_html)
        log_message(f"Detected page type: {page_type}", 'INFO')
        
        if page_type == 'search':
            return self._scrape_search_results(follow_links, max_pages, min_delay, max_delay)
        elif page_type == 'contact_profile':
            return [self._scrape_contact_profile()]
        elif page_type == 'company_profile':
            return [self._scrape_company_profile()]
        else:
            log_message("Unknown page type, attempting generic extraction...", 'WARNING')
            return [self._scrape_generic_page()]
    
    def _scrape_search_results(self, follow_links: bool = True, max_pages: int = None, min_delay: int = 3, max_delay: int = 7) -> List[Dict[str, Any]]:
        """
        Scrape search results page with pagination.
        
        Args:
            follow_links: Follow links to enrich contact data
            max_pages: Maximum pages to scrape
        
        Returns:
            List of all scraped results
        """
        all_results = []
        page_num = 1
        max_pages = max_pages or Config.MAX_PAGES
        
        log_message("Scraping search results...", 'INFO')
        
        while page_num <= max_pages:
            log_message(f"Scraping page {page_num}...", 'INFO')
            
            # Wait for results to load
            random_delay(min_delay, max_delay)
            
            # Get current page HTML
            page_html = self.driver.page_source
            
            # Parse results from current page
            results = parse_search_results(page_html)
            
            if not results:
                log_message("No results found on this page, stopping pagination.", 'WARNING')
                break
            
            log_message(f"Found {len(results)} results on page {page_num}", 'SUCCESS')
            
            # Enrich results by visiting detail pages
            if follow_links:
                results = self._enrich_results(results)
            
            all_results.extend(results)
            
            # Try to go to next page
            if not self._go_to_next_page():
                log_message("No more pages available", 'INFO')
                break
            
            page_num += 1
            random_delay(min_delay, max_delay)
        
        log_message(f"Total results scraped: {len(all_results)}", 'SUCCESS')
        return all_results
    
    def _enrich_results(self, results: List[Dict]) -> List[Dict]:
        """
        Enrich results by following links to detail pages.
        
        Args:
            results: List of basic result dictionaries
        
        Returns:
            Enriched results
        """
        enriched = []
        
        log_message(f"Enriching {len(results)} results...", 'INFO')
        
        for result in results:
            profile_url = result.get('profile_url')
            
            if profile_url:
                try:
                    # Visit profile page
                    self.driver.get(profile_url)
                    random_delay(2, 4)
                    
                    # Parse detailed profile
                    detailed_data = self._scrape_contact_profile()
                    
                    # Merge with basic data
                    result.update(detailed_data)
                    
                    # Go back
                    self.driver.back()
                    random_delay(2, 3)
                    
                except Exception as e:
                    log_message(f"Failed to enrich contact: {str(e)}", 'WARNING')
            
            enriched.append(result)
        
        return enriched
    
    def _go_to_next_page(self) -> bool:
        """
        Navigate to next page in search results.
        
        Returns:
            True if successfully navigated to next page, False otherwise
        """
        try:
            # Try different selectors for next button
            next_button_selectors = [
                "button[aria-label='Next page']",
                "button:contains('Next')",
                "a[aria-label='Next']",
                ".pagination button:last-child",
                "[class*='next']:not([disabled])"
            ]
            
            for selector in next_button_selectors:
                try:
                    next_button = self.driver.find_element(By.CSS_SELECTOR, selector)
                    if next_button.is_enabled() and next_button.is_displayed():
                        next_button.click()
                        log_message("Clicked next page button", 'DEBUG')
                        return True
                except:
                    continue
            
            # Try infinite scroll
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            random_delay(2, 3)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            
            if new_height > last_height:
                log_message("Infinite scroll triggered", 'DEBUG')
                return True
            
            return False
            
        except Exception as e:
            log_message(f"Could not navigate to next page: {str(e)}", 'DEBUG')
            return False
    
    def _scrape_contact_profile(self) -> Dict[str, Any]:
        """Scrape current page as contact profile"""
        page_html = self.driver.page_source
        return parse_contact_profile(page_html)
    
    def _scrape_company_profile(self) -> Dict[str, Any]:
        """Scrape current page as company profile"""
        page_html = self.driver.page_source
        return parse_company_profile(page_html)
    
    def _scrape_generic_page(self) -> Dict[str, Any]:
        """Generic scraping for unknown page types"""
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        
        return {
            'type': 'generic',
            'url': self.driver.current_url,
            'title': self.driver.title,
            'text_content': soup.get_text()[:1000],  # First 1000 chars
            'scraped_at': time.strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def close(self):
        """Close the browser and cleanup"""
        if self.driver:
            log_message("Closing browser...", 'INFO')
            self.driver.quit()
            log_message("Browser closed", 'SUCCESS')
    
    def __enter__(self):
        """Context manager entry"""
        self.setup_driver()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.close()

