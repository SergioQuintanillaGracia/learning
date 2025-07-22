from datetime import datetime
import os
import requests

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

WEIGHT_KG = 82
HEIGHT_CM = 180
AGE = 45

userinput = input("Which exercises did you do?: ").strip()

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

nutritionix_json = {
    "query": userinput,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=nutritionix_json, headers=nutritionix_headers)
response = response.json()

for exercise in response["exercises"]:
    data = exercise
    print(data)

    date = datetime.now().strftime("%d/%m/%Y")
    time = datetime.now().strftime("%H:%M:%S")
    exercise = data["name"].capitalize()
    duration = int(data["duration_min"])
    calories = float(data["nf_calories"])

    print(date, time, exercise, duration, calories)

    sheety_add_row_endpoint = os.environ["SHEET_ENDPOINT"]

    sheety_headers = {
        "Authorization": f"Bearer {os.environ["TOKEN"]}"
    }

    sheety_json = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }

    response = requests.post(sheety_add_row_endpoint, json=sheety_json, headers=sheety_headers)
    print(response.text)