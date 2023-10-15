# Weather API Project credit to Youtube channel 'NueralNine'. Wind Speed Conversion function was self-made.
# Future updates would ideally include the Geocoder Import to auto-detect the users location. 

import datetime as dt
import requests

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
API_KEY = '88e452115bbd89dc2acc3d923d376fd1'
CITY = 'Oslo'

# Can also be written as follows, as per the documentation.:
# https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
#  More granularity in the Parameters, Units of Measurement and Language settings.


def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin -273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit


def wind_speed_conversion(metric):
    imperial = metric * 2.237
    return imperial, metric


url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)

feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

wind_speed = response['wind']['speed']
wind_speed_imperial, wind_speed_metric = wind_speed_conversion(wind_speed)

humidity = response['main']['humidity']
description = response['weather'][0]['description']

sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])

sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])


print(f"Weather Description in {CITY}: {description}")
print(f"Temperature in {CITY}: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
print(f"Temperature in {CITY} feels like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind speed in {CITY}: {wind_speed_metric}m/s or {wind_speed_imperial}mph")
print(f"Sunrise in {CITY}: {sunrise_time}")
print(f"Sunset in {CITY}: {sunset_time}")


#Prints the structure of the response. Shows a dictionary with key/value pairs that we can use to customize the response. 
print(response)