import functions as func
from configparser import ConfigParser
import json
import time

#get elements from config.ini file
file = "config.ini"
config = ConfigParser()
config.read(file)

API_KEY = config["Settings"]["apiKey"]
UNIT = config["Settings"]["unit"]
city = "lausanne"

'''#counter that calls the api only once per Hour & overwrite the value in data.json
startTime = time.time()
while True:'''
#store data into json file to minimise calling the API
response = func.get_city_info(API_KEY, city, UNIT)
with open("data.json","w") as outputFile:
    json.dump(response, outputFile)
outputFile.close()
    #time.sleep(3600 - ((time.time() - startTime) % 3600))

with open("data.json") as dataJson:
    data = json.load(dataJson)
temp = func.get_temp(data)
weather = func.get_weather(data)
sunHour = func.get_sun_hour(data)

print(f"The actual temperature of {city} is {temp[0]}C that feels like {temp[1]}, with a minimum of {temp[2]}C and a maximum of {temp[3]}C")
print(f"The weather is {weather}")
print(f"the sunrises at {sunHour[0]}, sets at {sunHour[1]}, with a total sun hour of {sunHour[2]}")