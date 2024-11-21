from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def send_keys(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.send_keys(text)

    def click(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()


