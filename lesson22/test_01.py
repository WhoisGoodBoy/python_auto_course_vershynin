from selenium.webdriver import Chrome, Keys
import time

def test_01():
    driver = Chrome('lesson22/drivers/chromedriver.exe')
    driver.get('https://google.com')
    search_input_field_locator = '//textarea[@title="Пошук"]'
    first_non_ad_link_locator = "//h3[contains(text(), 'Повернись живим – фонд компетентної допомоги армії ...')]/.."
    search_input_field = driver.find_element(by='xpath', value=search_input_field_locator)
    search_input_field.send_keys('Повернись живим')
    search_input_field.send_keys(Keys.ENTER)
    time.sleep(3)
    first_non_ad_link = driver.find_element(by='xpath', value=first_non_ad_link_locator)
    first_non_ad_link.click()
    time.sleep(3)
    driver.quit()
