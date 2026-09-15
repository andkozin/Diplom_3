# pages/orders_feed_page.py
import allure

from pages.base_page import BasePage
from locators import ModalLocators as ML
from locators import FeedLocators as FL

import urls
import re


class OrdersFeedPage(BasePage):

    @allure.step("Открываем Ленту заказов")
    def open(self):
        self.driver.get(urls.FEED_URL)

    

    @allure.step("Получаем значение счетчика Выполнено за все время")
    def get_total_counter(self):
        text = self.get_text_content(FL.COUNTER_TOTAL)
        digits = re.findall(r'\d+', text)
        return int(digits[0]) if digits else 0

    @allure.step("Получаем значение счетчика  Выполнено за сегодня")
    def get_today_counter(self):
        text = self.get_text_content(FL.COUNTER_TODAY)
        digits = re.findall(r'\d+', text)
        return int(digits[0]) if digits else 0


    @allure.step("Получаем номера заказов в статусе В работе")
    def get_in_progress_orders(self):
        self.wait_elements_with_digits(FL.IN_PROGRESS_ITEMS)

        items = self.find_elements(FL.IN_PROGRESS_ITEMS)
        result = []
        for el in items:
            text = el.text.strip()
            digits = "".join(ch for ch in text if ch.isdigit())
            if digits:
                result.append(digits.lstrip('0'))
        return result


    @allure.step("Ждем появления реального номера заказа (не 9999)")
    def wait_real_order_number(self):
        self.wait_visible(ML.ORDER_MODAL)
        self.wait_text_not_present(ML.ORDER_MODAL_NUMBER, "9999")
        return self.wait_presence(ML.ORDER_MODAL_NUMBER).text.strip()

    @allure.step("Ждем появления модалки с номером заказа")
    def wait_order_modal(self):
        self.wait_visible(ML.ORDER_MODAL)
        return self.wait_presence(ML.ORDER_MODAL_NUMBER).text.strip()

    @allure.step("Закрываем модалку с номером заказа")
    def close_order_modal(self):
        self.click(ML.ORDER_MODAL_CLOSE)
        self.wait_invisible(ML.ORDER_MODAL)


    @allure.step("Ждем увеличения счетчика за все время ")
    def wait_total_counter_increases(self, expected_value):
        
        self.wait.until(lambda d: self.get_total_counter() > expected_value)
        return self.get_total_counter()

    @allure.step("Ждем увеличения счетчика Выполнено за сегодня")
    def wait_today_counter_increases(self, expected_value):
       
        self.wait.until(lambda d: self.get_today_counter() > expected_value)
        return self.get_today_counter()
