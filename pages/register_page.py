# pages/register_page.py

import allure
import urls
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators import RegisterLocators as RL


class RegisterPage(BasePage):

    @allure.step("Открываем страницу регистрации")
    def open(self):
        
        super().open(urls.REGISTER_URL)

    @allure.step("Регистрируем пользователя: {name}, {email}")
    def register(self, name, email, password):
        self.send_keys(RL.NAME_FIELD, name)
        self.send_keys(RL.EMAIL_FIELD, email)
        self.send_keys(RL.PASSWORD_FIELD, password)
        self.click(RL.REGISTER_BUTTON)
        self.wait.until(EC.url_contains("/login"))
        return self

