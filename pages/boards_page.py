import time

from selenium.common.exceptions import NoSuchElementException

from config.test_data import TestData
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.page_base import PageBase


class BoardsPageFactory:

    @staticmethod
    def get_page(pfm, web_page_helper):
        return BoardsPage(pfm, web_page_helper)


class BoardsPage(PageBase):

    def __init__(self, pfm, web_page_helper):
        super().__init__(pfm, web_page_helper)
        self.login_page = LoginPage(pfm,web_page_helper=web_page_helper)
        self.home_page = HomePage(pfm,web_page_helper=web_page_helper)

    def load_page(self):
        self.web_page_helper.go_to_url(TestData.BASE_URL)

    def is_page_loaded(self):
        try:
            search = self.web_page_helper.find_element_by_xpath(self.BOARDS_PAGE_VERIFIER)
            if search.is_displayed():
                print("Element displayed")

        except NoSuchElementException:
            raise NoSuchElementException("checker not found")

    """Object repo for Boards Page"""
    SEARCH_TEXT = 'search-boards'
    BOARDS_PAGE_VERIFIER = "//h1[@class='js-board-editing-target board-header-btn-text']"
    ADD_LIST = "//span[contains(text(),'Add a list')]"
    LIST_NAME = "//input[@name='name']"
    ADD_LIST_BUTTON = "//input[@type='submit']"
    ADD_CARD_NAME = "//span[contains(text(),'Add a card')]"
    TEXT_AREA = "//textarea[@placeholder='Enter a title for this card…']"
    EMPTY_CLICK = "//div[@id='trello-root']"
    CARD_1 = "//span[@class='list-card-title js-card-name' and text()='Card 1']/ancestor::a"
    CARD_2 = "//span[@class='list-card-title js-card-name' and text()='Card 2']/ancestor::a"
    CARD_2_TARGET = "//textarea[contains(text(),'In Progress')]"
    CARD_3 = "//span[@class='list-card-title js-card-name' and text()='Card 3']/ancestor::a"
    CARD_3_TARGET = "//textarea[contains(text(),'QA')]"
    MEMBERS = "//div[@class='window-sidebar']/descendant-or-self::span[contains(text(),'Members')]/parent::a"
    SEARCH_MEMBERS = "//input[@class='js-search-mem js-autofocus']"
    COMMENT_AREA = "//div[@class='comment-box']/child::textarea"
    SAVE_COMMENT_BUTTON = "//div[@class='comment-box']/descendant-or-self::input[@type='submit']"
    CLOSE_COMMENT_MODAL = "//a[@class='icon-md icon-close dialog-close-button js-close-window']"

    textarea = "//h2[text()='In Progress']/ancestor::div[@class='list js-list-content']"

    def search_board(self, boardname):
        self.boards_icon(wait_time=5)
        self.web_page_helper.find_element_by_name(self.SEARCH_TEXT)
        self.web_page_helper.click_element()
        self.web_page_helper.send_text(boardname)

    def create_not_started(self):
        self.web_page_helper.find_element_by_xpath(self.ADD_LIST)
        self.web_page_helper.click_element()
        time.sleep(2)
        self.web_page_helper.find_element_by_xpath(self.LIST_NAME)
        self.web_page_helper.send_text("Not Started")
        self.web_page_helper.find_element_by_xpath(self.ADD_LIST_BUTTON)
        self.web_page_helper.click_element()

    def create_in_progress(self):
        self.web_page_helper.find_element_by_xpath(self.ADD_LIST)
        self.web_page_helper.click_element()
        time.sleep(2)
        self.web_page_helper.find_element_by_xpath(self.LIST_NAME)
        self.web_page_helper.send_text("In progress")
        self.web_page_helper.find_element_by_xpath(self.ADD_LIST_BUTTON)
        self.web_page_helper.click_element()

    def create_qa(self):
        self.web_page_helper.find_element_by_xpath(self.ADD_LIST)
        self.web_page_helper.click_element()
        time.sleep(2)
        self.web_page_helper.find_element_by_xpath(self.LIST_NAME)
        self.web_page_helper.send_text("QA")
        self.web_page_helper.find_element_by_xpath(self.ADD_LIST_BUTTON)
        self.web_page_helper.click_element()

    def create_done(self):
        self.web_page_helper.find_element_by_xpath(self.ADD_LIST)
        self.web_page_helper.click_element()
        time.sleep(2)
        self.web_page_helper.find_element_by_xpath(self.LIST_NAME)
        self.web_page_helper.send_text("Done")
        self.web_page_helper.find_element_by_xpath(self.ADD_LIST_BUTTON)
        self.web_page_helper.click_element()

    def create_cards(self):
        """Add card 1"""
        self.web_page_helper.find_element_by_xpath(self.ADD_CARD_NAME)
        self.web_page_helper.click_element()
        time.sleep(2)
        self.web_page_helper.send_text("Card 1")
        self.web_page_helper.press_enter()
        """Add card 2"""
        self.web_page_helper.send_text("Card 2")
        self.web_page_helper.press_enter()
        """Add card 3"""
        self.web_page_helper.send_text("Card 3")
        self.web_page_helper.press_enter()
        """Add card 4"""
        self.web_page_helper.send_text("Card 4")
        self.web_page_helper.press_enter()
        self.web_page_helper.find_element_by_xpath(self.EMPTY_CLICK)

    def move_card2_to_in_progress(self):
        source = self.CARD_2
        target = self.CARD_2_TARGET
        self.web_page_helper.do_drag_and_drop(source, target)

    def move_card3_to_qa(self):
        source = self.CARD_3
        target = self.CARD_3_TARGET
        self.web_page_helper.do_drag_and_drop(source, target)

    def move_card2_to_qa(self):
        source = self.CARD_2
        target = self.CARD_3_TARGET
        self.web_page_helper.do_drag_and_drop(source, target)

    def assign_card_to_current_user(self, name):
        self.web_page_helper.find_element_by_xpath(self.CARD_1)
        self.web_page_helper.click_element()
        time.sleep(3)
        self.web_page_helper.find_element_by_xpath(self.MEMBERS)
        self.web_page_helper.click_element()
        time.sleep(2)
        self.web_page_helper.find_element_by_xpath(self.SEARCH_MEMBERS)
        self.web_page_helper.click_element()
        self.web_page_helper.send_text(name)
        self.web_page_helper.press_enter()
        time.sleep(2)

    def comment_on_card(self, comment):
        self.web_page_helper.find_element_by_xpath(self.COMMENT_AREA)
        self.web_page_helper.click_element()
        self.web_page_helper.send_text(comment)
        time.sleep(2)
        self.web_page_helper.find_element_by_xpath(self.SAVE_COMMENT_BUTTON)
        self.web_page_helper.click_element()
        time.sleep(3)
        self.web_page_helper.find_element_by_xpath(self.CLOSE_COMMENT_MODAL)
        self.web_page_helper.click_element()










