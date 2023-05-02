from driver.browser import Browser
from driver.chrome_browser import ChromeBrowser
from driver.firefox_browser import FirefoxBrowser

class BrowserFactory:
    def __init__(self):
        self.last_browser = None

    def get_browser(self, name: str) -> Browser:
        if name == 'chrome':
            return ChromeBrowser()
        elif name == 'firefox':
            return FirefoxBrowser()
        else:
            raise Exception('wrong browser name')

our_browser_factory = BrowserFactory()

chrome = our_browser_factory.get_browser('chrome')
ff = our_browser_factory.get_browser('firefox')
print()
