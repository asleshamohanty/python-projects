import requests
from datetime import *
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
VANTAGE_API_KEY = "GQBDC24JI3MVP34W"
NEWS_API = "73964898165b4a02bd5524d4790a9096"


account_sid = 'ACf212da148153b87f50920f9192ea0186'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : VANTAGE_API_KEY
}

now = datetime.now()
yesterday = str(now.date() - timedelta(days = 1))
day_before_yesterday = str(now.date() - timedelta(days = 2))
print(day_before_yesterday)

news_params = {
    "q": "Tesla",
    "name": COMPANY_NAME,
    "from": now.date() - timedelta(days = 5),
    "searchIn": "title",
    "to": now.date(),
    "language": "en",
    "sortBy": "popularity",
    "pageSize": 3,
    "apiKey": NEWS_API

}




## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get(url = "https://www.alphavantage.co/query", params = stock_params )
stock_data = stock_response.json()
print(stock_data)
