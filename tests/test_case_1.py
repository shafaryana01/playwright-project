from config import USERNAME, PASSWORD
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_case_1(login_page: LoginPage, main_page: MainPage, cart_page: CartPage):
    login_page.load()
    login_page.login(USERNAME, PASSWORD)
    main_page.add_backpack_to_card()
    expected_item_name = main_page.get_item_name()
    main_page.click_shopping_cart()
    actual_item_name = cart_page.get_item_name()
    assert expected_item_name == actual_item_name, (f"Expected item name is {expected_item_name}, "
                                                    f"but actual item name is {actual_item_name}")
    items_count_before_removing = cart_page.get_items_count()
    cart_page.remove_backpack_from_cart()
    items_count_after_removing = cart_page.get_items_count()
    assert items_count_before_removing > items_count_after_removing, "Item not deleted"
