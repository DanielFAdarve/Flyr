from selenium.webdriver.common.by import By
from utils.helpers import wait_for_element
import time

class ServicesPage:
    def __init__(self, driver):
        self.driver = driver
        self.continue_button = (By.XPATH, "//div[@class='page_buttons']//button[span[contains(text(),'Continuar')] and not(contains(@sytle,'display: none!important;'))][2]")
        self.next=(By.XPATH,"//div[@class='terciary-button']")
        self.service_lounge=(By.XPATH,"//button[@id='serviceButtonTypeBusinessLounge']")
        self.confirm_service=(By.XPATH,"//button//span[contains(text(),'Confirmar')]")
    def control_window(self):
        try:
            wait_for_element(self.driver,*self.next).click()
        except:
            print("No aparece ventaja emergente ")


    def skip_services(self):
        wait_for_element(self.driver,*self.continue_button,20).click()
        self.control_window()

    def add_service_lounge(self):
        wait_for_element(self.driver,*self.service_lounge,15).click()
        time.sleep(4)
         
        try:
            confirm_button = wait_for_element(self.driver, *self.confirm_service, 15)
            confirm_button.click()
        except Exception as e:
            self.driver.execute_script("arguments[0].click();", confirm_button)

        confirm_button = wait_for_element(self.driver, *self.confirm_service, 15)
        confirm_button.click()
        wait_for_element(self.driver,*self.continue_button,15).click()
        self.control_window()
