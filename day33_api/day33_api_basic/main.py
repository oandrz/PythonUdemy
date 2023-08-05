import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
print(data["iss_position"])

parameters = {
    "lat": 11.0,
    "lng": 12.2,
    "formatted":0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise)