import requests
from datetime import datetime
import json

#unit = metric(C), imperial(F) or standard(kelvin)
def get_city_info(api_key, city, unit):
    url =f"http://api.openweathermap.org/data/2.5/weather?q={city}&units={unit}&appid={api_key}"
    response = requests.get(url).json()
    return response

def overwrite_data(response, fileName):
    with open(fileName,"w") as outputFile:
        json.dump(response, outputFile)
    outputFile.close()

#gets temp, max & min temp
def get_temp(response):
    temp = response['main']['temp']
    tempMin = response['main']['temp_min']
    tempMax = response['main']['temp_max']
    feelsLike = response['main']["feels_like"]
    all = [temp, feelsLike, tempMin, tempMax]
    return all

#gets weather description
def get_weather(response):
    weathDescription = response['weather'][0]['description']
    return weathDescription

#gets sunrise, sunset in unix timestamp convert to readable hour
# returns sunrise hour & total sun hour 
def get_sun_hour(response):
    sunriseUnix = response['sys']['sunrise']
    sunrise = datetime.utcfromtimestamp(sunriseUnix).strftime('%H:%M:%S')
    sunsetUnix = response['sys']['sunset']
    sunset = datetime.utcfromtimestamp(sunsetUnix).strftime('%H:%M:%S')
    sunHourUnix = sunsetUnix - sunriseUnix
    sunHour = datetime.utcfromtimestamp(sunHourUnix).strftime('%H:%M:%S')
    all = [sunrise, sunset, sunHour]
    return all
