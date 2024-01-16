import requests
# import dotenv
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print("\n*** Get current Weather Conditions ***\n")

    city = input("\nPlease enter a city name:\n")

    request_url = f"https://api.openweathermap.org/data/3.0/onecall?appid={os.getenv('API_KEY')}&q={city}units=metric"

    # print(request_url)

    weather_data = requests.get(request_url).json()

    # pprint(weather_data)

    print(f"\nCurrent weather for {weather_data['name']}")
    print(f"\nThe temp is{weather_data['name']['temp']}")
    print(
        f"\nFeels like {weather_data['name']['feels_like']} and{weather_data['weather'][0]['description']}.")

if __name__ == "__main__":
    get_current_weather()