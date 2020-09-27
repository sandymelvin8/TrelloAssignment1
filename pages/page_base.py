"""
page base
"""
from config.test_data import TestData
from selenium.common.exceptions import NoSuchElementException


class PageBase:

    MORE = "'//button[@aria-label='Switch to...']'"
    HOME_ICON = "//a[@aria-label='Back to Home']//span[@role='img']"
    BOARDS = "//button[@aria-label='Open Boards Menu']"
    CREATE_BOARD = "//button[@aria-label='Create Board or Team']"
    INFO_ICON = "//button[@aria-label='Open Information Menu']"
    NOTIFICATION = "//button[@aria-label='Notifications']"
    MEMBER = "//button[@aria-label='Open Member Menu']"

    def __init__(self, pfm, web_page_helper):
        self.web_page_helper = web_page_helper
        self.base_url = TestData.BASE_URL

    def more_icon(self, wait_time=10):
        try:
            self.web_page_helper.find_element_by_xpath(self.MORE, wait_time)
            self.web_page_helper.is_element_present(self.MORE)
            self.web_page_helper.click_element()
            return True
        except NoSuchElementException:
            raise False

    def home_icon(self, wait_time=10):
        try:
            self.web_page_helper.find_element_by_xpath(self.HOME_ICON, wait_time)
            self.web_page_helper.is_element_present(self.HOME_ICON)
            self.web_page_helper.click_element()
            return True
        except NoSuchElementException:
            raise False

    def boards_icon(self, wait_time=10):
        try:
            self.web_page_helper.find_element_by_xpath(self.BOARDS, wait_time)
            self.web_page_helper.is_element_present(self.BOARDS)
            self.web_page_helper.click_element()
            return True
        except NoSuchElementException:
            return False

    def create_board_icon(self, wait_time=10):
        try:
            self.web_page_helper.find_element_by_xpath(self.CREATE_BOARD, wait_time)
            self.web_page_helper.is_element_present(self.CREATE_BOARD)
            self.web_page_helper.click_element()
            return True
        except NoSuchElementException:
            raise False
