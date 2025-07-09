import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# # if response.status_code != 200:
# #     raise Exception("Bad response from ISS API")
#
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)

LAT = 51.507351
LONG = -0.127758

parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise, sunset)

sunrise_hour = sunrise.split("T")[1][:2]
sunset_hour = sunset.split("T")[1][:2]
print(sunrise_hour, sunset_hour)

time_now = datetime.now()
hour_now = time_now.hour