"""test cases module"""
from pages.main_page import MainPage
from pages.image_page import ImagePage


_BASE_URL = 'https://yandex.ru'
_TEXT = 'тензор'
_LINK = 'https://tensor.ru/'
_IMG_URL = 'https://yandex.ru/images/'


def test_search_in_ya(browser):
    """test case search in yandex"""
    page = MainPage(browser, _BASE_URL)
    page.open()
    assert page.find_search_field(), 'Отсутствует поле для поиска'
    page.input_text_to_search(_TEXT)
    assert page.find_suggest(), 'Отсутствует таблица с подсказками (suggest)'
    page.click_enter()
    assert page.first_link() == _LINK, f'Первая ссылка не ведет на сайт {_LINK}'


def test_pictures(browser):
    """test case finding images in the browser"""
    page = MainPage(browser, _BASE_URL)
    page.open()
    assert page.find_picture_link(), 'Отсутствует ссылка "картинки" на странице'
    page.click_to_picture_link()
    image_page = ImagePage(browser, browser.current_url)
    assert image_page.get_img_page_url() == _IMG_URL, f'Перешли не на страницу {_IMG_URL}'
    image_page.open_first_category()
    assert image_page.get_category_name_from_search_field(), 'Имя категории не отображается в поле поиска'
    image_page.open_first_img()
    assert image_page.img_is_open(), 'Картинка не открылась'
    image_page.click_forward_btn()
    assert not image_page.img_is_change(), 'Картинка не сменилась'
    image_page.click_back_button()
    assert image_page.img_is_change(), 'Картинка не совпадает с начальной'
