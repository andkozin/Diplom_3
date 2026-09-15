# locators.py

from selenium.webdriver.common.by import By

class MainPageLocators:
    # Навигация
    CONSTRUCTOR_BTN = (By.CSS_SELECTOR, 'a.AppHeader_header__link__3D_hX[href="/"]')
    FEED_BTN = (By.XPATH, '//a[contains(@href, "/feed") and .//p[normalize-space()="Лента Заказов"]]')
    FEED_HEADER = (By.XPATH, '//h1[contains(text(), "Лента заказов")]')
    CONSTRUCTOR_HEADER = (By.XPATH, '//h1[contains(text(), "Соберите бургер")]')


class ConstructorLocators:
    # Конструктор бургера
    FIRST_INGREDIENT = (By.CSS_SELECTOR, 'a.BurgerIngredient_ingredient__1TVf6')
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, '.counter_counter__num__3nue1')
    BURGER_CONSTRUCTOR_BASKET = (By.CSS_SELECTOR, '.BurgerConstructor_basket__list__l9dp_')

    # Оформление заказа
    CHECKOUT_BTN = (By.XPATH, "//button[normalize-space(text())='Оформить заказ']")


class ModalLocators:
    # Модальное окно (ингредиент)
    MODAL_WINDOW = (By.CSS_SELECTOR, '.Modal_modal__container__Wo2l_')
    MODAL_TITLE = (By.XPATH, '//div[contains(@class,"modal")]//h2')
    MODAL_CLOSE_BTN = (By.CSS_SELECTOR, '.Modal_modal__close__TnseK')

    # Модалка после оформления заказа
    ORDER_MODAL = (By.CSS_SELECTOR, ".Modal_modal__contentBox__sCy8X")
    ORDER_MODAL_NUMBER = (By.CSS_SELECTOR, ".Modal_modal__title__2L34m")
    ORDER_MODAL_CLOSE = (By.CSS_SELECTOR, "button.Modal_modal__close__TnseK")

    # Оверлей
    OVERLAY = (By.CSS_SELECTOR, ".Modal_modal_overlay__x2ZCr")


class FeedLocators:
    # Счетчик Выполнено за все время
    COUNTER_TOTAL = (By.CSS_SELECTOR, 'p.OrderFeed_number__2MbrQ.text.text_type_digits-large')

    # Счетчик Выполнено за сегодня
    COUNTER_TODAY = (
        By.XPATH,
        "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p[1]"
    )

    # Элементы списка В работе 
    IN_PROGRESS_ITEMS = (By.CSS_SELECTOR, "ul[class*='OrderFeed_orderListReady'] li")


class RegisterLocators:
    # для регистрации
    NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    EMAIL_FIELD = (By.XPATH, '//label[normalize-space()="Email"]/following-sibling::input')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[type="password"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '.button_button__33qZ0')


class LoginLocators:
    # для логина
    EMAIL_FIELD_LOG = (
        By.CSS_SELECTOR,
        "form.Auth_form__3qKeq input.input__textfield[type='text']"
    )
    PASSWORD_FIELD_LOG = (By.XPATH, "//label[normalize-space()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.button_button__33qZ0')
