import requests
import os
import datetime as dt

NUT_ID = os.environ.get('NUT_ID')
NUT_API_KEY = os.environ.get('NUT_API_KEY')
NUT_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
nut_headers = {
    'x-app-id': NUT_ID,
    'x-app-key': NUT_API_KEY,
}
nut_parameters = {
    'query': input('What exercises did you do? '),
}

nut_response = requests.post(url=NUT_ENDPOINT, json=nut_parameters, headers=nut_headers)
data = nut_response.json()['exercises']

SHEETY_ENDPOINT = 'https://api.sheety.co/f4a6ed9b1279b8badb73379294f3decd/workoutTracking/workouts'
sheety_headers = {
    'Authorization': os.environ.get('SHEETY_AUTH')
}
for element in data:
    sheety_parameters = {
        'workout': {
            'date': dt.date.today().strftime('%d/%m/%Y'),
            'time': dt.datetime.now().strftime('%H:%M:%S'),
            'exercise': element['name'].title(),
            'duration': round(element['duration_min']),
            'calories': round(element['nf_calories']),
        }
    }
    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_parameters, headers=sheety_headers)
    print(sheety_response.text)
