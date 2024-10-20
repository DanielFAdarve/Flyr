import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.printer import Printer
from utils.localStorage import SessionStorage
from utils.helpers import wait_for_element, wait_for_clickable_element, scroll_up

consola = Printer()

class HomePage:
    def __init__(self, driver):
        self.group_name = "HomePage"
        self.driver = driver

        # Cookies y ventanas
        self.accept_cookies = (By.ID, "onetrust-accept-btn-handler")
        self.close_top_advice = (By.ID, "nsAlertButton")

        # Idioma
        self.language_dropdown = (By.CLASS_NAME, "dropdown_trigger_inner")
        self.language_option = "//span[contains(text(),'{}')]"
        self.language_verification_element = (By.XPATH, "//button[@type='submit'][2]")
        self.language_verification_element_dos="//button[@type='submit'][1]"
        # País
        self.pos_dropdown = (By.ID, "pointOfSaleSelectorId")
        self.pos_option = "//button//span[contains(text(),'{}') and @class='points-of-sale_list_item_label']"
        self.pos_confirm_selection = (By.XPATH, "//button[@class='button points-of-sale_footer_action_button']")
        self.pos_verification_element = "//button[contains(@id,'pointOfSaleSelectorId')]"

        # Selección del Viaje
        self.one_way = (By.ID, "journeytypeId_1")
        self.date = (By.ID, "departureInputDatePickerId")
        self.origin_button = (By.ID, "originBtn")
        self.origin_input = (By.XPATH, '//input[@aria-label="Search.DepartureArrivalFocusInfo"]')
        self.destination_button = (By.ID, "arrivalStationInputLabel")
        self.destination_input = (By.CSS_SELECTOR, 'input[placeholder="Hacia"]')
        self.passenger_button = (By.CSS_SELECTOR, 'button[aria-label^="Pasajeros"]')
        self.add_passenger_button = (By.CLASS_NAME, "ui-num-ud_button")
        self.count_passenger = (By.CLASS_NAME, "ui-num-ud_input")
        self.confirm_passenger = (By.XPATH, "//button[.//span[text()='Confirmar']]")
        self.search_button = (By.XPATH, "//button[2][@type='submit']//span[text()=' Buscar ']")

    def open_language_dropdown(self):
        wait_for_clickable_element(self.driver, *self.language_dropdown).click()

    def select_language(self, language):
        self.open_language_dropdown()
        lang_option_xpath = self.language_option.format(language)
        wait_for_clickable_element(self.driver, By.XPATH, lang_option_xpath).click()

    def select_pos(self, pos):
        wait_for_clickable_element(self.driver, *self.pos_dropdown).click()
        pos_option_xpath = self.pos_option.format(pos)
        wait_for_clickable_element(self.driver, By.XPATH, pos_option_xpath).click()
        wait_for_clickable_element(self.driver, *self.pos_confirm_selection).click()

    def select_one_way(self):
        wait_for_clickable_element(self.driver, *self.one_way).click()
        consola.printComment("homePage-select_one_way", "Se seleccionó correctamente el botón de solo ida")

    def select_flight_details(self, origin, destination):
        wait_for_clickable_element(self.driver, *self.origin_button).click()
        origin_input = wait_for_clickable_element(self.driver, *self.origin_input)
        origin_input.send_keys(origin)
        origin_input.send_keys(Keys.ENTER)

        destination_input = wait_for_clickable_element(self.driver, *self.destination_input)
        destination_input.send_keys(destination)
        destination_input.send_keys(Keys.ENTER)

    def select_passengers(self, max_passengers=1):
        wait_for_clickable_element(self.driver, *self.passenger_button).click()
        buttons = self.driver.find_elements(*self.add_passenger_button)

        for index, button in enumerate(buttons):
            try:
                if index < max_passengers:
                    button.click()
                else:
                    break
            except Exception as e:
                consola.printWarnColor(f"homePage-select_passengers", f"No se pudo agregar el pasajero {index + 1}: {str(e)}")
        
        wait_for_clickable_element(self.driver, *self.confirm_passenger).click()

    def search_flights(self):
        wait_for_clickable_element(self.driver, *self.search_button).click()

    def control_cookies(self):
        try:
            wait_for_clickable_element(self.driver, *self.accept_cookies).click()
            consola.printComment("homePage-controlCookies", "Cookies aceptadas correctamente")
        except Exception:
            consola.printWarnColor("homePage-controlCookies", "No se encontró el botón de aceptar cookies")

    def close_header(self):
        try:
            wait_for_clickable_element(self.driver, *self.close_top_advice).click()
            consola.printComment("homePage-close_header", "Advertencia superior cerrada correctamente")
        except Exception:
            consola.printWarnColor("homePage-close_header", "No se encontró la advertencia superior")

    def verify_language_change(self, expected_text,expected_local_storage):
        actual_text = wait_for_element(self.driver, *self.language_verification_element,15).text
        local_storage_value = self.get_local_storage_pos('page_view', 'language_nav')
        return (actual_text == expected_text and local_storage_value==expected_local_storage)

    def get_local_storage_pos(self, key, item):
        session_storage = SessionStorage(self.driver)
        pos_info = json.loads(session_storage.__getitem__(key))
        return pos_info['_value'][item]

    def get_selected_pos(self):
        current_pos = wait_for_element(self.driver, By.XPATH, self.pos_verification_element)
        return current_pos.text

    def verify_pos_change(self, expected_text):
        scroll_up(self.driver, 200)
        actual_text = self.get_selected_pos()
        local_storage_value = self.get_local_storage_pos('pointOfSale', 'name')
        return expected_text in actual_text and expected_text == local_storage_value

    def test(self):
        wait_for_clickable_element(self.driver, *self.date).click()
