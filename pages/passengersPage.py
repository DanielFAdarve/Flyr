from selenium.webdriver.common.by import By

class PassengersPage:
    def __init__(self, driver):
        self.driver = driver

        self.passenger_gender=(By.XPATH,"//div[@class='passenger_data_block' and .//h4[contains(text(), ' Adulto 1: ')]]//div[@class='ui-form_controls']//div[contains(text(),'Género*')]")
        self.passenger_firstname=(By.XPATH,"//div[@class='passenger_data_block' and .//h4[contains(text(), ' Adulto 1: ')]]//div[@class='ui-form_controls']//div[contains(text(),'Género*')]")
        self.passenger_lastname=(By.XPATH,"//div[@class='passenger_data_block' and .//h4[contains(text(), ' Adulto 1: ')]]//div[@class='ui-form_controls']//div[contains(text(),'Género*')]")
        self.passenger_birthday_day=(By.XPATH,"//div[@class='passenger_data_block' and .//h4[contains(text(), ' Adulto 1: ')]]//div[@class='ui-form_controls']//div[contains(text(),'Género*')]")
        self.passenger_birthday_month=(By.XPATH,"//div[@class='passenger_data_block' and .//h4[contains(text(), ' Adulto 1: ')]]//div[@class='ui-form_controls']//div[contains(text(),'Género*')]")
        self.passenger_birthday_year=(By.XPATH,"//div[@class='passenger_data_block' and .//h4[contains(text(), ' Adulto 1: ')]]//div[@class='ui-form_controls']//div[contains(text(),'Género*')]")
        self.passenger_nacionality=(By.XPATH,"//div[@class='passenger_data_block' and .//h4[contains(text(), ' Adulto 1: ')]]//div[@class='ui-form_controls']//div[contains(text(),'Género*')]")


        self.submit_button = (By.ID, "submit-passengers")

    def fill_passenger_details(self, passengers_info):
        for passenger in passengers_info:
            
            self.driver.find_element(*self.passenger_gender).send_keys(passenger['gender'])
            self.driver.find_element(*self.passenger_firstname).send_keys(passenger['name'])
            self.driver.find_element(*self.passenger_lastname).send_keys(passenger['lastname'])
            self.driver.find_element(*self.passenger_birthday_day).send_keys(int(passenger['date'].split('-')[0]))
            self.driver.find_element(*self.passenger_birthday_month).send_keys(int(passenger['date'].split('-')[1]))
            self.driver.find_element(*self.passenger_birthday_year).send_keys(int(passenger['date'].split('-')[2]))
            self.driver.find_element(*self.passenger_nacionality).send_keys(passenger['nacionality'])



    def submit_passenger_info(self):
        self.driver.find_element(*self.submit_button).click()
