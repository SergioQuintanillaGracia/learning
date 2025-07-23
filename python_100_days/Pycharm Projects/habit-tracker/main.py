import requests
from datetime import datetime

TOKEN = "123mniobvs7n8vi348977gbv"
USERNAME = "juana"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph2",
    "name": "Among Us Wins Graph",
    "unit": "times",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{graph_config["id"]}"

today = datetime.now()
today_formatted = today.strftime("%Y%m%d")
print(today_formatted)

pixel_config = {
    "date": "20250721",
    "quantity": "5"
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixel_endpoint}/{today_formatted}"

update_pixel_config = {
    "quantity": "10"
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

delete_pixel_endpoint = update_pixel_endpoint

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)