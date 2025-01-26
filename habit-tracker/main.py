import requests
from datetime import *
from tkinter import *

# VARIABLES
USERNAME = "aslesha"
TOKEN = "shdjkfhsf"
GRAPHID = "graph1"
header = {"X-USER-TOKEN": TOKEN}
FONT = ("Ariel", 15, "normal")

# DATE
now = datetime.now()
today = str(now.date())
today_formatted = today.replace("-","")

# CREATING USER
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN, #password
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"}

user_response = requests.get(url = pixela_endpoint, params = user_params)

# CREATING GRAPH
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPHID,
    "name": "Walking Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"}

# CREATING PIXELS
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
pixel_data = {"date" : today_formatted, "quantity": "18.8"}

# UPDATING A PIXEL
pixel_updation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today_formatted}"
updating_data = {"quantity": "9.2"}

# DELETING A PIXEL
pixel_deletion_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today_formatted}"



response = requests.post(url = pixel_creation_endpoint, json = pixel_data, headers = header)
print(response.text)