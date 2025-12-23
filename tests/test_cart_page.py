from pages.cart_page import CartPage


class TestCartPage:
    def test_cart_page(self, driver):
        cart = CartPage(driver)
        cart.open()
        empty_cart_text = cart.find_element(cart.EMPTY_CART).text
        order_overview_text = cart.find_element(cart.ORDER_OVERVIEW).text
        contact_us = cart.find_element(cart.CONTACT_US)

        assert empty_cart_text == 'Your cart is empty!'
        assert order_overview_text == 'Order overview'
        assert contact_us and contact_us.text == 'Contact Us'
