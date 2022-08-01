"""Login Page Module"""
from .base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    """class for work with main page"""
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def find_search_field(self):
        """find search field"""
        return self.is_element_present(*MainPageLocators.FIND_FIELD)

    def input_text_to_search(self, text):
        """inputting text to searching field"""
        self.input_text_to_element(*MainPageLocators.FIND_FIELD, text)

    def find_suggest(self):
        """find suggest"""
        return self.is_element_present(*MainPageLocators.SUGGEST)

    def click_enter(self):
        """find button "Найти" and then click"""
        self.click_to_element(*MainPageLocators.BTN_FIND)
