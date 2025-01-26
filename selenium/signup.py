from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

fName = driver.find_element(By.NAME, "fName")
fName.send_keys("Aslesha")
fName.send_keys(Keys.ENTER)

lName = driver.find_element(By.NAME, "lName")
lName.send_keys("Mohanty")
lName.send_keys(Keys.ENTER)

email = driver.find_element(By.NAME, "email")
email.send_keys("xyz@gmail.com")
email.send_keys(Keys.ENTER)

submit = driver.find_element(By.CLASS_NAME, "btn btn-lg btn-primary btn-block")
submit.click()