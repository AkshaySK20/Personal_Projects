import requests
from pynput.keyboard import Key, Listener

api_key = '4d8567cfc8c2099137a1b5d90ab62c71'

while True:
    # if keyboard.is_pressed('esc'):
    user_input = input("Enter the city: ")
    if user_input == "Quit":
        break
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&appid={api_key}")
    if weather_data.json()['cod'] == '404':
        print("Invalid City!")
    else:
        # print(weather_data.json())
        weather = weather_data.json()['weather'][0]['description']
        temp = weather_data.json()['main']['temp']
        wind = weather_data.json()['wind']['speed']

        print(f"The weather in {user_input} is {weather}")
        print(f"The temperature is {temp} °C")
        print(f"The wind speed is {wind} m/s")
