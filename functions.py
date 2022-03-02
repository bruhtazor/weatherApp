import requests

#unit = metric(C), imperial(F) or standard(kelvin)
def get_city_info(api_key, city, unit):
    url =f"http://api.openweathermap.org/data/2.5/weather?q={city}&units={unit}&appid={api_key}"
    response = requests.get(url).json()
    return response

def get_temp(response):
    temp = response['main']['temp']
    tempMin = response['main']['temp_min']
    tempMax = response['main']['temp_max']
    feelsLike = response['main']["feels_like"]
    all = [temp, feelsLike, tempMin, tempMax]
    return all
