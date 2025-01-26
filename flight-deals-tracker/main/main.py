from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

data_manager = DataManager()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "BLR"

sheet_data = data_manager.get_destination_data()
print(sheet_data)

for i in sheet_data:
    if i["iataCode"] == "":
        for j in sheet_data:
            j["iataCode"] = flight_search.get_destination_code(j["city"])

data_manager.destination_data = sheet_data
data_manager.update_data()