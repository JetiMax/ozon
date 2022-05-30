from selenium.webdriver.remote.webelement import WebElement
from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumBase:

    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 5, 0.5)

    def __get_selenium_by(self, find_by: str) -> dict:  # __get приватный класс
        find_by = find_by.lower()
        locating = {
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'class_name': By.CLASS_NAME,
            'id': By.ID,
            'link_text': By.LINK_TEXT,
            'name': By.NAME,
            'partial_link_text': By.PARTIAL_LINK_TEXT,
            'tag_name': By.TAG_NAME
            }
        return locating[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:  # Возвращает WebElement
        '''Waiting on element and return WebElement if it is visible'''
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator))
                                 , locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        '''Waiting on element and return WebElement if it is present on DOM'''
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        '''Wait on element until it disappears '''
        return self.__wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by),
                                                                     locator)), locator_name)

    '''находим несколько элементов на странице'''
    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        '''Waiting on elements and return WebElements if they are visible'''
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by),
                                                                        locator)), locator_name)

    def is_all_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        '''Waiting on elements and return WebElements if they are present on DOM'''
        return self.__wait.until(ec.presence_of_all_elements_located((self.__get_selenium_by(find_by),
                                                                      locator)), locator_name)

    def get_text_from_webelements(self, elements: List[WebElement]) -> List[str]:
        '''The input should be a list of WebElements, where we read text from each element and Return a List[String]'''
        # element_list = []
        # for element in elements:
        #     element_list.append(element.text) # использование цикла for , вместо return
        return [element.text for element in elements]  # List comprehension — это упрощенный подход к созданию списка, который задействует цикл for, а также инструкции if-else д

    def get_element_by_text(self, elements: List[WebElement], name: str) -> WebElement:
        '''The input should we a list of WebElements, from which we return a single WebElement found by it's name'''
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]

    def delete_cookie(self, cookie_name: str) -> None:
        """Delete a cookie by a name"""
        self.driver.delete_cookie(cookie_name)


