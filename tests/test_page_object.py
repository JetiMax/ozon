# -*- encoding=utf8 -*-
import warnings
import time

from unittest import result
from pages.ozon import MainPage
from pages.ozon_page import OzonPage, ShopPage


def test_visit(driver):
    ozon_pages = OzonPage(driver)
    ozon_pages.visit()
    ozon_pages.get_shops()
    async_timeout = 100.0
    assert ozon_pages.get_shops().is_displayed()  # Проверяем что мы перешли на страницу
    driver.close()
    print(async_timeout)
    return async_timeout


def test_shops(driver):
    ozon_pages = OzonPage(driver)
    ozon_pages.visit()
    ozon_pages.get_shops().click()
    shop_pages = ShopPage(driver)
    time.sleep(3)
    print(shop_pages.get_shops())
    assert shop_pages.get_shops().is_displayed()
    time.sleep(3)
    driver.close()


def api_v1():
    warnings.warn(UserWarning("api v1, should use functions from v2"))
    warnings.warn(DeprecationWarning("api v1, should use functions from v2"))
    return 1


def test_one():
    assert api_v1() == 1


def test_scrool(driver):
    ozon_pages = OzonPage(driver)
    ozon_pages.visit()
    ozon_pages.get_shops()
    driver.execute_script("window.scrollTo(0, 1080)")
    assert ozon_pages.get_shops().is_displayed()
    time.sleep(5)
    driver.close()


def test_check_main_search(driver):
    """ Make sure main search works fine. """

    page = MainPage(driver)
    page.search = 'UGG'
    page.search_run_button.click()


    # Убеждаемся, что пользователь может видеть список продуктов:
    assert page.products_titles.count() >= 1

    # Убеждаемся, что пользователь нашел соответствующие продукты
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'ugg' in title.lower(), msg
        driver.close()


def test_check_wrong_input_in_search(driver):
    """ Make sure that wrong keyboard layout input works fine. """

    page = MainPage(driver)

    # Попробуйте ввести "крем" с английской клавиатуры:
    page.search = 'rhtv'
    page.search_run_button.click()

    # Убедитесь, что пользователь может видеть список продуктов:
    assert page.products_titles.count() >= 1

    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'крем' in title.lower(), msg
        driver.close()


def test_add_favorites(driver):
    page = MainPage(driver)
    page.search = 'CeraVe Крем для рук восстанавливающий, для очень сухой кожи, 50 мл'
    page.search_run_button.click()
    page.button_favorites.click()
    driver.close()


def test_add_and_deleted_favorites(driver):
    page = MainPage(driver)
    page.search = 'CeraVe Крем для рук восстанавливающий, для очень сухой кожи, 50 мл'
    page.search_run_button.click()
    page.button_favorites.click()
    page.headers_favorit.click()
    time.sleep(1)
    page.button_favorites_in_favorites.click()
    time.sleep(2)
    driver.close()


'''Тест footer соц.сети'''


def test_footer_icon_vk(driver):
    page = MainPage(driver)
    page.vk.click()
    assert result


def test_footer_icon_ok(driver):
    page = MainPage(driver)
    page.vk.click()
    assert result


def test_footer_icon_telegram(driver):
    page = MainPage(driver)
    page.telegram.click()
    assert result

