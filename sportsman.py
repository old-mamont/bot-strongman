import requests
from Config import appid

class Weather():
    id_city = 1508291
    def get_weather_city():
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                     params={'id': Weather.id_city, 'type': 'like', 'units': 'metric', 'lang': 'ru', 'APPID': appid()})
        data = res.json()
        return data
    


class Tracker():
    def __init__(self) -> None:
        pass


class UserRequests():
    def __init__(self) -> None:
        pass

class TrainingPlans():
    def __init__(self) -> None:
        pass

class Community():
    def __init__(self) -> None:
        pass

# Weather.get_weather_city()