from config.test_data import TestData
from pages.login_page import LoginPage
from pages.page_base import PageBase
from selenium.common.exceptions import NoSuchElementException

from utilities.errors import NoCreateButtonError


class HomePageFactory:

    @staticmethod
    def get_page(pfm, web_page_helper):
        return HomePage(pfm, web_page_helper)


class HomePage(PageBase):

    CREATE_NEW_BOARD = "//button[@data-test-id='header-boards-menu-create-board']"
    ADD_BOARD_TITLE = "//input[@aria-label='Add board title']"
    CREATE_BOARD_BUTTON = "//button[@data-test-id='create-board-submit-button']"

    def __init__(self, pfm, web_page_helper):
        super().__init__(pfm, web_page_helper)
        self.loginpage = LoginPage(pfm, web_page_helper=web_page_helper)

    def load_page(self):
        self.web_page_helper.go_to_url(TestData.BASE_URL)

    def is_page_loaded(self):
        home_icon = self.boards_icon(wait_time=10)
        home_icon.is_displayed()
        return True

    def is_create_button_visible(self):
        verify_button = self.web_page_helper.find_element_by_xpath(self.CREATE_BOARD_BUTTON)
        verify_button.is_enabled()
        return True

    def create_new_board(self, boardname):
        try:
            self.boards_icon(wait_time=10)
            self.web_page_helper.find_element_by_xpath(self.CREATE_NEW_BOARD)
            self.web_page_helper.click_element()
            self.web_page_helper.find_element_by_xpath(self.ADD_BOARD_TITLE)
            self.web_page_helper.click_element()
            self.web_page_helper.send_text(boardname)
            self.web_page_helper.find_element_by_xpath(self.CREATE_BOARD_BUTTON)
            self.web_page_helper.click_element()
        except NoSuchElementException:
            raise NoSuchElementException("Create Button Unavailable")







