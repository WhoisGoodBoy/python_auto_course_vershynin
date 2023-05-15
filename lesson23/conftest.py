from selenium.webdriver import Chrome
from lesson23.pages.dashboard_page import Dashboard

import pytest


@pytest.fixture(scope="session")
def driver():
    driver = Chrome('lesson23/drivers/chromedriver.exe')
    driver.get("https://epicentrk.ua/")
    #for cookie in driver.get_cookies():
    #    print(cookie)
    #print(driver.get_cookie('EPIC_LANG'))
    #token_xsrf = 'XSRF-TOKEN'
    #driver.add_cookie({'name':'test', 'value':'test_value'})
    #driver.delete_all_cookies()
    #print(driver.get_cookie('test'))
    #driver.delete_cookie('test')
    driver.execute_script("window.localStorage['test'] = 'Test_value'")
    print(type(driver.execute_script("return window.localStorage['esState'];")))

    yield driver

    driver.quit()


@pytest.fixture
def dashboard(driver):
    yield Dashboard(driver)
