import requests
from twilio.rest import Client

CURRENT_POS = (1.352083, 103.819839)
API_KEY = "7ff8d78d9ef0d00f9755add5e2f7e028"
account_sid = "AC37d691958f59caa2fadbaeaea7fb1ed2"
account_auth_token = "2089d3402e3db7c23d7e4f65078847de"

param = {
    "lat": CURRENT_POS[0],
    "lon": CURRENT_POS[1],
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=param)
response.raise_for_status()
weather_data = response.json()


will_rain = False
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, account_auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☔️",
            from_='+14694895439',
            to='+6583741619'
        )
    print(message.status)
