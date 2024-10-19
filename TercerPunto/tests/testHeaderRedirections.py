import unittest
import time
from selenium import webdriver
from pages.homePage import HomePage
from utils.printer import Printer

console=Printer()

class TestHeaderRedirections(unittest.TestCase):

    def setUp(self):
        # Setup for WebDriver
        self.driver = webdriver.Chrome()  # or any browser driver
        self.driver.get("https://www.avianca.com/")  # URL of the application
        self.home_page = HomePage(self.driver)


    def test_language_change(self):
        
        home_page = HomePage(self.driver)

        #Controlamos Cookies y ventanas que puede aparecer
        home_page.control_cookies()
        home_page.close_header()
        
        home_page.get_header_redirections()

        # self.home_page.select_pos("Argentina")
        console.printInfoColor("testHeaderRedirections","Pruebas segun el resultado esperado")
        

    def tearDown(self):

        # Teardown para cerrar el navegador
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
