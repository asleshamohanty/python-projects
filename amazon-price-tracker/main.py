import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "https://www.amazon.in/Fujifilm-Instax-Instant-Camera-White/dp/B085283V4X/ref=sr_1_7?crid=1KDY0E9E7N2X1&keywords=polaroid&qid=1706635075&sprefix=polaroi%2Caps%2C260&sr=8-7&th=1"
SET_PRICE = 6000
my_email = "@gmail.com"
password = ""

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=URL, headers=headers)
amazon_page = response.text
#print(amazon_page)

soup = BeautifulSoup(amazon_page, "lxml")
price = soup.find(name="span", class_="a-price-whole").getText().split(".")[0]
formatted_price = int(price.replace(",", ""))
title = soup.find(id="productTitle").get_text().strip()

message = f"{title} is now {formatted_price}!"

if formatted_price <= SET_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="asleshasocial@yahoo.com",
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8"))

