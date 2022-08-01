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
    IMG_FST_CAT = (By.CSS_SELECTOR, '.PopularRequestList-Shadow')
    FIND_FIELD = (By.CSS_SELECTOR, '.input__control.mini-suggest__input')
    IMG_FST = (By.CSS_SELECTOR, '.serp-item__thumb.justifier__thumb')
    NEXT_BTN = (By.CSS_SELECTOR, '.CircleButton.CircleButton_type_next.CircleButton_type.'
                                'MediaViewer-Button.MediaViewer-Button_hovered.MediaViewer_'
                                'theme_fiji-Button.MediaViewer-ButtonNext.MediaViewer_theme_fiji-ButtonNext')
    PREV_BTN = (By.CSS_SELECTOR, '.CircleButton.CircleButton_type_prev.CircleButton_type.MediaViewer-'
                                 'Button.MediaViewer_theme_fiji-Button.MediaViewer-'
                                 'ButtonPrev.MediaViewer_theme_fiji-ButtonPrev')
    IMG_OPEN = (By.CSS_SELECTOR, '.MMImage-Origin')