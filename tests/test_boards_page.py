import pytest

from tests.test_base import BaseTest
from config.test_data import TestData
from utilities.assertion import Assert


class TestLoginPage(BaseTest):

    def setup(self):
        super().setup()
        self.login_page.sign_in(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        self.boards_page.load_page()

    @pytest.mark.test
    @pytest.mark.usefixtures
    @pytest.mark.priority_0
    def test_boards_page(self):
        Assert.assert_true(self.boards_page.is_page_loaded(), "Boards page not loaded so cannot proceed")
        print("Boards page successfully loaded")

    @pytest.mark.priority_1
    def test_do_stuff(self):
        try:
            self.boards_page.search_board(TestData.BOARD_NAME)
            self.boards_page.create_not_started()
            self.boards_page.create_in_progress()
            self.boards_page.create_qa()
            self.boards_page.create_done()
            self.boards_page.create_cards()
            self.boards_page.move_card2_to_in_progress()
            self.boards_page.move_card3_to_qa()
            self.boards_page.move_card2_to_qa()
            self.boards_page.assign_card_to_current_user(TestData.NAME)
            self.boards_page.comment_on_card(TestData.COMMENT)
        except Exception as e:
            print(e)






