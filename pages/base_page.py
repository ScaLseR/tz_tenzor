"""Base Page Module"""
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    """base class for all pages"""
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """opens the page"""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """finds an element on the page"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def input_text_to_element(self, how, what, text):
        """enter text into an element"""
        inp_text = self.browser.find_element(how, what)
        inp_text.send_keys(text)

    def click_to_element(self, how, what):
        """click on element"""
        element = self.browser.find_element(how, what)
        element.click()

    def find_element(self, how, what):
        """finds the link of the first element in the search results"""
        element = self.browser.find_element(how, what)
        return element

    def go_to_new_window(self):
        """go to new window in browser"""
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)

    def get_page_url(self):
        """get current url"""
        return self.browser.current_url
