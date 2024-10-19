from selenium.webdriver.common.by import By

class SeatmapPage:
    def __init__(self, driver):
        self.driver = driver
        self.economy_seat_button = (By.XPATH, "//button[contains(text(),'Economy')]")

    def select_economy_seat(self):
        self.driver.find_element(*self.economy_seat_button).click()
