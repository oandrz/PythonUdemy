import os
from flight_data import FlightData

import requests
FLIGHT_API_KEY = os.getenv("KIWI_FLIGHT")
FLIGHT_SEARCH_HOST = "https://api.tequila.kiwi.com"
headers = {"apikey": FLIGHT_API_KEY}

class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{FLIGHT_SEARCH_HOST}/locations/query"
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def get_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "SGD"
        }

        response = requests.get(
            url=f"{FLIGHT_SEARCH_HOST}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except (IndexError, KeyError):
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: SGD {flight_data.price}")
        return flight_data
