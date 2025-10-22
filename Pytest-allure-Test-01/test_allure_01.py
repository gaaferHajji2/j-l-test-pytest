from typing import Tuple
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure
import pytest

import time

service = Service(executable_path='chromedriver.exe')
# chrome = webdriver.Chrome(service=service)

# chrome.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

class TestOHRM:

    USERNAME_LOC = (By.XPATH, '//input[@name="username"]')

    def test_ui(self, get_driver_and_wait: Tuple[webdriver.Chrome, WebDriverWait]):
        driver, wait = get_driver_and_wait
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        t1 = wait.until(EC.presence_of_element_located(self.USERNAME_LOC))

        assert t1 is not None

    def test_login(self, get_driver_and_wait):
        pass
        # print("driver is: ", type(driver))
        # print("wait is: ", type(wait))

time.sleep(1.2)