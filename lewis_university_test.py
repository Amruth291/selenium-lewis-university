from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up WebDriver
driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)


def test_homepage_title():
    print("Opening Lewis University website...")
    driver.get("https://www.lewisu.edu/")
    time.sleep(5)  # Wait for page to load fully
    assert "Lewis University" in driver.title
    print("Homepage title test passed.")
    driver.save_screenshot("homepage_title.png")

# Run the test
try:
    test_homepage_title()
finally:
    driver.quit()

