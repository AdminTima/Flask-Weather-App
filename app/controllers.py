from flask import Blueprint, render_template, request
from .api import get_weather
from .service import WeatherService


weather_bp = Blueprint("weather_bp", __name__, static_folder="static")


@weather_bp.route("/", methods=["POST", "GET"])
def get_current_weather():
    error = None
    location_info = None
    current_info = None
    if request.method == "POST":
        city_name = request.form.get("city_name")
        weather_data = get_weather(city_name)
        print(weather_data)
        payload = WeatherService.get_weather_payload(weather_data)
        if "error" in payload:
            error = payload["error"]
        else:
            location_info = payload["location_info"]
            current_info = payload["current_info"]
    return render_template(
            "index.html",
            location_info=location_info,
            current_info=current_info,
            error=error,
        )
