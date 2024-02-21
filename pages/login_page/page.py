import allure
from playwright.sync_api import Page

from config import LOGIN_PAGE_URL
from pages.base_page import BasePage
from pages.login_page.locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.USERNAME_INPUT = page.locator(LoginPageLocators.USERNAME_INPUT)
        self.PASSWORD_INPUT = page.locator(LoginPageLocators.PASSWORD_INPUT)
        self.LOGIN_BUTTON = page.locator(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Entering username")
    def enter_username(self, username: str):
        self.USERNAME_INPUT.fill(username)

    @allure.step("Entering password")
    def enter_password(self, password: str):
        self.PASSWORD_INPUT.fill(password)

    @allure.step("Clicking login button")
    def click_login_button(self):
        self.LOGIN_BUTTON.click()

    @allure.step("Login to the system")
    def login(self, username, password):
        self.page.goto(LOGIN_PAGE_URL)
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
