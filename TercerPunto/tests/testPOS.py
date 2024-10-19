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


    def test_language_change(self):
        
        #Paises junto con el valor que se espera de un objeto
        pos = {
            'Argentina': 'Argentina',  
            'España': 'España',      
            'Chile': 'Chile'
        }


        #Controlamos Cookies y ventanas que puede aparecer
        self.home_page.control_cookies()
        self.home_page.close_header()
        

        #Ciclo para recorrer cada pais, y validar que el objeto tenga el valor esperado
        for country, expected_text in pos.items():
            with self.subTest(country=country):

                console.printComment("textPOS",f"Entro a seleccionar el Pais: {country}")
                self.home_page.select_pos(country)
                time.sleep(5)
                
                self.assertTrue(self.home_page.verify_pos_change(expected_text),
                                f"Language change to {country} failed.")

        # self.home_page.select_pos("Argentina")
        console.printInfoColor("testPOS","Pruebas segun el resultado esperado")
        

    def tearDown(self):

        # Teardown para cerrar el navegador
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
