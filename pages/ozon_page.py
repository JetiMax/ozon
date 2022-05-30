from selenium.webdriver.common.by import By
from tests.config import url


class OzonPage():

    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        self.driver.get(url)

    def get_shops(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'TOP Fashion')]")

    def get_shops1(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Premium')]")

    def get_shops2(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Ozon Travel')]")

    def get_shops3(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Ozon fresh')]")

    def get_shops4(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Ozon Счёт')]")

    def get_shops5(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'LIVE')]")

    def get_shops6(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Акции')]")

    def get_shops7(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Бренды')]")

    def get_shops8(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Магазины')]")

    def get_shops9(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Электроника')]")

    def get_shops10(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Одежда и обувь')]")

    def get_shops11(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Детские товары')]")

    def get_shops12(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Дом и сад')]")

    def get_shops13(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Зона лучших цен')]")

    def command_line_args(self):
        raise NotImplementedError("This method needs to be implemented in a sub class")


class ShopPage():

    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        self.driver.get(url)

    def get_shops(self):
        return self.driver.find_element(By.XPATH, '//*[@id="layoutPage"]/div[1]/div[3]/div[5]/div')

    def command_line_args(self):
        raise NotImplementedError("This method needs to be implemented in a sub class")
