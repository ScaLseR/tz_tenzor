"""locators for all class"""
from selenium.webdriver.common.by import By


class BasePageLocators:
    """locators for BasePage"""


class MainPageLocators:
    """locators for MainPage"""
    FIND_FIELD = (By.ID, 'text')
    SUGGEST = (By.CSS_SELECTOR, '.mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_theme_tile')
