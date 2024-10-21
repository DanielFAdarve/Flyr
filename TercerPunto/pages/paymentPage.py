from selenium.webdriver.common.by import By
from utils.helpers import wait_for_element, wait_for_clickable_element, wait_for_elements,form_fill_input

class PaymentPage:
    def __init__(self, driver):
        self.driver = driver
        self.card_add=(By.XPATH,"//button[@class='card-payment_add-card_button']")
        self.card_number_input = (By.ID, "card-number")
        self.expiry_date_input = (By.ID, "expiry-date")
        self.cvv_input = (By.ID, "cvv")
        self.pay_button = (By.ID, "pay-button")
        self.email=(By.XPATH,"//input[@id='email']")
        self.city=(By.XPATH,"//input[@id='city']")
        self.dropdown_country=(By.XPATH,"//button[@id='country']")
        self.country_button="//button[@role='option' and .//span[contains(text(),'{}')]]"
        self.address=(By.XPATH,"//input[@id='address']")
        self.check=(By.XPATH,"//input[@name='terms']")
        

    def fill_card_details(self, card_number, expiry_date, cvv):
        self.driver.find_element(*self.card_number_input).send_keys(card_number)
        self.driver.find_element(*self.expiry_date_input).send_keys(expiry_date)
        self.driver.find_element(*self.cvv_input).send_keys(cvv)

    def fill_payment_details(self, email, adress, city,country):
            
        #Ingresar el correo
        input_name_field= wait_for_element(self.driver, *self.email,10)
        form_fill_input(input_name_field,email)

        #ingresamos la direccion
        input_name_field= wait_for_element(self.driver, *self.address,10)
        form_fill_input(input_name_field,adress)    
            
        #ingresamos la ciudad
        input_name_field= wait_for_element(self.driver, *self.city,10)
        form_fill_input(input_name_field,city)

        #Ingresar el pais
        wait_for_element(self.driver, *self.dropdown_country).click()
        select_country = self.country_button.format(country)
        wait_for_element(self.driver, By.XPATH, select_country).click()

        wait_for_element(self.driver, *self.check).click()
        
    def submit_payment(self):
        self.driver.find_element(*self.pay_button).click()
