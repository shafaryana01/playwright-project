import allure
from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.cart_page.locators import CartPageLocators


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.ITEM_NAME = page.locator(CartPageLocators.ITEM_NAME)
        self.ITEM = page.locator(CartPageLocators.ITEM)
        self.REMOVE_BACKPACK_BUTTON = page.locator(CartPageLocators.REMOVE_BACKPACK_BUTTON)

    @allure.step("Getting backpack name from cart")
    def get_backpack_name_from_cart(self):
        return self.ITEM_NAME.text_content()

    @allure.step("Getting count of items in cart")
    def get_count_of_items_in_cart(self):
        item = self.ITEM
        return item.count()

    @allure.step("Removing backpack from cart")
    def remove_backpack_from_cart(self):
        self.REMOVE_BACKPACK_BUTTON.click()
