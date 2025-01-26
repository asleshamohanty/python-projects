import requests

class DataManager:

    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/55f9227d8d1fb79ef9a5ce1e93510660/flightDealsTracker/prices"

    def get_destination_data(self):
        self.response = requests.get(url = self.sheety_endpoint)
        self.data = self.response.json()
        self.destination_data = self.data["prices"]
        return self.destination_data

    def update_data(self):
        for city in self.destination_data:
            new_data = {"prices": {"IATA Code": city["iataCode"]}}
            response = requests.put(url = f"{self.sheety_endpoint}/{city['id']}", json = new_data)
            print(response.text)