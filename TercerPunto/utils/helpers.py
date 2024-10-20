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

def scroll_up(driver, pixels=100):
    driver.execute_script(f"window.scrollBy(0, -{pixels});")