from src.Pages.basepage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    username = (By.ID,'urname')
    userpass = (By.ID,'urpass')
    login_button = (By.XPATH,'//input[@value="ავტორიზაცია"]')

    def enter_username(self,username):
        self.send_keys(self.username,username)

    def enter_password(self, password):
        self.send_keys(self.username, password)

    def click_login(self):
        self.click(self.login_button)

    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

