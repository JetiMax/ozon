from selenium.webdriver.remote.webelement import WebElement
from typing import List

from base.seleniumbase import SeleniumBase


class HomepageNav(SeleniumBase):  # Наследуем класс SeleniumBase

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = 'ul.kc9>li'
        self.NAV_LINK_TEXT = 'TOP Fashion,Premium,Билеты и Отели,Ozon fresh,Ozon Счёт,LIVE,Акции,Бренды,Магазины,Электроника,Одежда и обувь,Детские товары,Дом и сад,Зона лучших цен'

    def get_nav_links(self) -> List[WebElement]:  # Функция будет возвращать нам наш элемент
        return self.are_visible('css', self.__nav_links, 'Header Navigation Links')

    '''Возвращаем текст с веб элементов'''

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)  # метод возвращат текст
        # return Utils.join_strings(nav_links_text)
        return ','.join(nav_links_text)

    # def get_nav_link_by_name(self, name) -> WebElement:
    '''Return a nav link WebElement, the input is a link's name'''
    #     elements = self.get_nav_links()
    #     return self.get_element_by_text(elements, name)
