import allure
from playwright.sync_api import Page

from config import MAIN_PAGE_URL


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Opening url")
    def load(self):
        self.page.goto(MAIN_PAGE_URL)

    def click(self, locator: str):
        self.page.click(locator)

    def fill(self, locator: str, text: str):
        self.page.fill(locator, text)

    def get_text(self, locator: str):
        return self.page.text_content(locator)

    def is_element_visible(self, locator: str):
        return self.page.is_visible(locator)
