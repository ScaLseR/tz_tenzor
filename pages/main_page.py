"""Login Page Module"""
from .base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    """class for work with main page"""
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def find_search_field(self):
        """finds the search field"""
        return self.is_element_present(*MainPageLocators.FIND_FIELD)

    def input_text_to_search(self, text):
        """enters text in the search field"""
        self.input_text_to_element(*MainPageLocators.FIND_FIELD, text)

    def find_suggest(self):
        """finds suggest"""
        return self.is_element_present(*MainPageLocators.SUGGEST)

    def click_enter(self):
        """finds the 'Найти' button and then clicks on it"""
        self.click_to_element(*MainPageLocators.BTN_FIND)

    def first_link(self):
        """finds the first link in the search results"""
        first_element = self.find_element(*MainPageLocators.FIRST_ELEMENT)
        link = first_element.get_attribute('href')
        return link

    def find_picture_link(self):
        """finds links to pictures"""
        return self.is_element_present(*MainPageLocators.PICTURE_LINK)

    def click_to_picture_link(self):
        """ click to the pictures link"""
        self.click_to_element(*MainPageLocators.PICTURE_LINK)
