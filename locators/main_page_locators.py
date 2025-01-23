from selenium.webdriver.common.by import By

class MainPageLocators:
    DESTINATION_INPUT = (By.ID, "avia_form_destination-input")
    START_DATE_FIELD = (By.XPATH, "//button[@data-test-id='start-date-field']")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 's__mKolDTwVaUL0fYyF_xuI')]")
    SUBMIT_BUTTON = (By.XPATH, "//button[@data-test-id='form-submit']")
    END_DATE_FIELD = (By.XPATH, "//div[@data-test-id='end-date-value']")
    HOTELS_BUTTON = (By.XPATH, "//div[@class='s__WJBFOjXpaWb4CntP5Bga s__OB5rgHcUTJnLSaY3AAI5 s__HrVnNfqeMvwHldrpXROu s__JvoYkPCB88widi_F4bcq' and text()='Избранное']")
    SHOW_ALL_PLACES_BUTTON = (By.XPATH, "//div[@class='s__WJBFOjXpaWb4CntP5Bga s__OB5rgHcUTJnLSaY3AAI5 s__HrVnNfqeMvwHldrpXROu' and text()='Короче']")
    RESULTS = (By.CSS_SELECTOR, "[data-test-id='search_results']")