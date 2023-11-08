import allure

from pages.cart_page.page import CartPage
from pages.main_page.page import MainPage


@allure.title("Login test")
@allure.description("This test logs into the system and checks the opening of the main page")
def test_login(page):
    main_page = MainPage(page)
    main_page.load()
    assert main_page.is_product_title_visible(), "Product title is not visible"


@allure.title("Shopping cart test")
@allure.description("This test verifies that items are added and removed from the cart correctly")
def test_shopping_cart(page):
    main_page = MainPage(page)
    main_page.load()
    main_page.add_backpack_to_cart()
    expected_item_name = main_page.get_backpack_name_from_main_page()
    main_page.click_shopping_cart_button()
    cart_page = CartPage(page)
    actual_item_name = cart_page.get_backpack_name_from_cart()
    assert expected_item_name == actual_item_name, (f"Expected item name is {expected_item_name}, "
                                                    f"but actual item name is {actual_item_name}")
    items_count_before_removing = cart_page.get_count_of_items_in_cart()
    cart_page.remove_backpack_from_cart()
    items_count_after_removing = cart_page.get_count_of_items_in_cart()
    assert items_count_before_removing > items_count_after_removing, "Item not deleted"
