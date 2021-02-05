import requests
from decouple import config


LAT = '7.4315422064317636'
LON = '80.71661806492484'

para = {
    'lat': LAT,
    'lon': LON,
    'exclude': 'current,minutely,daily',
    'appid': config('API_KEY'),
}

url = "https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(url, params=para)
response.raise_for_status()
weather_data = response.json()

hours = weather_data['hourly']

bring_umbrella = False

for i in range(12):
    hour = hours[i]
    id = hour['weather'][0]['id']
    if id < 700:
        bring_umbrella = True

if bring_umbrella:
    print("Bring an umbrella.")

# print(weather_data)
