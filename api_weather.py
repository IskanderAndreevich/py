from typing import Any
import requests


class WeatherClient:
    def __init__(
        self,
        geo_url: str = "https://geocoding-api.open-meteo.com/v1/search",
        weather_url: str = "https://api.open-meteo.com/v1/forecast",
    ) -> None:
        self.geo_url: str = geo_url
        self.weather_url: str = weather_url

    def _get_json(self, url: str, params: dict[str, Any]) -> dict[str, Any] | None:
        try:
            resp = requests.get(url, params=params, timeout=10)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.JSONDecodeError:
            print("Ошибка: сервер вернул не JSON")
        except requests.RequestException as err:
            print(f"Ошибка сети: {err}")
        return None

    def get_coordinates(self, city: str) -> tuple[float, float, str] | None:
        data = self._get_json(self.geo_url, {"name": city, "count": 1, "language": "ru"})
        if not data or not data.get("results"):
            return None
        loc = data["results"][0]
        return loc["latitude"], loc["longitude"], loc["name"]

    def get_weather(self, city: str) -> str:
        coords = self.get_coordinates(city)
        if not coords:
            return f"Не удалось найти координаты для города: {city}"

        lat, lon, name = coords
        params: dict[str, Any] = {
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,apparent_temperature,wind_speed_10m",
        }
        data = self._get_json(self.weather_url, params)
        if not data or "current" not in data:
            return "Не удалось получить данные о погоде."

        cur = data["current"]
        return (
            f"Локация: {name}\n"
            f"Сейчас: {cur.get('temperature_2m')}°C "
            f"(ощущается как {cur.get('apparent_temperature')}°C), "
            f"ветер {cur.get('wind_speed_10m')} км/ч"
        )


if __name__ == "__main__":
    city: str = input("Введите название города: ")
    client = WeatherClient()
    print(client.get_weather(city))