
class WeatherService:
    __unk = "Unknown"

    @classmethod
    def __get_current_payload(cls, current):
        current_info = dict()
        current_info["last_updated"] = current.get("last_updated", cls.__unk)
        current_info["temp_c"] = current.get("temp_c", cls.__unk)
        current_info["temp_f"] = current.get("temp_f", cls.__unk)
        current_info["wind"] = current.get("wind_mph", cls.__unk)
        current_info["pressure"] = current.get("pressure_in", cls.__unk)
        current_info["feels_like_c"] = current.get("feelslike_c", cls.__unk)
        current_info["feels_like_f"] = current.get("feelslike_f", cls.__unk)
        condition = current["condition"]
        current_info["condition"] = condition.get("text", cls.__unk)
        return current_info

    @classmethod
    def __get_location_payload(cls, location):
        location_info = dict()
        location_info["city_name"] = location.get("name", cls.__unk)
        location_info["region"] = location.get("region", cls.__unk)
        location_info["country"] = location.get("country", cls.__unk)
        location_info["date_time"] = location.get("localtime", cls.__unk)
        return location_info

    @classmethod
    def get_weather_payload(cls, weather_data):
        error = weather_data.get("error", None)
        if error:
            err_message = error["message"]
            return {"error": err_message}

        location = weather_data.get("location", None)
        current = weather_data.get("current", None)

        location_info = dict()
        current_info = dict()

        if location:
            location_info = cls.__get_location_payload(location)
        if current:
            current_info = cls.__get_current_payload(current)

        return {
                "location_info": location_info,
                "current_info": current_info,
            }

