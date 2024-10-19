import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utils.printer import Printer
from selenium.webdriver.common.keys import Keys

consola = Printer()
class HomePage:
    def __init__(self, driver):

        self.group_name="HomePage"
        self.driver = driver

        #Cookies y ventanas
        self.accept_cookies=(By.ID,"onetrust-accept-btn-handler")
        self.close_top_advice=(By.ID,"nsAlertButton")

        #Lenguague
        self.language_dropdown = (By.CLASS_NAME, "dropdown_trigger_inner")
        self.language_option="//span[contains(text(),'{}')]"
        self.language_verification_element = (By.XPATH, "//button[@type='submit'][1]")

        #Seleccion del Viaje
        self.one_way=(By.ID,"journeytypeId_1")
        self.date = (By.ID,"departureInputDatePickerId")
        self.origin_button=(By.ID,"originBtn")
        self.origin_input = (By.XPATH, '//input[@aria-label="Search.DepartureArrivalFocusInfo"]')
        self.destination_button = (By.ID,"arrivalStationInputLabel")
        self.destination_input = (By.CSS_SELECTOR, 'input[placeholder="Hacia"]')
        self.passenger_button = (By.CSS_SELECTOR, 'button[aria-label^="Pasajeros"]')
        self.add_passenger_button=(By.CLASS_NAME, "ui-num-ud_button")
        self.count_passenger=(By.CLASS_NAME, "ui-num-ud_input")
        self.confirm_passenger=(By.XPATH,"//button[.//span[text()='Confirmar']]")
        self.search_button = (By.XPATH, "//button[2][@type='submit']//span[text()=' Buscar ']")

    def open_dropdown(self):
        self.driver.find_element(*self.language_dropdown).click()
    

    def select_language(self, language):

        self.open_dropdown()
        lang_option_xpath = self.language_option.format(language)  # Usamos format() en la cadena
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, lang_option_xpath)))
        self.driver.find_element(By.XPATH, lang_option_xpath).click()


    def select_one_way(self):
        self.driver.find_element(*self.one_way).click()
        # consola.printComment(f"homePage-select_one_way",f"Se selecciono correctamente el boton de solo ida")

    def select_flight_details(self, origin, destination):
        
        self.driver.find_element(*self.origin_button).click()
        self.driver.find_element(*self.origin_input).send_keys(origin)
        self.driver.find_element(*self.origin_input).send_keys(Keys.ENTER)

        self.driver.find_element(*self.destination_input).send_keys(destination)
        self.driver.find_element(*self.destination_input).send_keys(Keys.ENTER)

    def select_passengers(self):
        self.driver.find_element(*self.passenger_button).click()
                

  
        buttons = self.driver.find_elements(*self.add_passenger_button)
        for index, button in enumerate(buttons):
            try:
                button.click()
        
            except Exception as e:
                print(f"No se pudo agregar el pasajero {index + 1}: {str(e)}")
                continue  # Continúa con el siguiente botón si ocurre un error
        
        self.driver.find_element(*self.confirm_passenger).click()

        # time.sleep(100)


    # def select_passengers(self):
    #     # Hacer clic en el botón de pasajeros
    #     self.driver.find_element(*self.passenger_button).click()

    #     # Encontrar todos los botones para agregar pasajeros
    #     buttons = self.driver.find_elements(*self.add_passenger_button)
        
    #     # Encontrar el campo que cuenta el número de pasajeros
    #     passenger_count_element = self.driver.find_element(*self.count_passenger)
    #     current_passenger_count = int(passenger_count_element.get_attribute("value")) if passenger_count_element.get_attribute("value") else 0

    #     for index, button in enumerate(buttons):
    #         try:
    #             # Si el contador de pasajeros es menor que el límite (ej. 1)
    #             if current_passenger_count < 1:
    #                 if index > 0:  # Evitar agregar con el primer botón
    #                     button.click()
    #                     print(f"Se agregó pasajero {index + 1}")
    #                     current_passenger_count += 1  # Incrementar el contador manualmente
    #             else:
    #                 print("No se puede agregar más pasajeros, ya se alcanzó el límite.")
    #                 break  # Salir del bucle si se ha alcanzado el límite
    #         except Exception as e:
    #             print(f"No se pudo agregar el pasajero {index + 1}: {str(e)}")
    #             continue  # Continúa con el siguiente botón si ocurre un error

    #     time.sleep(100)
        
    def search_flights(self):
        self.driver.find_element(*self.search_button).click()
        # time.sleep(100)

    def control_cookies(self):
        try:
            self.driver.find_element(*self.accept_cookies).click()
            consola.printInfoColor(f"homePage-controlCookies",f"Existia el elemento de las cookies y se cerro segun lo esperado")
        except KeyError :
            consola.printWarnColor(f"homePage-controlCookies","No existia el boton de aceptar Cookies")
            

    def close_header(self):
        try:
            self.driver.find_element(*self.close_top_advice).click()
            consola.printInfoColor(f"homePage-close_header",f"Existia el elemento de la parte superior")
        except:
            consola.printWarnColor(f"homePage-close_header","No existia el elemento de la parte superior")

    def verify_language_change(self, expected_text):
        # Espera explícita hasta que el mensaje de bienvenida esté visible
        actual_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.language_verification_element)).text
        return actual_text == expected_text
    
    def test(self):
        self.driver.find_element(*self.date).click()