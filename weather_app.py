import requests

API_KEY = "your_api_key_here"  # Get free key from https://openweathermap.org/api
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    url = BASE_URL + f"appid={API_KEY}&q={city}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']

        print(f"\n🌍 Weather in {city.title()}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Condition: {weather['description'].title()}")
        print(f"Humidity: {main['humidity']}%")
        print(f"Wind Speed: {wind['speed']} m/s\n")
    else:
        print("❌ City not found. Please try again.")

if __name__ == "__main__":
    print("=== Weather App 🌦️ ===")
    city = input("Enter city name: ")
    get_weather(city)
