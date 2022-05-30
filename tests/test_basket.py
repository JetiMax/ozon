import time
import pytest
import requests
import allure

from pages.basket import Basket


def test_add_product_in_basket(driver):
    page = Basket(driver)
    page.search = 'Чайник заварочный GALAXY, 800 мл'
    page.search_run_button.click()
    driver.execute_script("window.scrollTo(0, 1080)")
    page.add_in_basket_button.click()
    driver.quit()


@pytest.mark.xfail(reason="adding product is not possible. block")
def test_adding_an_item_to_the_basket(driver):
    page = Basket(driver)
    page.search = 'Чайник заварочный GALAXY, 800 мл'
    page.search_run_button.click()
    driver.execute_script("window.scrollTo(0, 1080)")
    page.add_in_basket_button.click()
    page.basket_button.click()
    time.sleep(1)
    driver.refresh()
    page.button_amount.click()
    page.amount.click()
    driver.quit()


def test_adding_quantity_when_choosing_a_product(driver):
    page = Basket(driver)
    page.search = 'Чайник заварочный GALAXY, 800 мл'
    page.search_run_button.click()
    driver.execute_script("window.scrollTo(0, 1080)")
    page.add_in_basket_button.click()
    time.sleep(3)
    page.add_plus_button.click()
    driver.quit()


def test_status_code(driver):
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        response = requests.get('https://www.ozon.ru')
        assert response.status_code == 403, f"Неверный код ответа, получен {response.status_code}"
        with allure.step("Запрос отправлен. Десериализируем ответ из json в словарь."):
            with allure.step(f"Посмотрим что получили {response}"):
                print(response)


@pytest.mark.slow
def test_func_slow():
    pass


@pytest.mark.fast
def test_func_fast():
    pass


