from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.locators.cart_page_locators import CartPageLocators


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def get_item_name(self):
        return self.get_text(CartPageLocators.ITEM_NAME)

    def get_items_count(self):
        item = self.page.locator(CartPageLocators.ITEM)
        return item.count()

    def remove_backpack_from_cart(self):
        self.click(CartPageLocators.REMOVE_BACKPACK_BUTTON)
