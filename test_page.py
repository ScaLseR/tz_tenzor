"""Test Cases Module"""
from pages.main_page import MainPage
from pages.locators import MainPageLocators
from time import sleep

_URL = 'http://yandex.ru'
_TEXT = 'Тензор'


def test_search_in_ya(browser):
    """test case search in yandex"""
    page = MainPage(browser, _URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.FIND_FIELD), 'Отсутствует поле для поиска!'
    page.input_text_to_element(*MainPageLocators.FIND_FIELD, _TEXT)
    assert page.is_element_present(*MainPageLocators.SUGGEST), 'Отсутствует таблица с подсказками!'
    sleep(10)
