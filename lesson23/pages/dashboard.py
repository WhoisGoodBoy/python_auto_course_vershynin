from lesson23.pages.base_page import BasePage
from selenium.webdriver.chrome.webdriver import  WebDriver

class Dashboard(BasePage):
    def __init__(self,driver: WebDriver):
        super().__init__(driver)
        self.__nav_bar_locator = ('xpath', "//div[@class='header__burger']")

    def click_on_navbar(self):
        element = self._wait_until_element_appears(self.__nav_bar_locator)
        element.click()

    def choose_subcategory(self,name):
        locator = ('xpath', f"//ul[@class='catalog-menu']//a[@title='{name}']")
        element = self._wait_until_element_appears(locator)
        element.click()


