from selenium.webdriver.common.by import By
import time
import allure
from pages.main_page import MainPage  # Импортируем наш Page Object


### Тест 1: Открытие сайта и проверка его загрузки
@allure.title("Открытие сайта")
@allure.description("Открытие сайта и проверка его загрузки")
@allure.severity(allure.severity_level.CRITICAL)
def test_open_aviasales_site(browser):
        with allure.step("Проверили отображение названия загруженного сайта - Авиасейлс"):
            assert "Авиасейлс" in browser.title, "Сайт не загружен корректно"


### Тест 2: Проверка валидации форм
@allure.title("Проверка валидации формы")
@allure.description("Тест проверяет отображение ошибок валидации при пустых полях")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_validation(browser):
    main_page = MainPage(browser)
    main_page.click_submit_button()
    error_messages = main_page.get_error_messages()

    with allure.step("Проверили, что количество сообщений об ошибке > 0"):
        assert len(error_messages) > 0, "Ошибки валидации не отображаются"


### Тест 3: Заполнение формы поиска
@allure.title("Заполнение формы поиска")
@allure.description("Тест проверяет отображение заполненных полей")
@allure.severity(allure.severity_level.CRITICAL)
def test_fill_search_form(browser):
    main_page = MainPage(browser)
    main_page.sendkeys_destination_input("Москва")
    main_page.sendkeys_start_end_date_field("04.02.2025", "15.02.2025")


    with allure.step("Выполнили проверку заполненных значений"):
        assert main_page.get_dist_value() == "Москва"
        assert main_page.get_date_from() == "4 февраля, вт"
        assert main_page.get_date_to() == "15 февраля, сб"


### Тест 4: Поиск билетов
@allure.title("Поиск билетов")
@allure.description("Выполнить поиск билетов")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_tickets(browser):
    main_page = MainPage(browser)
    main_page.sendkeys_destination_input("Стамбул")
    main_page.sendkeys_start_end_date_field("01.02.2025", "05.02.2025")
    main_page.click_submit_button()
    results = main_page.get_results()
    assert len(results) > 0, "Результаты поиска не отображаются"


### Тест 5: Заглушки для навигации по сайту
@allure.title("Заглушки для навигации по сайту")
@allure.description("Проверка заглушек для страниц")
@allure.severity(allure.severity_level.CRITICAL)
def test_navigation_buttons(browser):
    main_page = MainPage(browser)
    main_page.show_all_places()
    main_page.click_hotels_button()

    assert "Здесь бронируют балдёжные отели" in browser.title, "Избранное в Авиасейлс"