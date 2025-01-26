import requests

api_key = ""
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = ""
auth_token = ""

weather_params = {
    "lat": 12.971599,
    "lon": 77.594566,
    "appid": "",
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_endpoint, params = weather_params)
print(response.status_code)
print(response.json())
