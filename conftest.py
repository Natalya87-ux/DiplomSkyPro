import pytest
from selenium import webdriver
from config import BASE_URL
import allure

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Инициализация драйвера
    driver.maximize_window()

    with allure.step("Открытие браузера"):
        driver.get(BASE_URL) # Переход на базовый URL
    yield driver  # Возвращает драйвер тесту
    driver.quit()  # Закрывает браузер после теста