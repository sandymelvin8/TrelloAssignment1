"""
This module defines WebPageHelper which handles browser required operations in tests.
"""
from enum import Enum
import time
import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, SessionNotCreatedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class BrowserType(Enum):
    """
    Enum for browser type
    """
    FIRE_FOX = "firefox"
    CHROME = "chrome"


class ElementBy(Enum):
    """
    Enum for find element by
    """
    ID = "id"
    XPATH = "xpath"
    NAME = "name"
    CLASS = "class"
    LINK_TEXT = "link_text"
    TAG = "tag"


class WebPageHelper:
    """
    Class to help Web Page operation required for Trello E2E TEsts
    """

    def __init__(self):
        self.driver = None
        self.element = None

    def set_driver(self, browser_type):
        """
        Set the appropriate driver based on browser type
        :param browser_type: browser type to use
        :return: None
        """
        if browser_type == BrowserType.FIRE_FOX.value:
            self.driver = webdriver.Firefox()
        elif browser_type == BrowserType.CHROME.value:
            import platform
            if 'Window' in platform.platform():
                driver_path = os.path.join(os.getcwd(), 'chromedriver.exe')
                print(driver_path)
            else:
                driver_path = os.path.join(os.getcwd(), 'chromedriver')
            self.driver = webdriver.Chrome(executable_path=driver_path)
        else:
            raise Exception("Invalid Browser Type passed")

    def go_to_url(self, url):
        """
        Go to the url given on the browser
        :param url: url to go to
        :return: None
        """
        if not self.driver:
            raise Exception("Please set driver first")
        print("Go to %s" % url)
        self.driver.get(url)

    def _find_element(self, by, value, timeout=10):
        """
        Find element by and set found element
        :param by: ElementBy enum to choose
        :param value: value to use to find element
        :return: None
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                if by == ElementBy.ID:
                    self.element = self.driver.find_element_by_id(value)
                elif by == ElementBy.XPATH:
                    self.element = self.driver.find_element_by_xpath(value)
                elif by == ElementBy.NAME:
                    self.element = self.driver.find_element_by_name(value)
                elif by == ElementBy.CLASS:
                    self.element = self.driver.find_element_by_class_name(value)
                elif by == ElementBy.LINK_TEXT:
                    self.element = self.driver.find_element_by_link_text(value)
                elif by == ElementBy.TAG:
                    self.element = self.driver.find_element_by_tag_name(value)
                else:
                    raise Exception("Not supported find element operation")
                return
            except NoSuchElementException:
                print("Element not found yet, waiting")
                time.sleep(2)
        print("Element not found, timeout")
        raise Exception("Element with ID: {} was not found".format(value))

    def _find_all_elements(self, by, value, timeout=10):
        """
        Find element by and set found element
        :param by: ElementBy enum to choose
        :param value: value to use to find element
        :return: None
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                if by == ElementBy.ID:
                    self.element = self.driver.find_elements_by_id(value)
                elif by == ElementBy.NAME:
                    self.element = self.driver.find_elements_by_name(value)
                elif by == ElementBy.CLASS:
                    self.element = self.driver.find_elements_by_class_name(value)
                elif by == ElementBy.LINK_TEXT:
                    self.element = self.driver.find_elements_by_link_text(value)
                elif by == ElementBy.TAG:
                    self.element = self.driver.find_elements_by_tag_name(value)
                else:
                    raise Exception("Not supported find element operation")
                return
            except NoSuchElementException:
                print("Element not found yet, waiting")
                time.sleep(2)
        print("Element not found, timeout")
        raise Exception("Element with ID: {} was not found".format(value))

    def find_element_by_name(self, value, timeout=10):
        """

        :param value:
        :param timeout:
        :return:
        """
        self._find_element(ElementBy.NAME, value, timeout)

    def find_element_by_xpath(self, value, timeout=10):
        """

        :param value:
        :param timeout:
        :return:
        """
        self._find_element(ElementBy.XPATH, value, timeout)

    def find_element_by_class(self, value, timeout=10):
        """

        :param value:
        :param timeout:
        :return:
        """
        self._find_element(ElementBy.CLASS, value, timeout)

    def find_elements_by_link_text(self, value, timeout=10):
        """

        :param timeout:
        :param value:
        :return:
        """
        self._find_all_elements(ElementBy.LINK_TEXT, value, timeout)

    def find_element_by_link_text(self, value, timeout=10):
        """

        :param timeout:
        :param value:
        :return:
        """
        self._find_element(ElementBy.LINK_TEXT, value, timeout)

    def find_all_forms(self, timeout=10):
        """

        :return:
        """
        self._find_all_elements(ElementBy.TAG, 'form', timeout)

    def find_element_by_id(self, value, timeout=10):
        """

        :param timeout:
        :param value:
        :return:
        """
        self._find_element(ElementBy.ID, value, timeout)

    def click_element(self):
        """
        Click on the element found
        :return: None
        """
        if not self.element:
            raise Exception("No element is set to click on")
        self.element.click()

    def is_element_present(self, value):
        """
        Click on the element found
        :return: None

        """
        if not self.element:
            raise Exception("No element is set to find on")
        self.find_element_by_xpath(ElementBy.CLASS, value)

    def is_page_loaded(self, value):
        self.find_element_by_xpath(ElementBy.CLASS, value)

    def clear_input_box(self):
        """

        :return:
        """
        self.element.clear()

    def do_drag_and_drop(self, source, target):
        """

        :return:
        """
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    def send_text(self, text):
        """
        Send text to the element found
        :param text: text to send
        """
        if not self.element:
            raise Exception("No element is set to send text")
        self.element.send_keys(text)

    def submit(self):
        """
        submit element
        :return:
        """
        self.element.submit()

    def press_enter(self):
        """
        Hit enter key
        :return: None
        """
        self.element.send_keys(Keys.RETURN)

    def close(self):
        """
        close the driver
        :return: None
        """
        self.driver.close()
