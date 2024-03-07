import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        return f"Weather in {city}: {weather_description}, Temperature: {temperature}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} m/s"
    else:
        return "Error fetching weather data."

def main():
    api_key = 'fa283b9219730ef0f1808cc0f1497b2c'  # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    city = input("Enter city name: ")
    print(get_weather(api_key, city))

if __name__ == "__main__":
    main()