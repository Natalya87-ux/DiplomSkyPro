import requests


class AviasalesApi:
    def __init__(self, url: str):
        """Конструктор класса.
           На вход принимает ссылку на корневой узел URL API Aviasales
        """
        self._url = url

    def get_airline_directions(self, params: dict) -> requests.Response:
        """Метод для взаимодействия с методом airline-directions
        Возвращает направления, по которым авиакомпания осуществляет перелеты,
        отсортированные по популярности
        """
        addUri = "/v1/airline-directions?"
        resp = requests.get(self._url + addUri, params=params)
        return resp

    def get_prices_by_calendar(self, params: dict) -> requests.Response:
        """Метод для взаимодействия с методом calendar
        Возвращает самый дешевый билет (без пересадки, с одной
        или двумя пересадками)
        для указанного направления для каждого дня выбранного месяца
        """
        addUri = "/v1/prices/calendar?"
        resp = requests.get(self._url + addUri, params=params)
        return resp

    def get_prices_for_dates(self, params: dict) -> requests.Response:
        """Метод для взаимодействия с методом prices_for_dates
        Запрос возвращает самые дешевые авиабилеты за определённые даты,
        найденные пользователями Авиасейлс за последние 48 часов
        """
        addUri = "/aviasales/v3/prices_for_dates?"
        resp = requests.get(self._url + addUri, params=params)
        return resp

    def get_latest_prices(self, params: dict) -> requests.Response:
        """Метод для взаимодействия с методом get_latest_prices
        Возвращает цены на авиабилеты за определённый период,
        найденные пользователями Авиасейлс за последние 48 часов
        """
        addUri = "/aviasales/v3/get_latest_prices?"
        resp = requests.get(self._url + addUri, params=params)
        return resp
