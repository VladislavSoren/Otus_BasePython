class InvalidCity(Exception):
    def __init__(self, message):
        self.city = message
        # super().__init__(message)  # Не вижу особого смысла


print(InvalidCity.mro())

WEATHER_FORECAST = {
    'moscow': {
        "rain_chance": 52,
        'humidity': 60
    },
    'omsk': {
        "rain_chance": 15,
        'humidity': 42
    }
}


def get_weather(city):
    forecast = WEATHER_FORECAST.get(city.lower())
    if forecast is None:
        raise InvalidCity(city)

    return WEATHER_FORECAST[city.lower()]


def rain_tomorrow(city):
    """
    :param city:
    :return: bool or None
    """

    try:
        weather = get_weather(city)
    except InvalidCity as e:
        print("could not find weather for", e.args, e.city)
        return
    print(f'Weather for {city} conds: ', weather)

    return weather['rain_chance'] > 50


print(rain_tomorrow("Moscow"))
print(rain_tomorrow("Omsk"))
print(rain_tomorrow("Minsk"))
