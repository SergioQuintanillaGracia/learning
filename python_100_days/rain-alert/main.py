import requests
from twilio.rest import Client

account_sid = "..."
auth_token = "..."

owm_endpoint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = "..."

parameters = {
    "lat": "59.911859",
    "lon": "10.762178",
    "cnt": "4",
    "appid": api_key
}
response = requests.get(owm_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

will_rain = False

# Check if at some point it will rain
for datapoint in weather_data["list"]:
    for weather_condition in datapoint["weather"]:
        if weather_condition["id"] < 700:
            will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="...",
        to="..."
    )
    print(message.status)
else:
    print("No rain")