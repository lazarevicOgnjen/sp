from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

# Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.binary_location = "/usr/bin/google-chrome"

# Chrome driver setup
browser_driver = Service('/usr/bin/chromedriver')

# Start the browser
page_to_scrape = webdriver.Chrome(service=browser_driver, options=chrome_options)

try:
    # Step 1: Navigate to the page
    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/login/index.php")
    time.sleep(2)

    # Step 2: Log in via OpenID Connect
    page_to_scrape.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/section/div/div[2]/div/div/div/div/div/div[2]/div[3]/div/a").click()
    time.sleep(2)

    # Step 3: Input email
    mail = page_to_scrape.find_element(By.XPATH, '//*[@id="i0116"]')
    mail.send_keys(os.environ['MAIL'])  
    page_to_scrape.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
    time.sleep(2)   

    # Step 4: Input password
    password = page_to_scrape.find_element(By.XPATH, '//*[@id="i0118"]')
    password.send_keys(os.environ['PASSWORD'])  
    page_to_scrape.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
    time.sleep(2)

    # Step 5: Click "No" on "Stay signed in" prompt
    page_to_scrape.find_element(By.XPATH, '//*[@id="idBtn_Back"]').click()
    time.sleep(2)

    # Step 6: Navigate to the main page
    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/course/view.php?id=9")

    responseT1 = page_to_scrape.find_element(By.XPATH, '//*[@id="region-main"]')
    
    height = responseT1.size['height']
    width = responseT1.size['width']

    
    desired_width = max(width, 1200)  

    desired_height = min(height, 5000)

    page_to_scrape.set_window_size(desired_width, desired_height)  

   
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", responseT1)

    responseT1.screenshot('cs-sp1-nova-obavestenja.png')

finally:
    # Close the browser
    page_to_scrape.quit()
