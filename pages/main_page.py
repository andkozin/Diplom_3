import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as MPL

class MainPage(BasePage):
    @allure.step("Переход в Конструктор")
    def go_to_constructor(self):
        self.click(MPL.CONSTRUCTOR_BTN)

    @allure.step("Переход в Ленту заказов")
    def go_to_feed(self):
        self.click(MPL.FEED_BTN)

    @allure.step("Клик по первому ингредиенту")
    def click_first_ingredient(self):
        self.click(MPL.FIRST_INGREDIENT)

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        self.click(MPL.MODAL_CLOSE_BTN)

    @allure.step("Добавление ингредиента в заказ (drag-and-drop)")
    def add_ingredient_via_drag(self):
        from selenium.webdriver.common.action_chains import ActionChains
        ingredient = self.wait_clickable(MPL.FIRST_INGREDIENT)
        checkout = self.wait_clickable(MPL.CHECKOUT_BTN)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, checkout).perform()

    @allure.step("Получение значения счётчика ингредиента")
    def get_ingredient_counter(self):
        # Если счётчика нет — вернём 0
        if not self.is_visible(MPL.INGREDIENT_COUNTER):
            return 0
        text = self.get_text(MPL.INGREDIENT_COUNTER)
        try:
            return int(text)
        except ValueError:
            return 0

    @allure.step("Проверка отображения заголовка «Конструктор»")
    def is_constructor_header_visible(self):
        return self.is_visible(MPL.CONSTRUCTOR_HEADER)

    @allure.step("Проверка отображения заголовка «Лента заказов»")
    def is_feed_header_visible(self):
        return self.is_visible(MPL.FEED_HEADER)

