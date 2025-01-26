import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)






url = "https://www.sanjeevkapoor.com/Recipe"
queries = list(range(1, 21))

'''
for query in queries:
    response = requests.get(url=(f"https://www.sanjeevkapoor.com/Recipe?page={query}"))
    webpage = response.text

    soup = BeautifulSoup(webpage, "html.parser")
    recipe_links = soup.select(".col col-sm-4 col-md-4 col-lg-4 margin_y a")
    links = [link["href"] for link in recipe_links]'''


driver.get(url=("https://www.sanjeevkapoor.com/Recipe?page=2"))
driver.implicitly_wait(10)

event_times = driver.find_elements(By.CSS_SELECTOR, value=".col col-sm-4 col-md-4 col-lg-4 margin_y a")
print(event_times)


