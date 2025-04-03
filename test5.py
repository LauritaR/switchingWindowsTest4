from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(scope='function', autouse=True)
def setup_and_teardown():
    service = Service('chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

@pytest.fixture(scope='class', autouse=True)
def setup_and_teardown_class():
    service = Service('chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

@pytest.fixture(scope='module', autouse=True)
def setup_and_teardown_module():
    service = Service('chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

@pytest.fixture(scope='session', autouse=True)
def setup_and_teardown_session():
    service = Service('chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def fill_registration_form(driver, registration_url):
    driver.get(registration_url)
    try:
        driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input').send_keys('Robotas')
        driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input').send_keys('Robotauskas')
        driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input').send_keys('robotas.robotauskas@mif.stud.vu.lt')
        driver.find_element(By.XPATH, '/html/body/div/form/div[2]/div[1]/input').send_keys('+37061234567')
        driver.find_element(By.XPATH, '/html/body/div/form/div[2]/div[2]/input').send_keys('Didlaukio g. 59, Vilnius')
        driver.find_element(By.XPATH, '/html/body/div/form/button').click()
    except NoSuchElementException:
            return False
    return True

class TestRegistrationFunction:
    def test_registration1(self, setup_and_teardown):
        driver = setup_and_teardown
        fill_registration_form(driver, "http://suninjuly.github.io/registration1.html")
        success_text =  WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.TAG_NAME,'h1'))
        ).text
        assert success_text == 'Congratulations! You have successfully registered!'

    def test_registration2(self, setup_and_teardown):
        driver = setup_and_teardown
        fill_registration_form(driver, "http://suninjuly.github.io/registration2.html")
        success_text =  WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.TAG_NAME,'h1'))
        ).text
        assert success_text == 'Congratulations! You have successfully registered!'

class TestRegistrationClass:
    def test_registration1(self, setup_and_teardown_class):
        driver = setup_and_teardown_class
        fill_registration_form(driver, "http://suninjuly.github.io/registration1.html")
        success_text =  WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.TAG_NAME,'h1'))
        ).text
        assert success_text == 'Congratulations! You have successfully registered!'

    def test_registration2(self, setup_and_teardown_class):
        driver = setup_and_teardown_class
        fill_registration_form(driver, "http://suninjuly.github.io/registration2.html")
        success_text =  WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.TAG_NAME,'h1'))
        ).text
        assert success_text == 'Congratulations! You have successfully registered!'

class TestRegistrationModule:
    def test_registration1(self, setup_and_teardown_module):
        driver = setup_and_teardown_module
        fill_registration_form(driver, "http://suninjuly.github.io/registration1.html")
        success_text =  WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.TAG_NAME,'h1'))
        ).text
        assert success_text == 'Congratulations! You have successfully registered!'

    def test_registration2(self, setup_and_teardown_module):
        driver = setup_and_teardown_module
        fill_registration_form(driver, "http://suninjuly.github.io/registration2.html")
        success_text =  WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.TAG_NAME,'h1'))
        ).text
        assert success_text == 'Congratulations! You have successfully registered!'

class TestRegistrationSession:
    def test_registration1(self, setup_and_teardown_session):
        driver = setup_and_teardown_session
        fill_registration_form(driver, "http://suninjuly.github.io/registration1.html")
        success_text =  WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.TAG_NAME,'h1'))
        ).text
        assert success_text == 'Congratulations! You have successfully registered!'

    def test_registration2(self, setup_and_teardown_session):
        driver = setup_and_teardown_session
        fill_registration_form(driver, "http://suninjuly.github.io/registration2.html")
        success_text =  WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.TAG_NAME,'h1'))
        ).text
        assert success_text == 'Congratulations! You have successfully registered!'
