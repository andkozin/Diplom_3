import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Ожидание видимости элемента")
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание кликабельности элемента")
    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Клик по элементу")
    def click(self, locator):
        element = self.wait_clickable(locator)
        element.click()

    @allure.step("Получение текста элемента")
    def get_text(self, locator):
        return self.wait_visible(locator).text

    @allure.step("Проверка, что элемент виден")
    def is_visible(self, locator):
        try:
            self.wait_visible(locator)
            return True
        except:
            return False
