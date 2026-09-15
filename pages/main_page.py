# pages/main_page.py

import allure
from pages.base_page import BasePage
from locators import MainPageLocators as MPL
from locators import ConstructorLocators as CL
from locators import ModalLocators as ML
from seletools.actions import drag_and_drop


class MainPage(BasePage):
    @allure.step("Переход в Конструктор")
    def go_to_constructor(self):
        self.click(MPL.CONSTRUCTOR_BTN)

    @allure.step("Переход в Ленту заказов")
    def click_to_feed(self):
        self.click(MPL.FEED_BTN)

    @allure.step("Проверка отображения заголовка Лента заказов")
    def is_feed_header_visible(self):
        return self.is_visible(MPL.FEED_HEADER)

    @allure.step("Проверяем, что модальное окно видно")
    def is_modal_visible(self):
        return self.is_visible(ML.MODAL_WINDOW)

    
    @allure.step("Проверяем, что модальное окно закрыто") # навигация ингр
    def is_modal_closed(self):
        return self.is_not_visible(ML.MODAL_WINDOW)


    @allure.step("Получаем заголовок модального окна")
    def get_modal_title(self):
        return self.get_text(ML.MODAL_TITLE)

    @allure.step("Клик по первому ингредиенту")
    def click_first_ingredient(self):
        self.click(CL.FIRST_INGREDIENT)

    @allure.step("Нажимаем Оформить заказ и получаем реальный номер заказа")
    def click_place_order(self):
        self.click(CL.CHECKOUT_BTN)


    @allure.step("Закрытие модального окна")
    def close_modal(self):
        self.click(ML.MODAL_CLOSE_BTN)

    
    @allure.step("Получение значения счетчика ингредиента")
    def get_ingredient_counter(self):
        text = self.get_text(CL.INGREDIENT_COUNTER)
        return int(text)
       

    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient_via_drag(self):
        ingredient = self.wait_clickable(CL.FIRST_INGREDIENT)
        basket = self.wait_clickable(CL.BURGER_CONSTRUCTOR_BASKET)
        drag_and_drop(self.driver, ingredient, basket)
    
    @allure.step("Проверяем, что заголовок Соберите бургер не отображается")
    def is_constructor_header_not_displayed(self):
        elements = self.driver.find_elements(*MPL.CONSTRUCTOR_HEADER)
        return len(elements) == 0

    @allure.step("Проверка отображения заголовка Конструктор")
    def is_constructor_header_visible(self):
        return self.is_visible(MPL.CONSTRUCTOR_HEADER)

    @allure.step("Ждем увеличения счетчика ингредиента")
    def wait_counter_increases(self, expected_value):
        self.wait.until(lambda d: self.get_ingredient_counter() > expected_value)
        return self.get_ingredient_counter()

    

