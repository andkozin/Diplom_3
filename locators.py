from selenium.webdriver.common.by import By

class MainPageLocators:
    # Навигация
    CONSTRUCTOR_BTN = (By.XPATH, '//p[text()="Конструктор"]/..')
    FEED_BTN = (By.XPATH, '//p[text()="Лента заказов"]/..')
    FEED_HEADER = (By.XPATH, '//h1[contains(text(), "Лента заказов")]')


    # Конструктор бургера
    FIRST_INGREDIENT = (By.CSS_SELECTOR, '.BurgerIngredient')
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, '.counter__text')

    # Модальное окно (ингредиент)
    MODAL_WINDOW = (By.CSS_SELECTOR, '.Modal')
    MODAL_CLOSE_BTN = (By.CSS_SELECTOR, '.Modal__close')

    # Оформление заказа
    CHECKOUT_BTN = (By.XPATH, '//button[text()="Оформить заказ"]')

    # Заголовок конструктора (чтобы убедиться, что мы на нужной странице)
    CONSTRUCTOR_HEADER = (By.XPATH, '//h1[contains(text(), "Соберите бургер")]')
