from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def wait_for_element(driver, by, value, timeout=10):
    wait_for_hidde_page_loader(driver)
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

def wait_for_clickable_element(driver, by, value, timeout=10):
    wait_for_hidde_page_loader(driver)
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))

def wait_for_hidde_page_loader(driver):
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "page-loader"))
    )

#Para obtener todos los elementos
def wait_for_elements(driver, by, value, timeout=10):
    wait_for_hidde_page_loader(driver)
    return WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located((by, value)))

def wait_for_clickable_elements(driver, by, value, timeout=10):
    wait_for_hidde_page_loader(driver)
    return WebDriverWait(driver, timeout).until(EC.visibility_of_all_elements_located((by, value)))

def scroll_up(driver, pixels=100):
    driver.execute_script(f"window.scrollBy(0, -{pixels});")

def remove_tildes(text):
    # Diccionario de reemplazos de tildes
    replacements = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'ñ': 'n', 'Ñ': 'N'
    }

    # Reemplaza cada tilde en la cadena
    for accented_char, unaccented_char in replacements.items():
        text = text.replace(accented_char, unaccented_char)
    
    return text
