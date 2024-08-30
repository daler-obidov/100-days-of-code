import requests
from datetime import datetime

username = "eclipsedmenoway7"
password = "sjdhfuegfuefbbfbdk"
pixela = "https://pixe.la/v1/users" 

headers = {
    "X-USER-TOKEN": password
}

user_params = {
    "token": password,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": 'yes'
}

graph = f'{pixela}/{username}/graphs'

graph_config = {
    "id": "graphnumber1",
    "name": "Daily Water Drink Graph",
    "unit": "litre",
    "type": "float",
    "color": "sora"
}

today = datetime.now()

posting = f'{graph}/graphnumber1'

data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How much water did you drink today? ")
}

# updating = f'{posting}/{today.strftime("%Y%m%d")}'

# updated = {
#     "quantity": "7.2"
# }

response = requests.post(url=posting, json=data, headers=headers)

# response = requests.put(url=updating, json=updated, headers=headers)
# print(response.text)
