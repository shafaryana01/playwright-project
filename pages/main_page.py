from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def add_backpack_to_card(self):
        self.click(MainPageLocators.ADD_BACKPACK_TO_CARD_BUTTON)

    def get_item_name(self):
        return self.get_text(MainPageLocators.ITEM_NAME)

    def click_shopping_cart(self):
        self.click(MainPageLocators.SHOPPING_CART_BUTTON)
