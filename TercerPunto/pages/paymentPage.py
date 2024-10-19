from selenium.webdriver.common.by import By

class PaymentPage:
    def __init__(self, driver):
        self.driver = driver
        self.card_number_input = (By.ID, "card-number")
        self.expiry_date_input = (By.ID, "expiry-date")
        self.cvv_input = (By.ID, "cvv")
        self.pay_button = (By.ID, "pay-button")

    def fill_payment_details(self, card_number, expiry_date, cvv):
        self.driver.find_element(*self.card_number_input).send_keys(card_number)
        self.driver.find_element(*self.expiry_date_input).send_keys(expiry_date)
        self.driver.find_element(*self.cvv_input).send_keys(cvv)

    def submit_payment(self):
        self.driver.find_element(*self.pay_button).click()
