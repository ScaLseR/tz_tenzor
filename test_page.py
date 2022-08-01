"""Test Cases Module"""
from pages.main_page import MainPage
from time import sleep

_URL = 'http://yandex.ru'
_TEXT = 'Тензор'


def test_search_in_ya(browser):
    """test case search in yandex"""
    page = MainPage(browser, _URL)
    page.open()
    assert page.find_search_field(), 'Отсутствует поле для поиска!'
    page.input_text_to_search(_TEXT)
    assert page.find_suggest(), 'Отсутствует таблица с подсказками!'
    page.click_enter()
    sleep(300)
