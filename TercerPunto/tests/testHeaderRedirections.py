import unittest
import time
import random  # Importamos random para generar opciones aleatorias
from selenium import webdriver
from pages.homePage import HomePage
from utils.printer import Printer

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
            nav_option = home_page.get_random_nav_option()

            # Aseguramos que la nav_option no se ha utilizado
            while nav_option in used_options:
                nav_option = home_page.get_random_nav_option()
            used_options.add(nav_option)  

            # Seleccionamos el desplegable
            home_page.select_nav_option(nav_option)

            # Obtenemos un item aleatorio de nav
            nav_item = home_page.get_random_nav_item(nav_option)

            # Aseguramos que la nav_item no se ha utilizado
            while (nav_option, nav_item) in used_options:
                nav_item = home_page.get_random_nav_item(nav_option)
            used_options.add((nav_option, nav_item))  # Agregamos a las opciones usadas

            home_page.select_nav_item(nav_item)
            current_url = home_page.get_url()
            print(current_url)

            # Reemplazamos espacios y caracteres no deseados en las opciones
            if "y destinos" in nav_option:
                nav_option = nav_option.replace(" y ", " ")
            if " " in nav_option or "ó" in nav_option:
                nav_option = nav_option.replace(" ", "-").replace('ó','o')
            if " " in nav_item:
                nav_item = nav_item.replace(" ", "-")
            
            expected_url = f"es/{nav_option}/{nav_item}".lower()

            assert expected_url in current_url, f"Expected URL {expected_url} not found in {current_url}"
            console.printInfoColor("testHeaderRedirections", "Pruebas según el resultado esperado")

    def tearDown(self):
        # Teardown para cerrar el navegador
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
