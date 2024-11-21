import logging

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

logging.basicConfig(
    filename='log_file2q.log',
    level = logging.DEBUG,
    format ='%(asctime)s:%(levelname)s:%(message)s'
)

import time

try:
    driver = webdriver.Chrome(executable_path='D:/pythonProject6/src/utils/chromedriver.exe')
    logging.info('driveri shevqmenit')
    driver.get('https://e-school.ge/?')
    time.sleep(1)
    logging.info('web gverdi gaixsna')
    driver.find_element(By.ID,'urname').send_keys('tap@gmail.com')
    logging.info('gavagzavnet username')
    print(driver.title)
    assert 'E-School Login' in driver.title
    logging.info('namdvilad E-school Login aris title')
    print(5/0)
    driver.find_element(By.ID,'urpass').send_keys('123')
    logging.info('gavagzavnet password')

    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[1]/div[2]/div/form/div/div[3]/input').click()
    logging.info('davlogindit')
except NoSuchElementException as e:

    logging.error(f'aq moxda {e}')

except AssertionError:
    logging.info('ar yopila E-school Login')

except:
    logging.info('sxva erorr amovida')

finally:
    driver.quit()