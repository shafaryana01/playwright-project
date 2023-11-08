import allure
from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.cart_page.locators import CartPageLocators


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Getting backpack name from cart")
    def get_backpack_name_from_cart(self):
        return self.get_text(CartPageLocators.ITEM_NAME)

    @allure.step("Getting count of items in cart")
    def get_count_of_items_in_cart(self):
        item = self.page.locator(CartPageLocators.ITEM)
        return item.count()

    @allure.step("Removing backpack from cart")
    def remove_backpack_from_cart(self):
        self.click(CartPageLocators.REMOVE_BACKPACK_BUTTON)
