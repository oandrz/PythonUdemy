import os
import requests
import datetime as dt

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEETY_AUTH = os.getenv("SHEETY_AUTH")
SHEETY_ID = os.getenv("SHEETY_ID")

exercise_query = input("What are the exercise that you did ?")

request_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}
request_param = {
    "query": exercise_query,
    "gender": "male",
    "weight_kg": 73,
    "height_cm": 176,
    "age": 28
}
url = "https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(url=url, json=request_param, headers=request_header)
response_data = response.json()
print(response_data)
response.raise_for_status()

sheety_url = f"https://api.sheety.co/{SHEETY_ID}/myWorkouts/workouts"

for exercises in response_data["exercises"]:
    today = dt.datetime.now()
    cur_date = today.strftime("%d/%m/%Y")
    cur_time = today.strftime("%H:%M:%S")
    sheety_header = {
        "Content-Type": "application/json",
        "Authorization": SHEETY_AUTH
    }

    sheety_param = {
        "workout": {
            "date": cur_date,
            "time": cur_time,
            "exercise": exercises["name"],
            "duration": exercises["duration_min"],
            "calories": exercises["nf_calories"]
        }
    }
    sheety_post_response = requests.post(url=sheety_url, json=sheety_param, headers=sheety_header)
    print(sheety_post_response.json())
