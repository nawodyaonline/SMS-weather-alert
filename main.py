import requests
from twilio.rest import Client
from decouple import config

account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')

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

sliced_hours = weather_data['hourly'][:12]

bring_umbrella = False

for hour in sliced_hours:
    id = hour['weather'][0]['id']
    if id < 700:
        bring_umbrella = True

if bring_umbrella:
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                    body="It's going to rain today. Remember to bring an ☔",
                    from_='+12016465598',
                    to='+94779802204'
                )
    print(message.status)




# print(weather_data)
