import allure
from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.main_page.locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Adding backpack to cart")
    def add_backpack_to_cart(self):
        self.click(MainPageLocators.ADD_BACKPACK_TO_CARD_BUTTON)

    @allure.step("Getting backpack name from main page")
    def get_backpack_name_from_main_page(self):
        return self.get_text(MainPageLocators.ITEM_NAME)

    @allure.step("Clicking shopping cart button")
    def click_shopping_cart_button(self):
        self.click(MainPageLocators.SHOPPING_CART_BUTTON)

    @allure.step("Checking whether product title is visible")
    def is_product_title_visible(self):
        return self.is_element_visible(MainPageLocators.PRODUCT_TITLE)
