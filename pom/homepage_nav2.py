from selenium.webdriver.remote.webelement import WebElement
from typing import List

from base.seleniumbase import SeleniumBase


class HomepageNav2(SeleniumBase):  # Наследуем класс SeleniumBase

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = 'div.cj6>div>a'
        self.NAV_LINK_TEXT = 'Ваши товары на Ozon,Продавайте на Ozon,Установите постамат Ozon Box,Откройте пункт выдачи Ozon,Стать Поставщиком Ozon,Что продавать на Ozon,Selling on Ozon,Об Ozon / About Ozon,Станьте курьером,Контакты для прессы,Реквизиты,Арт-проект Ozon Ballon,Бренд Ozon,Горячая линия комплаенс,Устойчивое развитие,Ozon Забота,Условия обработки персональных данных,Как сделать заказ,Доставка,Оплата,Контакты,Безопасность,Добавить компанию,Мои компании,Подарочные сертификаты,'

    def get_nav_links(self) -> List[WebElement]:  # Функция будет возвращать нам наш элемент
        return self.are_visible('css', self.__nav_links, 'Header Navigation Links')

    '''Возвращаем текст с веб элементов'''

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)  # метод возвращат текст
        # return Utils.join_strings(nav_links_text)
        return ','.join(nav_links_text)

    def get_nav_link_by_name(self, name) -> WebElement:
        elements = self.get_nav_links()
        return self.get_element_by_text(elements, name)
