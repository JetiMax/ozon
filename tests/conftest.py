import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from abstract.selenium_listener import MyListener


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome("C:/Users/Max/PycharmProjects/practice/cromedriver/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    yield driver
    driver.quit()


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # Use headless if you do not need a browser Ui
    options.add_argument('--start-maximized')
    options.add_argument('--windows-size=1920, 1080')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    drivers = webdriver.Chrome(executable_path="C:/Users/Max/PycharmProjects/practice/cromedriver/chromedriver.exe", options=options)
    return drivers


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    driver = EventFiringWebDriver(driver, MyListener())
    url = 'https://www.ozon.ru/'
    if request.cls is not None:
        request.cls.driver = driver
        driver.get(url)
        # driver.delete_all_cookies()  # используем при защите от data scraping
        yield driver
        driver.quit()
