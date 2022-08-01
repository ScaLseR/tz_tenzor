"""Test Cases Module"""
from pages.main_page import MainPage
from time import sleep

_URL = 'https://yandex.ru'
_TEXT = 'Тензор'
_LINK = 'https://tensor.ru/'


def test_search_in_ya(browser):
    """test case search in yandex"""
    page = MainPage(browser, _URL)
    page.open()
    assert page.find_search_field(), 'Отсутствует поле для поиска!'
    page.input_text_to_search(_TEXT)
    assert page.find_suggest(), 'Отсутствует таблица с подсказками (suggest)!'
    page.click_enter()
    assert page.first_link() == _LINK, 'Первая ссылка не ведет на сайт tenzor.ru'

