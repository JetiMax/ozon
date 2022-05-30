ФАЙЛЫ

conftest.py содержит фикстуры для setup

pages/base.py содержит реализацию шаблона PageObject для Python.

pages/elements.py содержит вспомогательный класс для определения веб-элементов на веб-страницах.

seleniumbase.py  содержит базовые методы для test_homepage.py

pom/homepage_nav.py — это микрофреймворк Page-Object-Model для простой, быстрой и приятной разработки тестов веб-интерфейса. где наследуем class seleniumbase 

utils.py Содержит утилиту/ы

selenium_listener.py Содеожит исключения 

КАК ЗАПУСКАТЬ ТЕСТ:
Установите все требования:

pip install -r requirements
Загрузите Selenium WebDriver с https://chromedriver.chromium.org/downloads (выберите версию, совместимую с вашим браузером)


ЗАПУСТЬТЬ ТЕСТ:

pytest  -s -v 
