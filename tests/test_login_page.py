import pytest

from tests.test_base import BaseTest
from config.test_data import TestData
from utilities.errors import *
from utilities.assertion import Assert


class TestLoginPage(BaseTest):

    def setup(self):
        super().setup()
        self.login_page.load_page()

    @pytest.mark.test
    @pytest.mark.filterwarnings('ignore::RuntimeWarning')
    @pytest.mark.priority_0
    def test_login_page(self):
        Assert.assert_true(self.login_page.is_page_loaded(), "Login page not loaded so cannot proceed")
        print("Login page successfully loaded")

    @pytest.mark.priority_1
    def test_invalid_email(self):
        try:
            self.login_page.sign_in(TestData.INVALID_USERNAME, TestData.INVALID_PASSWORD)
            raise Exception("Sign in has passed with invalid email")
        except InvalidEmailError:
            pass

    @pytest.mark.priority_2
    def test_invalid_password(self):
        try:
            self.login_page.sign_in(TestData.INVALID_USERNAME, TestData.INVALID_PASSWORD)
            raise Exception("Sign in has passed with wrong password")
        except InvalidPasswordError:
            pass

    @pytest.mark.priority_3
    def valid_login(self):
        try:
            self.login_page.sign_in(TestData.VALID_USERNAME,TestData.VALID_PASSWORD)
        except InvalidLoginError:
            raise Exception("Username name or password is invalid")

