import requests

API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Change to "imperial" for Fahrenheit
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
        return weather
    else:
        return None

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather = get_weather(city)
    
    if weather:
        print(f"\nWeather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Condition: {weather['description'].capitalize()}")
    else:
        print("City not found or API error.")
