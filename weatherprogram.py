import requests

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
API_KEY = '5ae4c373cc54eb43325d86f2982fbddc'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # For Celsius
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if response.status_code != 200 or data.get('cod') != 200:
        print('City not found or API Error.')
        return

    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print(f"-Weather in {city}")
    print(f"- Description: {weather}")
    print(f"- Temperature: {temperature}°C")
    print(f"- Humidity: {humidity}%")
    print(f"- Wind Speed: {wind_speed} m/s")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
    
