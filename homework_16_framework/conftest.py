from time import sleep

import pytest
from selenium.webdriver import Chrome
from homework_16_framework.pages.dashboard import Dashboard


@pytest.fixture(scope='session')
def driver():
    driver = Chrome("drivers/chromedriver")
    driver.maximize_window()

    driver.get("https://www.yakaboo.ua/")
    sleep(0.5)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def dashboard(driver):
    yield Dashboard(driver)

