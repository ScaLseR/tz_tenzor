"""locators for all class"""
from selenium.webdriver.common.by import By


class MainPageLocators:
    """locators for MainPage"""
    FIND_FIELD = (By.ID, 'text')
    SUGGEST = (By.CSS_SELECTOR, '.mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_theme_tile')
    BTN_FIND = (By.CSS_SELECTOR, '.search2__button')
    REZ_FIND = (By.CSS_SELECTOR, '[aria-label="Результаты поиска"]')
    FIRST_ELEMENT = (By.CSS_SELECTOR, '[accesskey="1"]')
    PICTURE_LINK = (By.CSS_SELECTOR, '[data-id="images"]')


class ImagePageLocators:
    """locators for ImagePage"""
