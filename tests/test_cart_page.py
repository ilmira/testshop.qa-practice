class TestCartPage:
    def test_cart_page(self, cart, product):
        cart.open()
        cart.check_is_contact_us_displayed()
        cart.check_empty_cart_text()

        product.open()
        product.add_to_cart()
        product.is_cart_not_empty()

        cart.open()

        cart.check_is_checkout_button_visible()

        cart.remove_items()

        cart.check_empty_cart_text()

        cart.check_cart_shipping()
        cart.check_cart_payment()
        cart.check_cart_review_order()
