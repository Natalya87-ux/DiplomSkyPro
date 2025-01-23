from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
import allure

from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def click_destination_input(self):
        self.wait_and_find_element(MainPageLocators.DESTINATION_INPUT).click()

    def click_start_date_field(self):
        self.wait_and_find_element(MainPageLocators.START_DATE_FIELD).click()

    with allure.step("Выполнено нажатие кнопки Найти билеты"):
        def click_submit_button(self):
            self.wait_and_find_element(MainPageLocators.SUBMIT_BUTTON).click()

    with allure.step("Проверка, что появляется сообщение об ошибке"):
        def get_error_messages(self):
            return self.wait_and_find_element(MainPageLocators.ERROR_MESSAGE).text

    with allure.step("Заполнили форму 'куда'"):
        def sendkeys_destination_input(self, value):
            self.wait_and_find_element(MainPageLocators.DESTINATION_INPUT).send_keys(value + Keys.RETURN)
    with allure.step("Заполнили форму 'туда' и форму 'обратно'"):
        def sendkeys_start_end_date_field(self, start_date, end_date):
            self.wait_and_find_element(MainPageLocators.START_DATE_FIELD).click()
            modal_element = self.wait_and_find_element((By.CSS_SELECTOR, "[data-test-id='dropdown']"))

            self.driver.execute_script("arguments[0].scrollIntoView(true);", modal_element)

            start_date = (By.CSS_SELECTOR, f"[data-test-id='date-{start_date}']")
            end_date = (By.CSS_SELECTOR, f"[data-test-id='date-{end_date}']")
            self.wait_and_find_element(start_date).click()
            self.wait_and_find_element(end_date).click()

    with allure.step("Нажатие на кнопку 'показать все места'"):
        def show_all_places(self):
            self.wait_and_find_element(MainPageLocators.SHOW_ALL_PLACES_BUTTON).click()

    with (allure.step("Нажатие на кнопку 'Отели'")):
        def click_hotels_button(self):
            self.wait_and_find_element(MainPageLocators.HOTELS_BUTTON).click()

    with allure.step("Блок с результатами поиска отображается"):
        def get_results(self):
           return self.wait_and_find_element(MainPageLocators.RESULTS)

    with allure.step("Получение данных из поля 'Куда'"):
        def get_dist_value(self):
            return self.wait_and_find_element(MainPageLocators.DESTINATION_INPUT).get_attribute("value")

    with allure.step("Получение данных из поля 'Дата с'"):
        def get_date_from(self):
            return self.wait_and_find_element(MainPageLocators.START_DATE_FIELD).text

    with allure.step("Получение данных из поля 'Дата По'"):
        def get_date_to(self):
            return self.wait_and_find_element(MainPageLocators.END_DATE_FIELD).text
