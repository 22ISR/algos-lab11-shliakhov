import requests
import json
response = requests.get("http://www.omdbapi.com/?apikey=505480d7&s=joker")
if response.status_code == 200:
    print(response.json())  # {'name': 'michael', 'age': 40, 'count': 12345}

