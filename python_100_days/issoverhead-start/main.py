import time

import requests
from datetime import datetime
import smtplib

email = "..."
password = "..."

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

def is_iss_close():
    # Your position is within +5 or -5 degrees of the ISS position
    return abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5

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

while True:
    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()

        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])


        # It's nighttime
        if is_iss_close():
            # Send email
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=email, password=password)
                connection.sendmail(
                    from_addr=email,
                    to_addrs=email,
                    msg="Look up! The ISS is over you!"
                )

            print("Email sent!")

        else:
            print("Station not close enough")

    else:
        print("It's not nighttime yet")

    time.sleep(60)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
