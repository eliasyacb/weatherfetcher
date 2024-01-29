import requests

API_KEY = "ce63ed4629024c3945fc380f0eec536e"


city = input("Enter a city name: ")
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={API_KEY}")

if weather_data.status_code == 200:
    data = weather_data.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"]- 32, 1) * (5/9)

    print("Weather: ", weather)
    print("Temperature", temperature, "celsius")
else: 
    print("An erorr occurred.")