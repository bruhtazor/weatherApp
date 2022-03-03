import functions as func
from configparser import ConfigParser
import json

#global settings
#get elements from config.ini file
file = "config.ini"
config = ConfigParser()
config.read(file)
API_KEY = config["Settings"]["apiKey"]
UNIT = config["Settings"]["unit"]
city = input("enter city name: ")

#store data into json file to call the API at the start
response = func.get_city_info(API_KEY, city, UNIT)
func.overwrite_data(response, "data.json")

with open("data.json") as dataJson:
    data = json.load(dataJson)
temp = func.get_temp(data)
weather = func.get_weather(data)
sunHour = func.get_sun_hour(data)

print(f"The actual temperature of {city} is {temp[0]}C that feels like {temp[1]}, with a minimum of {temp[2]}C and a maximum of {temp[3]}C")
print(f"The weather is {weather}")
print(f"the sunrises at {sunHour[0]}, sets at {sunHour[1]}, with a total sun hour of {sunHour[2]}")
