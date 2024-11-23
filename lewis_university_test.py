from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Disable detection
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Set up WebDriver using Service
service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

# Example test case to verify the setup works
try:
    print("Opening Lewis University website...")
    driver.get("https://www.lewisu.edu/")
    time.sleep(5)  # Wait for the page to load fully
    print("Checking title...")
    assert "Lewis University" in driver.title
    print("Homepage title test passed.")
    driver.save_screenshot("homepage_title.png")
finally:
    driver.quit()


