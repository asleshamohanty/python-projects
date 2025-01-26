from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
cursor = driver.find_element(By.ID, "buyCursor")
cursor_price = driver.find_element(By.CSS_SELECTOR, "#buyCursor b moni")
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]
print(item_ids)

grandma = driver.find_element(By.ID, "buyGrandma")
while True:
    cookie.click()
    time.sleep(5)
