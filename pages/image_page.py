from .base_page import BasePage
from pages.locators import ImagePageLocators
from selenium.webdriver.common.action_chains import ActionChains


class ImagePage(BasePage):
    """class for work with image page"""
    _img_name = ''

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

    def open_first_img(self):
        """opens the first image"""
        self.click_to_element(*ImagePageLocators.IMG_FST)

    def click_forward_btn(self):
        """clicks forward button"""
        self.move_focus_to_img()
        self.click_to_element(*ImagePageLocators.NEXT_BTN)

    def click_back_button(self):
        """clicks back button"""
        self.move_focus_to_img()
        self.click_to_element(*ImagePageLocators.PREV_BTN)

    def img_is_open(self):
        """check if the image is open"""
        if self.is_element_present(*ImagePageLocators.IMG_OPEN):
            if len(self._img_name) == 0:
                self._img_name = self.find_element(*ImagePageLocators.IMG_OPEN).get_attribute('src')
                print('_img_name== ', self._img_name)
            return True
        return False

    def move_focus_to_img(self):
        """moving focus to the image"""
        img = self.find_element(*ImagePageLocators.IMG_OPEN)
        action = ActionChains(self.browser)
        action.move_to_element(img)
        action.perform()
