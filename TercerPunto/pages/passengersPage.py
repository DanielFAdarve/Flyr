from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from utils.helpers import wait_for_element, wait_for_clickable_element, scroll_up,wait_for_elements,form_fill_input
import time

class PassengersPage:
    def __init__(self, driver):
        self.driver = driver

        #Informacion del pasajero
        self.passenger_gender="//div[contains(@class, 'passenger_data_group_item') and .//span[contains(text(),'{}')]]//button[contains(@id,'IdPaxGender')]"
        self.passenger_gender_selection="(//div[contains(@class, 'passenger_data_group_item')]//button[@role='option' and .//span[contains(text(),'{}')] ])"

        self.passenger_firstname="//div[contains(@class, 'passenger_data_group_item') and .//span[contains(text(),'{}')]]//input[contains(@id,'IdFirstName')]"
        self.passenger_lastname="//div[contains(@class, 'passenger_data_group_item') and .//span[contains(text(),'{}')]]//input[contains(@id,'IdLastName')]"
        
        
        self.passenger_birthday_day_button="//div[contains(@class, 'passenger_data_group_item') and .//span[contains(text(),'{}')]]//button[contains(@id,'dateDayId_IdDateOfBirth')]"
        self.passenger_birthday_day_selection="//div[contains(@class, 'passenger_data_group_item')]//button[@role='option' and contains(@id,'dateDayId_IdDateOfBirth') and .//span[text()='{}'] ]"
        
        self.passenger_birthday_month_button="//div[contains(@class, 'passenger_data_group_item') and .//span[contains(text(),'{}')]]//button[contains(@id,'dateMonthId_IdDateOfBirth')]"
        self.passenger_birthday_month_selection="//div[contains(@class, 'passenger_data_group_item')]//button[@role='option' and contains(@id,'dateMonthId_IdDateOfBirth') and .//span[text()='{}'] ]"
        
        self.passenger_birthday_year_button="//div[contains(@class, 'passenger_data_group_item') and .//span[contains(text(),'{}')]]//button[contains(@id,'dateYearId_IdDateOfBirth')]"
        self.passenger_birthday_year_selection="//div[contains(@class, 'passenger_data_group_item')]//button[@role='option' and contains(@id,'dateYearId_IdDateOfBirth') and .//span[text()='{}'] ]"
        
        self.passenger_nacionality="//div[contains(@class, 'passenger_data_group_item') and .//span[contains(text(),'{}')]]//button[contains(@id,'IdDocNationality')]"
        self.passenger_nacionality_selection="//div[contains(@class,'passenger_data_group_item') and .//span[contains(text(),'{}')] and .//button[contains(@id,'IdDocNationality')]]//button[not(contains(@style,'display:none')) and .//span[contains(text(),'{}')]]"

        #Titular Reserva
        self.phone_prefix= (By.XPATH,"//button[@id='phone_prefixPhoneId']")
        self.phone_zone= "//button[contains(@id,'phone_prefixPhoneId')]//span[contains(text(),'{}')]"
        self.phone_number= (By.XPATH,"//input[contains(@id,'phone_phoneNumberId')]")

        self.mail = (By.XPATH,"//input[contains(@id,'email')]")

        #Confirmar
        self.check_one=(By.XPATH,"//input[@id='acceptNewCheckbox']")
        self.check_two=(By.XPATH,"//input[@id='sendNewsLetter']")
        self.submit_button = (By.XPATH, "(//div[contains(text(),'Continuar') and contains(@class,'button')])[2]")

    def fill_passenger_details(self, passengers_info):
        for passenger in passengers_info:
            
            #Ingresar el Genero
            drop_down_gender = self.passenger_gender.format(passenger['type'])
            wait_for_element(self.driver, By.XPATH, drop_down_gender).click()

            gender_selection= self.passenger_gender_selection.format(passenger['gender'])
            print(gender_selection)
            wait_for_element(self.driver, By.XPATH, gender_selection).click()

            #Ingresar el nombre
            add_passenger_name = self.passenger_firstname.format(passenger['type'])
            input_name_field= wait_for_element(self.driver, By.XPATH, add_passenger_name,10)
            form_fill_input(input_name_field,passenger['first_name'])
            
            #Ingresar el apellido
            add_passenger_last_name = self.passenger_lastname.format(passenger['type'])
            input_name_field=wait_for_element(self.driver, By.XPATH, add_passenger_last_name)
            form_fill_input(input_name_field,passenger['last_name'])
            

            #Ingresar la fecha de nacimiento
            add_passenger_birthday_day_button = self.passenger_birthday_day_button.format(passenger['type'])
            wait_for_element(self.driver, By.XPATH, add_passenger_birthday_day_button).click()

            add_passenger_birthday_day = self.passenger_birthday_day_selection.format(int(passenger['date'].split('-')[0]))
            wait_for_element(self.driver, By.XPATH, add_passenger_birthday_day).click()
            
            add_passenger_birthday_month_button = self.passenger_birthday_month_button.format(passenger['type'])
            wait_for_element(self.driver, By.XPATH, add_passenger_birthday_month_button).click()

            add_passenger_birthday_month = self.passenger_birthday_month_selection.format(int(passenger['date'].split('-')[1]))
            wait_for_element(self.driver, By.XPATH, add_passenger_birthday_month).click()
            
            add_passenger_birthday_year_button = self.passenger_birthday_year_button.format(passenger['type'])
            wait_for_element(self.driver, By.XPATH, add_passenger_birthday_year_button).click()

            add_passenger_birthday_year = self.passenger_birthday_year_selection.format(int(passenger['date'].split('-')[2]))
            wait_for_element(self.driver, By.XPATH, add_passenger_birthday_year).click()
            
            #Ingresar la nacionalidad
            add_passenger_nationality_button=self.passenger_nacionality.format(passenger['type'])
            wait_for_element(self.driver, By.XPATH, add_passenger_nationality_button).click()

            add_passenger_nationality=self.passenger_nacionality_selection.format(passenger['type'],passenger['nacionality'])
            wait_for_element(self.driver, By.XPATH, add_passenger_nationality).click()
            
    

    def fill_reservation_owner(self,country,phone_number,mail):
        #Prefijo del Telefono
        wait_for_element(self.driver,*self.phone_prefix).click()
        phone_zone_button=self.phone_zone.format(country)
        wait_for_element(self.driver, By.XPATH, phone_zone_button).click()

        #Numero de telefono
        input_name_field=wait_for_element(self.driver, *self.phone_number)
        form_fill_input(input_name_field,phone_number)
        
        #Correo
        input_name_field=wait_for_element(self.driver, *self.mail)
        form_fill_input(input_name_field,mail)
        
    def submit_passenger_info(self):
        
        wait_for_element(self.driver,*self.check_one).click()
        wait_for_element(self.driver,*self.check_two).click()
        wait_for_element(self.driver,*self.submit_button).click()
