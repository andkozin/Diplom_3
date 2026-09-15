# conftest.py
import pytest
import allure
import urls
from pages.main_page import MainPage
from pages.orders_feed_page import OrdersFeedPage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from helper.data_generator import prepare_user_credentials
from helper.user_helper import UserHelper

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def feed_page(driver):
    return OrdersFeedPage(driver)


@pytest.fixture
def driver(request):
    browser = request.param
    if browser == "firefox":
        options = FirefoxOptions()
        drv = webdriver.Firefox(options=options)
    else:
        options = ChromeOptions()
        #  всплывашка Пароль раскрыт в результате утечки
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,  # убирает "пароль раскрыт в утечке"
        }
        options.add_experimental_option("prefs", prefs)

        # ------
        drv = webdriver.Chrome(options=options)
    drv.set_window_size(1280, 1024)
    drv.get(urls.BASE_URL)
    yield drv
    drv.quit()


@pytest.fixture
def auth_user(driver):
    
    user = prepare_user_credentials()

    #Регистрация 
    register_page = RegisterPage(driver)
    register_page.open()
    
    register_page.register(user["name"], user["email"], user["password"])

    #Логин
    login_page = LoginPage(driver)
   
    login_page.login(user["email"], user["password"])

    yield user

    # --- TEARDOWN --- ИИ
    with allure.step("Очистка: удаление тестового пользователя"):
        token = driver.execute_script("return localStorage.getItem('accessToken');")
        
        if not token or token == 'null':
            allure.attach(
                "Не удалось получить токен из localStorage",
                name="Cleanup Error: No Token",
                attachment_type=allure.attachment_type.TEXT,
            )
            return

        response = UserHelper.delete_user(token)
        
        if response.status_code not in [202]:
            allure.attach(
                f"Удаление не прошло: статус {response.status_code}\nТело: {response.text}",
                name="Cleanup Warning",
                attachment_type=allure.attachment_type.TEXT,
            )
# для скринов при падении
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Скриншот при падении",
                attachment_type=allure.attachment_type.PNG
                )
        


