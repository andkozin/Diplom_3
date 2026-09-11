import allure
from pages.main_page import MainPage

@allure.feature("Навигация")
@allure.story("Переход между разделами")
@allure.title("TC-NAV-001: Переход в раздел «Конструктор»")
def test_navigate_to_constructor(driver):
    main_page = MainPage(driver)

    with allure.step("Переходим в «Конструктор»"):
        main_page.go_to_constructor()

    with allure.step("Проверяем, что заголовок «Соберите бургер» отображается"):
        assert main_page.is_constructor_header_visible(), "Заголовок раздела не найден"




@allure.feature("Навигация")
@allure.story("Переход между разделами")
@allure.title("TC-NAV-002: Переход в раздел «Лента заказов»")
def test_navigate_to_feed(driver):
    main_page = MainPage(driver)

    with allure.step("Кликаем на пункт меню «Лента заказов»"):
        main_page.go_to_feed()

    with allure.step("Проверяем, что заголовок «Лента заказов» отображается"):
        assert main_page.is_feed_header_visible(), "Заголовок раздела «Лента заказов» не найден"
