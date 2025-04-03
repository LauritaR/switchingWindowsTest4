from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import pytest


class TestRegistration:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        service=Service('chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        yield
        self.driver.quit()
    
    def fill_registration_form(self, registration_url):
        self.driver.get(registration_url)
        try:
            self.driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input').send_keys('Robotas')
            self.driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input').send_keys('Robotauskas')
            self.driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input').send_keys('robotas.robotauskas@mif.stud.vu.lt')
            self.driver.find_element(By.XPATH, '/html/body/div/form/div[2]/div[1]/input').send_keys('+37061234567')
            self.driver.find_element(By.XPATH, '/html/body/div/form/div[2]/div[2]/input').send_keys('Didlaukio g. 59, Vilnius')
            self.driver.find_element(By.XPATH, '/html/body/div/form/button').click()
        except NoSuchElementException:
            return False
        return True
    
    def test_registration1(self):
        self.fill_registration_form("http://suninjuly.github.io/registration1.html")
        success_text = WebDriverWait(self.driver,5).until(
            EC.presence_of_element_located((By.TAG_NAME,'h1'))
        ).text
        assert success_text == 'Congratulations! You have successfully registered!'
    
    def test_registration2(self):
        self.fill_registration_form("http://suninjuly.github.io/registration2.html")
        success_text =  WebDriverWait(self.driver,5).until(
            EC.presence_of_element_located((By.TAG_NAME,'h1'))
        ).text
        assert success_text == 'Congratulations! You have successfully registered!'
    
