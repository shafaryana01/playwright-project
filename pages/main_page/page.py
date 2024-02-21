
import allure
from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.main_page.locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.PRODUCT_TITLE = page.locator(MainPageLocators.PRODUCT_TITLE)
        self.ADD_BACKPACK_TO_CARD_BUTTON = page.locator(MainPageLocators.ADD_BACKPACK_TO_CARD_BUTTON)
        self.ITEM_NAME = page.locator(MainPageLocators.ITEM_NAME)
        self.SHOPPING_CART_BUTTON = page.locator(MainPageLocators.SHOPPING_CART_BUTTON)

    @allure.step("Adding backpack to cart")
    def add_backpack_to_cart(self):
        self.ADD_BACKPACK_TO_CARD_BUTTON.click()

    @allure.step("Getting backpack name from main page")
    def get_backpack_name_from_main_page(self):
        return self.ITEM_NAME.text_content()

    @allure.step("Clicking shopping cart button")
    def click_shopping_cart_button(self):
        self.SHOPPING_CART_BUTTON.click()

    @allure.step("Checking whether product title is visible")
    def is_product_title_visible(self):
        return self.PRODUCT_TITLE.is_visible()
