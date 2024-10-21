from selenium.webdriver.common.by import By
from utils.helpers import wait_for_clickable_element,wait_for_element
import time

class FlightPage:
    def __init__(self, driver):
        self.driver = driver
        self.drop_down_options = (By.XPATH, "//div[@class='journey_price-currency'][1]//span[@class='price text-space-gap']")
        self.drop_down_return_options = (By.XPATH, "//div[@class='journey-select_container'][1]//button[contains(@class,'journey_price_button')]//span[contains(text(),'Desde')]")
        self.basic_fare_button = (By.XPATH, "//div[contains(@aria-label, 'Click to select basic fare')][2]//button[contains(@class, 'fare_button')]//div[@class='fare_button_label']")
        self.basic_flex_button = (By.XPATH, "//div[@class='journey-control']//div[contains(@class,'journey_price-currency') and .//span[@class='price text-space-gap'] and .//span[contains(text(),'Desde')]]")
        self.continue_basic = (By.XPATH, "//div[@class='cro-button cro-no-accept-upsell-button']")
        self.confirm_flight_button = (By.XPATH, "//button[1]//span[contains(text(),' Continuar ')]")

    def select_basic_fare(self):
        # Selecciona la tarifa básica
        wait_for_clickable_element(self.driver, *self.drop_down_options).click()
        time.sleep(5)
        wait_for_element(self.driver, *self.basic_fare_button).click()

        # Trata de continuar, si aparece la opción
        try:
            wait_for_element(self.driver, *self.continue_basic).click()
        except:
            print("No apareció la opción de continuar con la tarifa básica")

        time.sleep(5)

    def select_return_basic_flex(self):
        # Selecciona la tarifa básica flexible
        wait_for_clickable_element(self.driver, *self.drop_down_return_options).click()
        time.sleep(5)
        wait_for_clickable_element(self.driver, *self.basic_flex_button).click()

        # Trata de continuar, si aparece la opción
        try:
            wait_for_clickable_element(self.driver, *self.continue_basic).click()
        except:
            print("No apareció la opción de continuar con la tarifa flexible")

    def confirm_flight(self):
        # Confirmar vuelo
        wait_for_clickable_element(self.driver, *self.confirm_flight_button).click()