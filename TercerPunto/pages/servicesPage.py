from selenium.webdriver.common.by import By
from utils.helpers import wait_for_element

class ServicesPage:
    def __init__(self, driver):
        self.driver = driver
        self.continue_button = (By.XPATH, "//div[@class='page_buttons']//button[span[contains(text(),'Continuar')] and not(contains(@sytle,'display: none!important;'))][2]")
        self.next=(By.XPATH,"//div[@class='terciary-button']")
    def skip_services(self):
        wait_for_element(self.driver,*self.continue_button).click()
        wait_for_element(self.driver,*self.next).click()