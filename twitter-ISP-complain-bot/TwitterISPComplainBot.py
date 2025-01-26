from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_UP = 200
PROMISED_DOWN = 200
TWITTER_EMAIL = "samplemail"
TWITTER_USERNAME = "username"
TWITTER_PASSWORD = "password"


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Option to keep Chrome open


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        cookies_continue = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookies_continue.click()
        go = self.driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a")
        # go = self.driver.find_element(by=By.LINK_TEXT, value="Go")
        go.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
        self.up = self.driver.find_element(By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
        print(self.up, self.down)


    def tweet_provider(self):
        self.driver.get("https://twitter.com/home?lang=en")
        time.sleep(2)
        sign_in = self.driver.find_element(By.LINK_TEXT, "Sign in")
        sign_in.click()
        time.sleep(5)
        email = self.driver.find_element(By.NAME, "text")
        email.send_keys(TWITTER_USERNAME, Keys.ENTER)
        time.sleep(5)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(TWITTER_PASSWORD, Keys.ENTER)
        time.sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span")
        tweet = f"Hey Internet Provider! Why is my internet speed {self.down} down/{self.up} up when I pay for {PROMISED_DOWN} down/{PROMISED_UP} up?"
        tweet_compose.send_keys(tweet, Keys.ENTER)
        post_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span")
        post_button.click()
        # password = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')


twitterbot = InternetSpeedTwitterBot()
twitterbot.get_internet_speed()
if float(twitterbot.up) < PROMISED_UP or float(twitterbot.down) < PROMISED_DOWN:
    twitterbot.tweet_provider()


