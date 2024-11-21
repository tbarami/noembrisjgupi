
from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import configparser

#assert shemowmeba tu gvinda

@pytest.fixture()
def data():
    return {'a':1,'b':2}

def test_case(data):
    assert data['a'] == 1


@pytest.mark.parametrize('login,password', [(1,2),(3,4)])
def test_login(login,password):
    assert login + 1 == password


#@pytest.mark.skip()
@pytest.mark.skip(reason='არ არის ფუნქციონალი შექმნილი')
def test_case2(data):
    assert data['a'] == 1

@pytest.mark.xfail(reson = 'რაიმე ბაგი გვაქვს რაც აფეილებს ტესტ ქეისს')
def test_case3(data):
    assert data['a'] == 5




brauzerebi = ['chrome','firefox','edge']

@pytest.fixture(params=brauzerebi)
def browser(request):
    #dasawyisi
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'edge':
        driver = webdriver.Edge()
    else:
        raise ValueError("არც ქრომია არც ფაიერფოქსი არც ედჯი")
    yield driver
    #bolo
    driver.quit()

def test_google(browser):
    browser.get('https://www.google.com')
    assert 'Google' in browser.title





def test_login(browser):
    username = browser.find_element(By.ID,'urname')
    password = browser.find_element(By.ID,'urpass')

    username.send_keys("teacher@gmail.com")
    password.send_keys('123')

    login_button = browser.find_element(By.XPATH,'//input[@value="ავტორიზაცია2"]')
    login_button.click()

    element = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/a/div[1]')

    assert '2' in element.text



#@pytest.fixture(scope='module')
@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://e-school.ge')
    yield driver
    driver.quit()

def config_reading():
    config = configparser.ConfigParser()
    config.read('D:/pythonProject6/configfile.ini')
    list2 = []
    for key in config['credential']:
        user = config['credential'][key]
        username, password, class_count = user.split(':')
        list2.append((username, password, class_count))
    return list2



@pytest.mark.parametrize('username,password,class_count', config_reading())
def test_login(browser,username,password,class_count):
    element_username = browser.find_element(By.ID,'urname')
    element_password = browser.find_element(By.ID,'urpass')
    element_username.send_keys(username)
    element_password.send_keys(password)
    wait = WebDriverWait(browser,30)
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="ავტორიზაცია"]')))
    login_button.click()
    element = \
        (browser.find_element \
         (By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/a/div[1]'))
    #WebDriverWait(browser,30).until(EC.text_to_be_present_in_element(element))
    #browser.implicitly_wait(1)
    assert class_count in element.text















