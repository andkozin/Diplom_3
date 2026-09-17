# pages/base_page.py
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Открываем страницу по URL: {url}")
    def open(self, url):
        self.driver.get(url)
# добавил
    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        return self.driver.current_url
# добавил
    @allure.step("Выполняем через скрипт")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)
# добавил
    @allure.step("Перетаскиваем элемент в корзину")
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step("Ждем элемент")
    def wait_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Ожидание видимости элемента")
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание кликабельности элемента")
    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Клик по элементу")
    def click(self, locator):
        element = self.wait_clickable(locator)
        self.execute_script("arguments[0].click();", element)

    @allure.step("Ждем, пока элемент станет невидимым")
    def wait_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Проверяем, что элемент НЕ виден")
    def is_not_visible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))
        return True

    @allure.step("Ввод текста в поле: {text}")
    def send_keys(self, locator, text):
        field = self.wait_visible(locator)
        field.clear()
        field.send_keys(text)

    @allure.step("Получаем текст элемента")
    def get_text(self, locator):
        return self.wait_visible(locator).text

    @allure.step("Получаем текст элемента через JS")
    def get_text_content(self, locator):
        element = self.wait_presence(locator)
        return self.execute_script("return arguments[0].textContent;", element)

    @allure.step("Находим все элементы по локатору")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Ждем появления элемента с цифрами")
    def wait_elements_with_digits(self, locator):
        self.wait.until(lambda d: any(
            "".join(ch for ch in el.text if ch.isdigit())
            for el in self.find_elements(locator)
        ))

    @allure.step("Проверяем видимость элемента")
    def is_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return True

    @allure.step("Ждем, пока текст исчезнет из элемента")
    def wait_text_not_present(self, locator, text):
        self.wait.until_not(EC.text_to_be_present_in_element(locator, text))

