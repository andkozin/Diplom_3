import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://stellarburgers.education-services.ru/"


@pytest.fixture
def driver(request):
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1280, 1024)
    driver.get(BASE_URL)
    driver.implicitly_wait(5)

    yield driver

    if request.node.rep_call and request.node.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Скриншот на падении",
            attachment_type=allure.attachment_type.PNG,
        )

    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
