import requests
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

GENDER = os.getenv("GENDER")
WEIGHT = float(os.getenv("WEIGHT"))
HEIGHT = float(os.getenv("HEIGHT"))
AGE = int(os.getenv("AGE"))

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
