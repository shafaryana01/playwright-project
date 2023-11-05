from playwright.sync_api import Page

from config import URL


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def load(self):
        self.page.goto(URL)

    def click(self, locator: str):
        self.page.click(locator)

    def fill(self, locator: str, text: str):
        self.page.fill(locator, text)

    def get_text(self, locator: str):
        return self.page.text_content(locator)

