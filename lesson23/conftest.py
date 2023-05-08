from selenium.webdriver import Chrome
from lesson23.pages.dashboard import Dashboard

import pytest


@pytest.fixture(scope="session")
def driver():
    driver = Chrome('lesson23/drivers/chromedriver.exe')
    driver.get("https://epicentrk.ua/")

    yield driver

    driver.quit()


@pytest.fixture
def dashboard(driver):
    yield Dashboard(driver)
