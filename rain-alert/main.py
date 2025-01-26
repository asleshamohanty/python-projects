import requests

api_key = "f323016d785cef92d65e359860be790b"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "AC259794b9dd687d76324824dfcfb2a92e"
auth_token = "8624e6a6979df0b4dc3602a727e3aaf9"

weather_params = {
    "lat": 12.971599,
    "lon": 77.594566,
    "appid": "69f04e4613056b159c2761a9d9e664d2",
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_endpoint, params = weather_params)
print(response.status_code)
print(response.json())