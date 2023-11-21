import requests
import argparse
import pyfiglet
from simple_chalk import chalk

API_KEY = "11a6015d0c4e6f0f696970be5b0978c6"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
WEATHER_ICONS = {
    "01d": "☀️",
    "02d": "⛅",
    "03d": "☁",
    "04d": "☁",
    "09d": "🌧",
    "10d": "🌦",
    "11d": "🌩",
    "13d": "🌨",
    "50d": "🌫",
    "01n": "🌙",
    "02n": "⛅",
    "03n": "☁",
    "04n": "☁",
    "09n": "🌧",
    "10n": "🌦",
    "11n": "🌩",
    "13n": "🌨",
    "50n": "🌫",
}

parser = argparse.ArgumentParser(description="Check the weather for a certain country/city")
parser.add_argument("country", help="The country/city to check the weather for")
args = parser.parse_args()
url = f"{BASE_URL}?q={args.country}&appid={API_KEY}&units=metric"

response = requests.get(url)
if response.status_code != 200:
    print(chalk.red("Error: Unable to retrieve the weather information"))
    exit()

data = response.json()

temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
description = data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city = data["name"]
country = data["sys"]["country"]
celsius_to_fahrenheit = (temperature * 9/5) + 32
celsius_to_fahrenheit_feels = (feels_like * 9/5) + 32


weather_icon = WEATHER_ICONS.get(icon, "")
output = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
output += f"{weather_icon} {description}\n"
output += f"Temperature: {temperature}℃  / {celsius_to_fahrenheit}°F\n"
output += f"Feels like: {feels_like}℃  / {celsius_to_fahrenheit_feels}°F\n"

print(chalk.green(output))
