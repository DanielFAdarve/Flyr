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
        home_page = HomePage(self.driver)
        home_page.control_cookies()
        home_page.close_header()
        
        #Valida el idioma
        home_page.select_language("Español")

        #Selecciona el POS
        home_page.select_pos('Colombia')
        home_page.close_header()
              #Informacion de Pruebas
        passengers_info=[
            {
                "type":"Adulto",
                "gender":"Masculino",
                "first_name":"Daniel",
                "last_name":"Adarve",
                "date":"04-12-2003",
                "nacionality":"Colombia"
            },
            {
                "type":"Bebé",
                "gender":"Femenino",
                "first_name":"Laura",
                "last_name":"Valencia",
                "date":"06-09-2024",
                "nacionality":"Colombia"
            },{
                "type":"Joven",
                "gender":"Masculino",
                "first_name":"Manuel",
                "last_name":"Cardona",
                "date":"04-12-2011",
                "nacionality":"Colombia"
            },
            {   "type":"Niño",
                "gender":"Masculino",
                "first_name":"David",
                "last_name":"Cardona",
                "date":"04-12-2015",
                "nacionality":"Colombia"
            }
            
            ]
        #Seleccionar el vuelo, los pasajeros y buscar el vuelo
        home_page.select_one_way()
        home_page.select_flight_details("Bogota", "Barranquilla")
        
        #Agregamos los pasajeros
        # home_page.select_passengers()
        home_page.open_passenger_selection()
        home_page.add_passenger_count("2")
        home_page.add_passenger_count("3")
        home_page.add_passenger_count("4")

        home_page.search_flights()
        time.sleep(5)

        # Flight Page
        print("Seleccionar Viaje")
        flight_page = FlightPage(self.driver)
        flight_page.select_basic_fare()
        flight_page.confirm_flight()
      
        # Passengers Page
        passengers_page = PassengersPage(self.driver)

        time.sleep(10)

        passengers_page.fill_passenger_details(passengers_info)
        passengers_page.fill_reservation_owner("Colombia","3235043212","soplefox23@gmail.com")
        passengers_page.submit_passenger_info()
        time.sleep(20)

        # Services Page
        services_page = ServicesPage(self.driver)
        services_page.skip_services()
       
        # Seatmap Page
        seatmap_page = SeatmapPage(self.driver)
        

        seatmap_page.select_seat('economy')
        seatmap_page.select_seat('economy')
        seatmap_page.select_seat('economy')
        seatmap_page.select_seat('economy')
        seatmap_page.go_to_pay()
        
    
        # Payment Page
        payment_page = PaymentPage(self.driver)
        
        time.sleep(20)
        payment_page.fill_payment_details("daniel@gmail.com", "carrera 25", "manizales","Colombia")
    
    def tearDown(self):
        self.driver.quit()
        

if __name__ == "__main__":
    unittest.main()
