from selenium.webdriver.common.by import By

class ServicesPage:
    def __init__(self, driver):
        self.driver = driver
        self.continue_button = (By.ID, "continue-without-services")

    def skip_services(self):
        self.driver.find_element(*self.continue_button).click()
