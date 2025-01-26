'''import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file) #creates an object
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temp = int(row[1])
            temperatures.append(temp)
    print(temperatures)
'''

import pandas

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()
print(temp_list)
print(f"Average Temperature is: {round((sum(temp_list)/len(temp_list)),2)}")
print(data["temp"].mean())
print(data["temp"].max())
data_dict = data.to_dict()
print(data_dict)

#Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])


