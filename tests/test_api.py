import json
from pages.aviasales_api import AviasalesApi
import datetime
import allure


BaseUri = "http://api.travelpayouts.com"
token = "ad8377b320de5052879784c519050558"
# ПОЗИТИВНЫЕ ТЕСТЫ
# Поиск рейсов с указанием аэропорта


@allure.feature("API Tests for Aviasales")
@allure.title("Search directions by the airline")
@allure.description("Поиск маршутов по аэропорту")
@allure.severity(allure.severity_level.NORMAL)
def test_find_flights_of_airline_class():
    params = {"airline_code": "SU", "limit": "10", "token": token}
    Aviasales_Api = AviasalesApi(BaseUri)
    resp = Aviasales_Api.get_airline_directions(params)
    textresponse = resp.text
    responsedata = json.loads(textresponse)
    flights = responsedata["data"]
    flight = flights["AER-SVO"]
    assert flight == 4282020720


# Поиск билетов на период по маршруту
@allure.feature("API Tests for Aviasales")
@allure.title("Search directions by the period")
@allure.description("Поиск билетов на период по маршруту")
@allure.severity(allure.severity_level.NORMAL)
def test_find_tickets_for_period_by_route():
    current_date = datetime.date.today().isoformat()
    params = {
        "depart_date": current_date,
        "origin": "MOW",
        "destination": "KZN",
        "calendar_type": "departure_date",
        "currency": "rub",
        "token": token,
    }
    Aviasales_Api = AviasalesApi(BaseUri)
    resp = Aviasales_Api.get_prices_by_calendar(params)
    textresponse = resp.text
    responsedata = json.loads(textresponse)
    currency = responsedata["currency"]
    assert currency == "rub"


# Поиск билетов на дату по маршруту
@allure.feature("API Tests for Aviasales")
@allure.title("Search directions by the date")
@allure.description("Поиск билетов на дату по маршруту")
@allure.severity(allure.severity_level.NORMAL)
def test_find_tickets_for_day():
    ourdate = "2025-01-29"
    params = {
        "currency": "rub",
        "origin": "MOW",
        "destination": "KZN",
        "departure_at": ourdate,
        "one_way": "true",
        "market": "ru",
        "limit": "100",
        "unique": "false",
        "token": token,
    }
    Aviasales_Api = AviasalesApi(BaseUri)
    resp = Aviasales_Api.get_prices_for_dates(params)
    textresponse = resp.text
    responsedata = json.loads(textresponse)
    currency = responsedata["currency"]
    assert currency == "rub"


# Поиск билетов на период без пересадок
@allure.feature("API Tests for Aviasales")
@allure.title("Search directions without transfers")
@allure.description("Поиск билетов на период без пересадок")
@allure.severity(allure.severity_level.NORMAL)
def test_find_tickets_without_transfers():
    ourdate = "2025-01-22"
    params = {
        "currency": "rub",
        "origin": "MOW",
        "destination": "KZN",
        "departure_at": ourdate,
        "one_way": "true",
        "direct": "true",
        "market": "ru",
        "limit": "100",
        "unique": "false",
        "token": token,
    }
    Aviasales_Api = AviasalesApi(BaseUri)
    resp = Aviasales_Api.get_prices_for_dates(params)
    textresponse = resp.text
    responsedata = json.loads(textresponse)
    currency = responsedata["currency"]
    assert currency == "rub"


# Поиск билетов с учётом класса обслуживания
@allure.feature("API Tests for Aviasales")
@allure.title("Search directions with class of service")
@allure.description("Поиск билетов с учётом класса обслуживания")
@allure.severity(allure.severity_level.NORMAL)
def test_find_tickets_with_ticket_class():
    params = {
        "currency": "rub",
        "origin": "MOW",
        "destination": "KZN",
        "period_type": "year",
        "page": "1",
        "limit": "30",
        "show_to_affiliates": "true",
        "sorting": "price",
        "trip_class": "1",
        "token": token,
    }
    Aviasales_Api = AviasalesApi(BaseUri)
    resp = Aviasales_Api.get_latest_prices(params)
    textresponse = resp.text
    responsedata = json.loads(textresponse)
    currency = responsedata["currency"]
    assert currency == "rub"


# НЕГАТИВНЫЕ ТЕСТЫ
# Поиск билетов с не корректной датой 2025-02-30 - 30 февраля
@allure.feature("API Tests for Aviasales")
@allure.title("Negative Scenario. Search by not correct date")
@allure.description("Поиск билетов с не корректной датой 30 февраля")
@allure.severity(allure.severity_level.NORMAL)
def test_not_correct_date():
    notcorretdate = "2025-02-30"
    params = {
        "currency": "rub",
        "origin": "MOW",
        "destination": "KZN",
        "departure_at": notcorretdate,
        "trip_class": "1",
        "token": token,
    }
    Aviasales_Api = AviasalesApi(BaseUri)
    resp = Aviasales_Api.get_prices_for_dates(params)
    textresponse = resp.text
    responsedata = json.loads(textresponse)
    status = responsedata["status"]
    assert status == 400


# Поиск билетов с не существующим аэропортом
@allure.feature("API Tests for Aviasales")
@allure.title("Negative Scenario. Search by not correct airline")
@allure.description("Поиск билетов с не существующим аэропортом")
@allure.severity(allure.severity_level.NORMAL)
def test_not_correct_airline():
    params = {
        "currency": "rub",
        "origin": "XYI",
        "destination": "KZN",
        "departure_at": "2024-09-29",
        "token": token,
    }
    Aviasales_Api = AviasalesApi(BaseUri)
    resp = Aviasales_Api.get_latest_prices(params)
    textresponse = resp.text
    responsedata = json.loads(textresponse)
    status = responsedata["status"]
    assert status == 400


# Поиск без обязательных параметров
@allure.feature("API Tests for Aviasales")
@allure.title("Negative Scenario. Search by not correct date")
@allure.description("Кейс с не заполненными обязательными параметрами")
@allure.severity(allure.severity_level.NORMAL)
def test_without_requid_params():
    params = {"currency": "rub", "departure_at": "2024-09-29", "token": token}
    Aviasales_Api = AviasalesApi(BaseUri)
    resp = Aviasales_Api.get_latest_prices(params)
    textresponse = resp.text
    responsedata = json.loads(textresponse)
    status = responsedata["status"]
    assert status == 400
