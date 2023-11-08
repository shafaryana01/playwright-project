import allure
from playwright.sync_api import Page

from config import LOGIN_PAGE_URL
from pages.base_page import BasePage
from pages.login_page.locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Entering username")
    def enter_username(self, username: str):
        self.fill(LoginPageLocators.USERNAME_INPUT, username)

    @allure.step("Entering password")
    def enter_password(self, password: str):
        self.fill(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Clicking login button")
    def click_login_button(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Login to the system")
    def login(self, username, password):
        self.page.goto(LOGIN_PAGE_URL)
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
