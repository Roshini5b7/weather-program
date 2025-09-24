** 1. Importing the requests library**
python
import requests

* This lets you send HTTP requests to web APIs (in this case, OpenWeatherMap API).*
 
**2. API setup**
python
API_KEY = '5ae4c373cc54eb43325d86f2982fbddc'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
* You store your *API key* (unique code to access OpenWeatherMap).
* BASE_URL is the endpoint for the current weather API.

**3. Defining the function get_weather(city)**
python
def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

* Takes a city name as input.
* Prepares *parameters* (city name, API key, temperature in Celsius).
* Sends an HTTP GET request to the OpenWeatherMap API.
* Converts the API response to JSON format (data).
  
**4. Error Handling**
python
if response.status_code != 200 or data.get('cod') != 200:
    print('City not found or API Error.')
    return
* Checks if the API request was successful (status_code 200 means success).
* If not, prints an error message and stops.
  
 **5. Extracting useful data**
python
weather = data['weather'][0]['description']
temperature = data['main']['temp']
humidity = data['main']['humidity']
wind_speed = data['wind']['speed']
* Extracts *description* (like "clear sky", "rain").
* Extracts *temperature* in °C.
* Extracts *humidity* percentage.
* Extracts *wind speed* in m/s.
  
**6. Printing results**
python
print(f"-Weather in {city}")
print(f"- Description: {weather}")
print(f"- Temperature: {temperature}°C")
print(f"- Humidity: {humidity}%")
print(f"- Wind Speed: {wind_speed} m/s")
* Displays the collected weather details nicely formatted.
  
** 7. Main program**
python
if _name_ == "_main_":
    city = input("Enter city name: ")
    get_weather(city)
* This part is slightly wrong ❌ → It should be:
  
python
if __name__ == "__main__":
* When fixed, it runs the program only if you execute this file directly.
* It asks the user for a city name, then calls get_weather(city).
