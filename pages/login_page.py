# pages/login_page.py

import urls
import allure
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators import ModalLocators as ML
from locators import LoginLocators as LL


class LoginPage(BasePage):
    @allure.step("Открываем страницу входа")
    def open(self):
        self.driver.get(urls.LOGIN_URL)  # ← заменяем на super().open(urls.LOGIN_URL)
        super().open(urls.LOGIN_URL)

    @allure.step("Выполняем вход: email={email}, password={password}")
    def login(self, email, password):
        self.send_keys(LL.EMAIL_FIELD_LOG, email)
        self.send_keys(LL.PASSWORD_FIELD_LOG, password)

        self.wait.until(EC.invisibility_of_element_located(ML.OVERLAY))

        self.click(LL.LOGIN_BUTTON)

        start_url = self.get_current_url()
        self.wait.until(EC.url_changes(start_url))

