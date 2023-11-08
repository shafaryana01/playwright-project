from typing import Dict, Generator

import allure
import pytest
from playwright.sync_api import Browser, BrowserContext
from playwright.sync_api import Playwright, APIRequestContext

from config import USERNAME, PASSWORD
from pages.login_page.page import LoginPage


@pytest.fixture()
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        'viewport': {
            'width': 800,
            'height': 600,
        },
    }


@pytest.fixture()
def context(create_browser_context, browser: Browser, browser_context_args: Dict) -> Generator[
    BrowserContext, None, None]:
    context = browser.new_context(storage_state="state.json", **browser_context_args)
    yield context
    context.close()


@allure.step("Create Session")
@pytest.fixture(scope='session')
def create_browser_context(browser) -> None:
    context = browser.new_context()
    page = context.new_page()
    login_page = LoginPage(page)
    login_page.login(USERNAME, PASSWORD)
    context.storage_state(path="state.json")
    yield context, page
    context.close()

@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="https://petstore.swagger.io/"
    )
    yield request_context
    request_context.dispose()


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
