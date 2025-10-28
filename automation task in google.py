from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Step 1: Setup Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)

# Step 2: Open Weather.com (safe website)
url = "https://weather.com/en-IN/weather/today/l/Chennai+Tamil+Nadu?canonicalCityId=2f44c028c19c99b2a7f57b2516f8918e678a4ac69c8137aebcf9f239f1583a2a"
driver.get(url)

# Step 3: Wait for the page to load
time.sleep(8)

# Step 4: Take screenshot
save_path = r"C:\Users\admin\Pictures\chennai_weather.png"
driver.save_screenshot(save_path)

print(f"✅ Screenshot saved successfully at: {save_path}")

# Step 5: Close browser
driver.quit()

#output
# ✅ Screenshot saved successfully at: C:\Users\admin\Pictures\chennai_weather.png
# PS C:\Users\admin\Pictures\pandas>
##c:\Users\admin\Pictures\chennai_weather.png
