from selenium import  webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def get_driver(browser_name):
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(executable_path='D:/pythonProject6/src/utils/chromedriver.exe')

    elif browser_name == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise ValueError(f"browseri ar iyo arc firefox arc chrome")

    driver.maximize_window()
    return driver
