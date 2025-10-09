"""
Apollo.io Scraper - Apify Actor
Main entry point for the Apify Actor

This actor scrapes Apollo.io using a free account (no paid API required).
Works forever with free accounts - no credits needed!
"""

from apify import Actor
from src.scraper import ApolloScraper
from src.utils import log_message, is_valid_url
import json


async def main():
    """
    Main Apify Actor entrypoint.
    
    Gets input from Apify input, scrapes Apollo.io, and pushes results to dataset.
    """
    async with Actor:
        # Get input
        actor_input = await Actor.get_input() or {}
        
        # Validate required inputs
        apollo_email = actor_input.get('apolloEmail')
        apollo_password = actor_input.get('apolloPassword')
        start_urls = actor_input.get('startUrls', [])
        
        if not apollo_email or not apollo_password:
            await Actor.fail('Apollo.io email and password are required!')
            return
        
        if not start_urls:
            await Actor.fail('At least one start URL is required!')
            return
        
        # Get configuration
        max_pages = actor_input.get('maxPages', 10)
        enrich_profiles = actor_input.get('enrichProfiles', True)
        min_delay = actor_input.get('minDelay', 3)
        max_delay = actor_input.get('maxDelay', 7)
        proxy_config = actor_input.get('proxyConfiguration')
        
        log_message(f"Starting Apollo scraper with {len(start_urls)} URLs")
        log_message(f"Max pages per URL: {max_pages}, Enrich profiles: {enrich_profiles}")
        
        # Get proxy URL if configured
        proxy_url = None
        if proxy_config:
            try:
                from apify import ProxyConfiguration
                # Create proxy configuration
                if isinstance(proxy_config, dict) and proxy_config.get('useApifyProxy'):
                    proxy_configuration = ProxyConfiguration()
                else:
                    proxy_configuration = ProxyConfiguration(**proxy_config) if isinstance(proxy_config, dict) else ProxyConfiguration()
                proxy_url = await proxy_configuration.new_url()
                log_message(f"Using proxy: {proxy_url[:50]}...")
            except Exception as e:
                log_message(f"Proxy setup failed, continuing without proxy: {e}", 'WARNING')
                proxy_url = None
        
        # Initialize scraper
        scraper = None
        total_results = 0
        
        try:
            # Create scraper instance
            scraper = ApolloScraper(
                headless=True,  # Always headless on Apify
                use_proxy=proxy_url is not None,
                proxy_url=proxy_url
            )
            
            # Setup browser
            scraper.setup_driver()
            
            # Login to Apollo
            log_message("Logging in to Apollo.io...")
            
            # Try to load saved cookies from key-value store
            cookies_loaded = False
            try:
                kvs = await Actor.open_key_value_store()
                cookies_json = await kvs.get_value('apollo_cookies')
                if cookies_json:
                    log_message("Found saved cookies, attempting to use them...")
                    scraper.driver.get('https://app.apollo.io')
                    for cookie in cookies_json:
                        if 'expiry' in cookie:
                            del cookie['expiry']
                        try:
                            scraper.driver.add_cookie(cookie)
                        except:
                            pass
                    scraper.driver.refresh()
                    if scraper._is_logged_in():
                        log_message("Successfully logged in using saved cookies!")
                        cookies_loaded = True
                        scraper.logged_in = True
            except Exception as e:
                log_message(f"Could not load saved cookies: {e}", 'WARNING')
            
            # If cookies didn't work, do regular login
            if not cookies_loaded:
                login_success = scraper.login(
                    email=apollo_email,
                    password=apollo_password,
                    use_saved_cookies=False
                )
                
                if not login_success:
                    await Actor.fail('Login to Apollo.io failed!')
                    return
                
                # Save cookies to key-value store for future runs
                try:
                    kvs = await Actor.open_key_value_store()
                    cookies = scraper.driver.get_cookies()
                    await kvs.set_value('apollo_cookies', cookies)
                    log_message("Saved cookies for future runs")
                except Exception as e:
                    log_message(f"Could not save cookies: {e}", 'WARNING')
            
            # Process each URL
            for idx, url_obj in enumerate(start_urls):
                url = url_obj.get('url') if isinstance(url_obj, dict) else url_obj
                
                if not is_valid_url(url):
                    log_message(f"Skipping invalid URL: {url}", 'WARNING')
                    continue
                
                log_message(f"Processing URL {idx + 1}/{len(start_urls)}: {url}")
                
                try:
                    # Scrape the URL
                    results = scraper.scrape_url(
                        url=url,
                        follow_links=enrich_profiles,
                        max_pages=max_pages,
                        min_delay=min_delay,
                        max_delay=max_delay
                    )
                    
                    log_message(f"Scraped {len(results)} results from {url}", 'SUCCESS')
                    
                    # Push results to Apify dataset
                    if results:
                        await Actor.push_data(results)
                        total_results += len(results)
                    
                except Exception as e:
                    log_message(f"Error scraping {url}: {str(e)}", 'ERROR')
                    continue
            
            log_message(f"Scraping complete! Total results: {total_results}", 'SUCCESS')
            
        except Exception as e:
            log_message(f"Fatal error: {str(e)}", 'ERROR')
            await Actor.fail(str(e))
        
        finally:
            # Cleanup
            if scraper:
                scraper.close()
            
            log_message("Actor finished")


# Run the actor
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())


