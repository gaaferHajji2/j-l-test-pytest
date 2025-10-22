from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import time

@pytest.fixture(scope='session')
def get_driver_and_wait():
    service = Service(executable_path='chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=0.5)

    yield driver, wait

    time.sleep(2)

    driver.close()