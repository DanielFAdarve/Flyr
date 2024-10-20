import unittest
from selenium import webdriver
from pages.homePage import HomePage
from utils.printer import Printer
from utils.helpers import remove_tildes
console = Printer()

class TestHeaderRedirections(unittest.TestCase):

    def setUp(self):

        # Setup for WebDriver
        self.driver = webdriver.Chrome()  # or any browser driver
        self.driver.get("https://www.avianca.com/")  # URL of the application
        self.driver.maximize_window()
        self.home_page = HomePage(self.driver)

    def test_nav_redirection(self):
        home_page = self.home_page

        # Controlamos Cookies y ventanas que pueden aparecer
        home_page.control_cookies()
        home_page.close_header()
        # Valida el idioma
        home_page.select_language("Español")

        # Usamos un conjunto para evitar duplicados
        used_options = set()

        for _ in range(3):  # Ejecutamos la prueba 3 veces
            # Obtenemos una seccion aleatoria del nav
            footer_option = home_page.get_random_footer_option()

            # Aseguramos que la footer_option no se ha utilizado y se excluye articulos restringidos
            while footer_option in used_options and footer_option != 'Artículos restringidos':
                footer_option = home_page.get_random_footer_option()
            used_options.add(footer_option)  

            # Seleccionamos el link
            home_page.select_footer_option(footer_option)

            current_url = home_page.get_url()
            
            #controlamos las tiles, los espacios  y que el texto este en minuscula
            footer_option_url=remove_tildes(footer_option).replace(' ','-').lower()
            
            #Controlamos el unico link que no usa la particula 'de'
            if 'politica-de-privacidad' in footer_option_url:
                footer_option_url=footer_option_url.replace('-de','')

            assert 'es' in current_url and  footer_option_url in current_url, f"La parte {footer_option_url} no se encontro dentro de la URL: {current_url}"
            console.printInfoColor("testFooter", "Pruebas según el resultado esperado")
            
            home_page.return_home_page()

    def tearDown(self):
        # Teardown para cerrar el navegador
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
