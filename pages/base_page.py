"""Base Page Module"""
from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    """base class for all pages"""
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """open page"""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """find element on page"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def input_text_to_element(self, how, what, text):
        """input text to element"""
        inp_text = self.browser.find_element(how, what)
        inp_text.send_keys(text)

    def click_to_element(self, how, what):
        """click to element"""
        element = self.browser.find_element(how, what)
        element.click()
