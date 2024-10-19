from selenium.webdriver.common.by import By
import time

class FlightPage:
    def __init__(self, driver):
        self.driver = driver
        self.drop_down_options=(By.XPATH,"//div[@class='journey_price-currency'][1]//span[@class='price text-space-gap']")
        self.basic_fare_button = (By.XPATH, "//div[contains(@aria-label, 'Click to select basic fare')][2]//button[contains(@class, 'fare_button')]//div[@class='fare_button_label']")
        self.continue_basic=(By.XPATH,"//div[@class='cro-button cro-no-accept-upsell-button']")
        self.confirm_fligth=(By.XPATH,"//button[1]//span[contains(text(),' Continuar ')]")

    def select_basic_fare(self):

        self.driver.find_element(*self.drop_down_options).click()
        time.sleep(5)
        self.driver.find_element(*self.basic_fare_button).click()

        try:
            self.driver.find_element(*self.continue_basic).click()
        except:
            print("No aparecio")

        time.sleep(5)        
        self.driver.find_element(*self.confirm_fligth).click()
        
        