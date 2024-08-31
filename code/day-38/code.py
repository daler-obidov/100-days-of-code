import requests
from datetime import datetime

# Replace with your actual API Key and ID
API_KEY = "95a6e87dd94cd6fe8aebe8e85cb66e0e"
API_ID = "9f18ea1e"

# Nutritionix API endpoint
exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Sheety API endpoint - replace with your actual endpoint
sheety_url = "https://api.sheety.co/a67804496d930dd7885cdc5a36ab0ae5/myWorkouts/workouts"

# Get the current date and time
time_now = datetime.now()
current_date = time_now.strftime("%Y:%m:%d")
current_time = time_now.strftime("%H:%M:%S")

# User information
GENDER = 'Male'
WEIGHT_KG = "54"
HEIGHT_CM = "177"
AGE = "16"

# Input for the exercise
exercise_text = input("Which exercise did you do: ")

# Headers for the Nutritionix API
headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

# Parameters for the exercise API call
params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Call the Nutritionix API
response = requests.post(exercise_url, json=params, headers=headers)
result = response.json()

# Loop through each exercise from the API response
for exercise in result['exercises']:
    exercise_data = {
        "workout": {  # Change from "sheet1" to "workout"
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    
    # Post the data to Sheety
    sheet_response = requests.post(sheety_url, json=exercise_data)
    print(sheet_response.text)
