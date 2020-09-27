import pytest

from tests.test_base import BaseTest
from config.test_data import TestData
from utilities.errors import *
from utilities.assertion import Assert


class TestHomePage(BaseTest):

    def setup(self):
        super().setup()
        self.login_page.sign_in(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        self.home_page.load_page()

    @pytest.mark.test
    def test_home_page(self):
        Assert.assert_true(self.boards_page.is_page_loaded(), "Login page not loaded so cannot proceed")
        print("Login page successfully loaded")

    def test_create_board(self):
        try:
            self.home_page.create_new_board(TestData.BOARD_NAME)
            Assert.assert_equals(TestData.BOARD_NAME,self.boards_page.is_page_loaded(), 'Board Name mismatch')
        except NoCreateButtonError:
            raise NoCreateButtonError("No create button available")
