import os
from typing import Any
import requests
import telebot
from telebot.types import Message


class WeatherClient:
    def __init__(
        self,
        geo_url: str = "https://geocoding-api.open-meteo.com/v1/search",
        weather_url: str = "https://api.open-meteo.com/v1/forecast",
        metrics: str = "temperature_2m,apparent_temperature,relative_humidity_2m,wind_speed_10m",
        timeout: int = 10,
    ) -> None:
        self.geo_url = geo_url
        self.weather_url = weather_url
        self.metrics = metrics
        self.timeout = timeout

    def request_json(self, url: str, params: dict[str, Any]) -> dict[str, Any]:
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError as err:
            raise ValueError(f"Ответ сервера не является JSON: {response.text}") from err

    def get_weather(self, city: str) -> str:
        geo = self.request_json(self.geo_url, {"name": city, "count": 1, "language": "ru"})
        results = geo.get("results")
        if not results:
            return f"Город «{city}» не найден."

        try:
            loc = results[0]
            params = {
                "latitude": loc["latitude"],
                "longitude": loc["longitude"],
                "current": self.metrics,
            }
            cur = self.request_json(self.weather_url, params)["current"]
            return (
                f"Город: {loc['name']}\n"
                f"Темпа: {cur['temperature_2m']}°C (на деле {cur['apparent_temperature']}°C)\n"
                f"Влажность: {cur['relative_humidity_2m']}%, скорость ветра: {cur['wind_speed_10m']} км/ч"
            )
        except (KeyError, IndexError) as err:
            raise KeyError(f"В ответе API не хватает поля или индекса: {err}") from err


if __name__ == "__main__":
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("Не задана переменная окружения BOT_TOKEN")

    bot = telebot.TeleBot(token)
    weather = WeatherClient()

    @bot.message_handler(commands=["start"])
    def handle_start(message: Message) -> None:
        bot.send_message(message.chat.id, "Привет! Напиши город, чтобы узнать погоду.")

    @bot.message_handler(content_types=["text"])
    def handle_message(message: Message) -> None:
        try:
            bot.send_message(message.chat.id, weather.get_weather(message.text))
        except Exception as err:
            bot.send_message(message.chat.id, f"Ошибка: {err}")

    bot.polling(none_stop=True)