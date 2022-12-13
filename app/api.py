import requests
from decouple import config


api_url = "http://api.weatherapi.com/v1/current.json"
API_KEY = config("API_KEY")


def get_weather(city_name):
    params = {
        "key": API_KEY,
        "q": city_name,
    }
    response = requests.get(api_url, params=params)
    weather_info = response.json()
    return weather_info




