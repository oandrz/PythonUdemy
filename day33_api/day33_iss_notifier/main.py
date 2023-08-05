import time

import pytz
import requests
from datetime import datetime
import smtplib

my_email = ""
password = ""

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude


def is_current_position_near_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    check_lat = (iss_latitude - 5) <= iss_latitude <= (iss_latitude + 5)
    check_long = (iss_longitude - 5) <= iss_longitude <= (iss_longitude + 5)

    return check_lat and check_long


def is_evening():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    kuala_lumpur = pytz.timezone('Asia/Kuala_Lumpur')
    now_in_kuala_lumpur = time_now.astimezone(kuala_lumpur)
    is_evening = now_in_kuala_lumpur.hour >= sunset
    return is_evening


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

# Your position is within +5 or -5 degrees of the ISS position.

while True:
    time.sleep(60) # send every 60s
    if is_current_position_near_iss() and is_evening():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="oentoro.andreas@gmail.com",
                msg="Hey man, look up!"
            )
            print("email send successfully")
    else:
        print("There's no space station")
