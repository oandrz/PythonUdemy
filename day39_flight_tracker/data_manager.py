import os
import requests

SHEETY_AUTH = os.getenv("SHEETY_AUTH")
SHEETY_ID = os.getenv("SHEETY_ID")
SHEETY_URL = f"https://api.sheety.co/{SHEETY_ID}/flightDeals/prices"
sheety_header = {
    "Content-Type": "application/json",
    "Authorization": SHEETY_AUTH
}

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_URL}/{city['id']}",
                json=new_data,
                headers=sheety_header
            )
            print(response.text)

    def fetch_all_prices(self):
        response = requests.get(url=SHEETY_URL, headers=sheety_header)
        json_response = response.json()
        print(json_response)
        response.raise_for_status()

        return json_response["prices"]

