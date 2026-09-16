# tests/test_navigation.py

import allure
import pytest

@allure.feature("Навигация и работа с ингредиентами")
class TestNavigation:
   
    @allure.story("Переход между разделами")
    @allure.title("Переход в раздел Конструктор")
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_navigate_to_constructor(self, main_page):
        with allure.step("Скрываем конструктор (переход на Ленту заказов)"):
            main_page.click_to_feed()
            
            assert main_page.is_constructor_header_not_displayed(), "Заголовок 'Соберите бургер' не должен быть на Ленты заказов"

        with allure.step("Переходим в Конструктор"):
            main_page.go_to_constructor()

        assert main_page.is_constructor_header_visible(), "Заголовок 'Соберите бургер' нет"

    @allure.story("Переход между разделами")
    @allure.title("Переход в раздел Лента заказов")
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_navigate_to_feed(self, main_page):
        with allure.step("Переходим в Ленту заказов"):
            main_page.click_to_feed()

        assert main_page.is_feed_header_visible(), "Заголовок 'Лента заказов' нет"

    @allure.story("Детали ингредиента")
    @allure.title("Открытие модального окна")
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_ingredient_modal_opens(self, main_page):
        with allure.step("Кликаем по первому ингредиенту"):
            main_page.click_first_ingredient()

        with allure.step("Проверяем-что модальное окно появилось"):
           
            assert main_page.is_modal_visible(), "Модальное окно не появилось"

        with allure.step("Проверяем, что в заголовке есть текст"):
            title = main_page.get_modal_title()
           
            assert title, "Заголовок модального окна пустой"

        assert main_page.is_modal_visible() and bool(title), "Модальное окно - нет"

    @allure.story("Детали ингредиента")
    @allure.title("Закрытие модального окна кликом по крестику")
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_ingredient_modal_close(self, main_page):
        with allure.step("Открываем модальное окно (подготовка)"):
            main_page.click_first_ingredient()

        with allure.step("Клик по крестику"):
            main_page.close_modal()

        assert main_page.is_modal_closed(), "Модалка осталась видимой"

    @allure.story("Конструктор - добавление ингредиентов")
    @allure.title("Счётчик ингредиента увеличивается при перетаскивании в корзину")
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_ingredient_counter_increases(self, main_page):
        with allure.step("Получаем начальное значение счётчика"):
            initial_count = main_page.get_ingredient_counter()
            assert initial_count >= 0, f"Счётчик  >= 0  был - {initial_count}"
            allure.attach(
                f"Начальный счётчик: {initial_count}",
                name="Начальный счётчик",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Перетаскиваем ингредиент в корзину"):
            main_page.add_ingredient_via_drag()

        with allure.step("Проверяем, что счётчик увеличился"):
            new_count = main_page.wait_counter_increases(initial_count)
            allure.attach(
                f"Новый счётчик: {new_count}",
                name="Новый счётчик",
                attachment_type=allure.attachment_type.TEXT
            )
           
        assert new_count > initial_count, f"Счётчик не увеличился - было {initial_count} - стало {new_count}"



