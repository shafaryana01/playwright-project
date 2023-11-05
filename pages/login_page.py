from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def enter_username(self, username: str):
        self.fill(LoginPageLocators.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        self.fill(LoginPageLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
