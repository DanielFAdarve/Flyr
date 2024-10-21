from selenium.webdriver.common.by import By
from utils.helpers import wait_for_element, wait_for_clickable_element, scroll_up,wait_for_elements
import time
class SeatmapPage:
    def __init__(self, driver):
        self.driver = driver
        self.seat_map="//li[contains(@class,'{}')]//button[not(contains(@class,'unavailable'))]"
        self.select_individual_seat = "//li[contains(@class,'{}')]//button[not(contains(@class,'unavailable'))]//span[contains(text(),'{}')]"

    
    def select_seat(self,seat_class):
        
        time.sleep(5)
        #Obtenemos los asientos disponibles
        seats=  self.seat_map.format(seat_class)
        seats_vailable = wait_for_elements(self.driver,By.XPATH, seats,15)
        available_seats = []
        for item in seats_vailable:
            if item.text !='':
                available_seats.append(item.text)
        
        #Seleccionamos el asiento
        select_seat=  self.select_individual_seat.format(seat_class,available_seats[0].replace('Asiento:\n',''))
        wait_for_clickable_element(self.driver,By.XPATH, select_seat,15).click()
        