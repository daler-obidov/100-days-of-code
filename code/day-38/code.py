import requests
from datetime import datetime

API_KEY = "95a6e87dd94cd6fe8aebe8e85cb66e0e"
API_ID = "9f18ea1e"

exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheety_url = "https://api.sheety.co/a67804496d930dd7885cdc5a36ab0ae5/myWorkouts/workouts"

time_now = datetime.now()
current_date = time_now.strftime("%Y:%m:%d")
current_time = time_now.strftime("%H:%M:%S")

GENDER = 'Male'
WEIGHT_KG = "54"
HEIGHT_CM = "177"
AGE = "16"

exercise_text = input("Which exercise did you do: ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_url, json=params, headers=headers)
result = response.json()

for exercise in result['exercises']:
    exercise_data = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    
    sheet_response = requests.post(sheety_url, json=exercise_data)
    print(sheet_response.text)
