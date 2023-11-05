import pytest
import allure
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture(scope='session')
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        'viewport': {
            'width': 1920,
            'height': 1080,
        },
    }


@pytest.fixture()
def login_page(page: Page):
    return LoginPage(page)


@pytest.fixture()
def main_page(page: Page):
    return MainPage(page)


@pytest.fixture()
def cart_page(page: Page):
    return CartPage(page)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    test_result = outcome.get_result()
    test_result.extra = []

    types = ["smoke", "hotlink"]
    for type in types:
        marker_priority = item.get_closest_marker(type)
        if marker_priority:
            item.config._metadata["Test Type"] = marker_priority.name

            print(marker_priority)

    if "page" not in item.funcargs:
        return "page not in item.funcargs"
    page = item.funcargs["page"]

    if test_result.when in ["setup", "call"]:
        xfail = hasattr(test_result, 'wasxfail')
        if test_result.failed or (test_result.skipped and xfail):
            allure.attach(page.screenshot(), name='screenshot', attachment_type=allure.attachment_type.PNG)
            allure.attach(page.content(), name='html_source', attachment_type=allure.attachment_type.HTML)
