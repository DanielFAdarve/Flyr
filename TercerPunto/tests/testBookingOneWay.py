import unittest
import time
from selenium import webdriver
from pages.homePage import HomePage
from pages.flightPage import FlightPage
from pages.passengersPage import PassengersPage
from pages.servicesPage import ServicesPage
from pages.seatmapPage import SeatmapPage
from pages.paymentPage import PaymentPage

class BookingTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.avianca.com/")
        self.driver.maximize_window()
        # time.sleep(10)

    def test_booking_one_way(self):
        # Home Page
        print("HomePage")
        home_page = HomePage(self.driver)
        # home_page.test()
        home_page.control_cookies()
        home_page.close_header()
        
        #Valida el idioma
        # home_page.select_language("Español")

        #Seleccionar el vuelo, los pasajeros y buscar el vuelo
        home_page.select_one_way()
        home_page.select_flight_details("Bogota", "Barranquilla")
        home_page.select_passengers() 
        home_page.search_flights()
        time.sleep(15)

        # Flight Page
        print("Seleccionar Viaje")
        flight_page = FlightPage(self.driver)
        flight_page.select_basic_fare()

      
        # Passengers Page
        passengers_page = PassengersPage(self.driver)

        #Informacion de Pruebas
        passengers_info=[
            {
                "gender":"Masculino",
                "first_name":"Daniel",
                "last_name":"Adarve",
                "date":"04-12-2024",
                "nacionality":"Colombia"
            },
            {
                "gender":"Masculino",
                "first_name":"Daniel",
                "last_name":"Adarve",
                "date":"04-12-2024",
                "nacionality":"Colombia"
            },
            {
                "gender":"Masculino",
                "first_name":"Daniel",
                "last_name":"Adarve",
                "date":"04-12-2024",
                "nacionality":"Colombia"
            },
            {
                "gender":"Masculino",
                "first_name":"Daniel",
                "last_name":"Adarve",
                "date":"04-12-2024",
                "nacionality":"Colombia"
            },
            {
                "gender":"Masculino",
                "first_name":"Daniel",
                "last_name":"Adarve",
                "date":"04-12-2024",
                "nacionality":"Colombia"
            },
            ]

        passengers_page.fill_passenger_details(passengers_info)
        passengers_page.submit_passenger_info()

        # Services Page
        services_page = ServicesPage(self.driver)
        services_page.skip_services()

        # Seatmap Page
        seatmap_page = SeatmapPage(self.driver)
        seatmap_page.select_economy_seat()

        # Payment Page
        payment_page = PaymentPage(self.driver)
        payment_page.fill_payment_details("4111111111111111", "12/25", "123")
        payment_page.submit_payment()

    # def tearDown(self):
    #     self.driver.quit()
        

if __name__ == "__main__":
    unittest.main()
