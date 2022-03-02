import functions as func
from configparser import ConfigParser
import json

#get elements from config.ini file
file = "config.ini"
config = ConfigParser()
config.read(file)

API_KEY = config["Settings"]["apiKey"]
UNIT = config["Settings"]["unit"]

#TODO: if else statement with counter to call the api only once per Hour
#store data into json file to minimise calling the API
response = func.get_city_info(API_KEY,"lausanne", UNIT)
with open("data.json","w") as outputFile:
    json.dump(response, outputFile)
outputFile.close()

data = open("data.json", "r")
print(data.read(5))