import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.ozon.ru'

        super().__init__(web_driver, url)

    # Основное поле поиска
    search = WebElement(xpath='//*[@id="stickyHeader"]/div[3]/div[1]/form[1]/div[2]/input[1]')

    # Кнопка поиска
    search_run_button = WebElement(xpath='//*[@id="stickyHeader"]/div[3]/div/form/button')

     # Названия товаров в результатах поиска
    products_titles = ManyWebElements(xpath='//*[@id="layoutPage"]/div[1]/div[3]/div[1]/div/div/div[1]/strong')

    # Добавить в избранное товар
    button_favorites = WebElement(xpath='//*[@id="layoutPage"]/div[1]/div[3]/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/button')

    #кнопка избранное в headers

    headers_favorit = WebElement(xpath='//*[@id="stickyHeader"]/div[4]/a[1]/span[2]')

    # кнопка избранное в избранном для отмены
    button_favorites_in_favorites = WebElement(xpath='//*[@id="stickyHeader"]/div[4]/a[1]/span[2]')

    vk = WebElement(xpath='//*[@id="layoutPage"]/div[1]/footer/div[1]/div/div[5]/div[2]/a[1]')
    ok = WebElement(xpath='//*[@id="layoutPage"]/div[1]/footer/div[1]/div/div[5]/div[2]/a[2]/svg')
    telegram = WebElement(xpath='//*[@id="layoutPage"]/div[1]/footer/div[1]/div/div[5]/div[2]/a[3]')








