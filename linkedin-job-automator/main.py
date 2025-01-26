from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

PHONE = 1234567890
EMAIL = "maildummy101108@gmail.com"
PWD = "npshsr@123"

def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3732528413&f_AL=true&f_E=2&f_WT=2&geoId=112376381&keywords=Python%20Developer&location=Bangalore%20Urban%2C%20Karnataka%2C%20India&origin=JOB_SEARCH_PAGE_JOB_FILTER")

time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

email_phone = driver.find_element(By.NAME, "session_key")
email_phone.send_keys(EMAIL, Keys.TAB)

password = driver.find_element(By.NAME, "session_password")
password.send_keys(PWD, Keys.TAB)
password.send_keys(Keys.ENTER)

# time.sleep(5)
# apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
# apply_button.click()
#
# time.sleep(5)
# phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
# if phone.text == "":
#     phone.send_keys(PHONE)
#
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
# submit_button.click()

time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for listing in all_listings:
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == " ":
            phone.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application
            print("Complex application, skipped.")
            continue
        else:
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
