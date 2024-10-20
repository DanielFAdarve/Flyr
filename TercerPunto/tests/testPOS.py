import unittest
import time
from selenium import webdriver
from pages.homePage import HomePage
from utils.printer import Printer

console=Printer()


class TestPOSChange(unittest.TestCase):

    def setUp(self):
        # Setup for WebDriver
        self.driver = webdriver.Chrome()  # or any browser driver
        self.driver.get("https://www.avianca.com/")  # URL of the application
        self.home_page = HomePage(self.driver)
        self.driver.maximize_window()

    def test_pos_change(self):
        
        #Paises junto con el valor que se espera de un objeto
        pos = {
            'Argentina': 'Argentina',  
            'España': 'España',      
            'Chile': 'Chile'
        }

        #Controlamos Cookies y ventanas que puede aparecer
        self.home_page.control_cookies()
        self.home_page.close_header()
        
        console.printInfoColor("testPOS","Pruebas para validar el pais por medio del un objeto y el local Storage")

        #Ciclo para recorrer cada pais, y validar que el objeto tenga el valor esperado
        for country, expected_text in pos.items():
            with self.subTest(country=country):
                console.printComment("textPOS",f"Entro a seleccionar el Pais: {country}")
                self.home_page.select_pos(country)
                time.sleep(2)
                self.home_page.close_header()
                self.assertTrue(self.home_page.verify_pos_change(expected_text),
                                f"Cambio al pais {country} fallido.")
        console.printInfoColor("testPOS","Pruebas segun el resultado esperado")
    
    def tearDown(self):
        # Teardown para cerrar el navegador
        if self.driver: 
            print("Entra al tearDown")
            self.driver.quit()
            print("Finalizo")
if __name__ == "__main__":
    test = TestPOSChange()
    test.setUp()
    try:
        test.test_pos_change()
    finally:
        test.tearDown()
