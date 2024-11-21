import csv
import pytest
import src.utils.config_reader
import src.utils.driver
import src.Pages.login_page
def data():
    location = 'D:/pythonProject6/src/recources/login_pass.csv'
    with open(location,'r') as file:
        obj = csv.DictReader(file, delimiter='\t')
        return [row for row in obj]
@pytest.fixture()
def setup(request):
    config = src.utils.config_reader.get_config()
    driver = src.utils.driver.get_driver(config['browser'])
    driver.get(config['base_url'])
    request.cls.driver = driver
    yield driver
    driver.quit()



@pytest.mark.usefixtures('setup')
class TestLogin:
    @pytest.mark.parametrize("data", data())
    def test_login(self,data):
        login_page = src.Pages.login_page.LoginPage(self.driver)
        login_page.login(data['username'],data['password'])



