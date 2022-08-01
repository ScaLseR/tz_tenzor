from .base_page import BasePage
from pages.locators import ImagePageLocators


class ImagePage(BasePage):
    """class for work with image page"""

    def open_first_category(self):
        """opens the first image category"""
        self.click_to_element(*ImagePageLocators.IMG_FST_CAT)

    def get_img_page_url(self):
        """get new page url"""
        url = self.get_page_url()
        return url[0: url.find('?')]

    def get_category_name_from_search_field(self):
        """get category name from search field"""
        category_name = self.find_element(*ImagePageLocators.FIND_FIELD).get_attribute('value')
        if len(category_name) > 0:
            return True
        return False
