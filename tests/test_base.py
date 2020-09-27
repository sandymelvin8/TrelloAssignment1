import pytest
from utilities.web_page_helper import WebPageHelper
from pages.login_page import LoginPageFactory
from pages.home_page import HomePageFactory
from pages.boards_page import BoardsPageFactory

from selenium.common.exceptions import SessionNotCreatedException, WebDriverException


class BaseTest:

    def setup(self):
        self.web_page_helper = WebPageHelper()
        try:
            self.web_page_helper.set_driver("chrome")
        except SessionNotCreatedException:
            raise Exception("Something wrong with the chromedriver version or file")
        except WebDriverException:
            raise Exception("Chrome driver not in path, put your driver in chromdriver folder in this folder")
        pfm = 'US'
        self.login_page = LoginPageFactory.get_page(pfm=pfm, web_page_helper=self.web_page_helper)
        self.home_page = HomePageFactory.get_page(pfm=pfm, web_page_helper=self.web_page_helper)
        self.boards_page = BoardsPageFactory.get_page(pfm=pfm, web_page_helper=self.web_page_helper)
        self.screenshot_helper = None

    def teardown(self):
        self.web_page_helper.close()
