import requests
import json
# response = requests.get("http://www.omdbapi.com/?apikey=505480d7&s=joker")
# if response.status_code == 200:
#     print(response.json())  # {"name": "michael", "age": 40, "count": 12345}

while True:
    command = input('Enter command (or "exit" to quit): ')
    if command.lower() == "exit":
        print("Goodbye!")
        break

    response = requests.get("http://www.omdbapi.com/?apikey=505480d7&s=" + command)
    if response.status_code == 200:
        data = response.json()
        for movie in data.get("Search"): #  для фильмов в список вытащить пbreоиск
            print(f" {movie['Title']} ({movie['Year']})") # выводим пользователю его результаты

