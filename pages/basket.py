import os

from pages.base import WebPage
from pages.elements import WebElement


class Basket(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.ozon.ru'

        super().__init__(web_driver, url)

    # Основное поле поиска
    search = WebElement(xpath='//*[@id="stickyHeader"]/div[3]/div[1]/form[1]/div[2]/input[1]')

    # Кнопка поиска
    search_run_button = WebElement(xpath='//*[@id="stickyHeader"]/div[3]/div/form/button')

    # Добавление товара в корзину
    add_in_basket_button = WebElement(xpath='//*[@id="layoutPage"]/div[1]/div[3]/div[2]/div[2]/div[4]/div/div/div/div[1]/div[1]/div[4]/div/div/div/button/span')

    # кнопка корзины
    basket_button = WebElement(xpath='//*[@id="stickyHeader"]/div[4]/a[2]/span[2]')

    # кнопка количества
    button_amount = WebElement(xpath='//*[@id="layoutPage"]/div[1]/div[1]/div[1]/div[3]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]')

    # количество
    amount = WebElement(xpath='body/div[22]/div[1]/div[1]/div[1]/div[5]')

    # добавление +
    add_plus_button = WebElement(xpath='//*[@id="layoutPage"]/div[1]/div[3]/div[2]/div[2]/div[4]/div/div/div/div[1]/div[1]/div[4]/div/div/div[2]/div/button')