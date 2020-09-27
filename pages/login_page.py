from config.test_data import TestData
from pages.page_base import PageBase
from selenium.common.exceptions import NoSuchElementException
from utilities.errors import InvalidEmailError, InvalidPasswordError


class LoginPageFactory:

    @staticmethod
    def get_page(pfm, web_page_helper):
        if pfm == 'US':
            return USLoginPage(pfm, web_page_helper)
        elif pfm == 'UK':
            return UKLoginPage(pfm, web_page_helper)
        else:
            return LoginPage(pfm, web_page_helper)


class LoginPage(PageBase):

    EMAIL_ID = 'user'
    PASSWORD = 'password'
    LOGIN_WITH_ATLASSIAN = 'login'
    LOGIN_BUTTON = 'login-submit'
    SUBMIT_BUTTON = 'login'
    HOME_ICON = 'sc-bdVaJa kBFJig'

    def __init__(self, pfm, web_page_helper):
        super().__init__(pfm, web_page_helper)

    def load_page(self):
        self.web_page_helper.go_to_url(TestData.BASE_URL)

    def is_page_loaded(self):
        try:
            self.web_page_helper.find_element_by_class('trello-main-logo')
            return True
        except NoSuchElementException:
            return False

    def sign_in(self, email, password):
        self.web_page_helper.go_to_url(TestData.BASE_URL)
        self.web_page_helper.find_element_by_id(self.EMAIL_ID, timeout=3)
        self.web_page_helper.send_text(email)
        if self._is_password_box_visible():
            raise InvalidEmailError("Invalid Email")
        try:
            self.web_page_helper.find_element_by_id(self.PASSWORD, timeout=2)
            self.web_page_helper.send_text(password)
        except InvalidPasswordError:
            raise InvalidPasswordError("Invalid Password")

        return True

    def _is_password_box_visible(self):
        self.web_page_helper.find_element_by_id(self.PASSWORD, timeout=2)
        return True

    def wait_for_sign_in_complete(self, wait_time=20):
        """

        :param wait_time:
        :return:
        """
        try:
            self.web_page_helper.find_element_by_class(self.HOME_ICON, timeout=wait_time)
            self.web_page_helper.is_element_present(self.HOME_ICON)
            return True
        except NoSuchElementException:
            return False


class USLoginPage(LoginPage):

    def __init__(self, pfm, web_page_helper):
        super().__init__(pfm, web_page_helper)


class UKLoginPage(LoginPage):

    def __init__(self, pfm, web_page_helper):
        super().__init__(pfm, web_page_helper)
