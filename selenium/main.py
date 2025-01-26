from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome Open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

'''
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/Fujifilm-Instax-Instant-Camera-White/dp/B085283V4X/ref=sr_1_7?crid=1KDY0E9E7N2X1&keywords=polaroid&qid=1706635075&sprefix=polaroi%2Caps%2C260&sr=8-7&th=1")
driver.implicitly_wait(10)

price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole")
price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction")
print(f"The price is {price_whole.text}.{price_fraction}")

# button = driver.find_element((By.XPATH, '//*[@id="add-to-cart-button"])'))
# print(button.size)

# driver.close() # closes a single tab'''

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
driver.implicitly_wait(10)

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_titles = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}

for n in range(0, len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_titles[n].text
    }

print(events)



driver.quit() # closes entire browser