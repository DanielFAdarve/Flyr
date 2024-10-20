import unittest
import time
from selenium import webdriver
from pages.homePage import HomePage
from utils.printer import Printer

console=Printer()

class TestLanguageChange(unittest.TestCase):
    def setUp(self):
        # Setup for WebDriver
        self.driver = webdriver.Chrome()  # or any browser driver
        self.driver.get("https://www.avianca.com/")  # URL of the application
        self.home_page = HomePage(self.driver)
        self.driver.maximize_window()


    def test_language_change(self):
        
        #Idiomas junto con el valor que se espera de un objeto
        languages = {
            'Español': ['Buscar','es'],  
            'English': ['Search','en'],      
            'Português': ['Buscar voos','pt'],   
            'Français': ['Rechercher','fr'] 
        }

        #Controlamos Cookies y ventanas que puede aparecer
        self.home_page.control_cookies()
        self.home_page.close_header()
        
        #Ciclo para recorrer cada idioma, y validar que el objeto tenga el valor esperado
        for lang, (expected_text,expected_text_local_storage) in languages.items():
            with self.subTest(lang=lang):
                self.home_page.select_language(lang)
                self.assertTrue(self.home_page.verify_language_change(expected_text,expected_text_local_storage),
                                f"Language change to {lang} failed.")

        console.printInfoColor("testLanguageChange","Pruebas segun el resultado esperado")
        

    def tearDown(self):
        # Teardown para cerrar el navegador
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
