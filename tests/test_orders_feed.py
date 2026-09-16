# tests/test_orders_feed.py

import allure
import pytest

@allure.feature("Лента заказов - Stellar Burgers")
class TestOrdersFeed:

    @allure.story("Счетчики заказов")
    @allure.title("Счетчик   Выполнено за все время  увеличивается при новом заказе")
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_total_counter_increases(self, auth_user, main_page, feed_page):
        with allure.step("Запоминаем счетчик до заказа"):
            feed_page.open()
            before = feed_page.get_total_counter()
            allure.attach(str(before), name="Счетчик ДО", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Переходим в Конструктор и собираем заказ"):
            main_page.go_to_constructor()
            main_page.add_ingredient_via_drag()
            main_page.click_place_order()

        with allure.step("Ждем модалку и закрываем"):
            order_number = feed_page.wait_order_modal()
            allure.attach(order_number, name="Номер заказа", attachment_type=allure.attachment_type.TEXT)
            feed_page.close_order_modal()

        with allure.step("Проверяем увеличение счетчика"):
            feed_page.open()
            after = feed_page.wait_total_counter_increases(before)
            allure.attach(str(after), name="Счетчик ПОСЛЕ", attachment_type=allure.attachment_type.TEXT)

        assert after == before + 1, f"Счетчик не увеличился - было {before} - стало {after}"

    @allure.story("Счетчики заказов")
    @allure.title("Счетчик  Выполнено за сегодня  увеличивается при новом заказе")
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_today_counter_increases(self, auth_user, main_page, feed_page):
        with allure.step("Запоминаем значение счетчика  За сегодня  до заказа"):
            feed_page.open()
            before = feed_page.get_today_counter()
            allure.attach(str(before), name="Счетчик за сегодня ДО", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Создаем заказ: Конструктор - ингредиент - оформить"):
            main_page.go_to_constructor()
            main_page.add_ingredient_via_drag()
            main_page.click_place_order()

        with allure.step("Ждем и закрываем модалку с номером заказа"):
            order_number = feed_page.wait_order_modal()
            allure.attach(order_number, name="Номер заказа в модалке", attachment_type=allure.attachment_type.TEXT)
            feed_page.close_order_modal()

        with allure.step("Проверяем увеличение счетчика за сегодня"):
            feed_page.open()
            after = feed_page.wait_today_counter_increases(before)
            allure.attach(str(after), name="Счетчик за сегодня ПОСЛЕ", attachment_type=allure.attachment_type.TEXT)

        assert after == before + 1, f"Счетчик за сегодня не увеличился - было {before} - стало {after}"

    @allure.story("Отображение заказов в ленте")
    @allure.title("Заказ появляется в разделе  В работе ")
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_order_appears_in_work_section(self, auth_user, main_page, feed_page):
        with allure.step("Создаем заказ"):
            main_page.go_to_constructor()
            main_page.add_ingredient_via_drag()
            main_page.click_place_order()

        with allure.step("Ждем реальный номер и закрываем модалку"):
            order_number = feed_page.wait_real_order_number()
            allure.attach(order_number, name="Номер заказа", attachment_type=allure.attachment_type.TEXT)
            feed_page.close_order_modal()

        with allure.step("Открываем ленту и проверяем раздел  В работе "):
            feed_page.open()
            in_progress_list = feed_page.get_in_progress_orders()

            allure.attach(
                "\n".join(in_progress_list),
                name="Список  В работе ",
                attachment_type=allure.attachment_type.TEXT
            )

        assert order_number.lstrip('0') in in_progress_list, f"Заказ {order_number} нет в ленте - Список: {in_progress_list}"
