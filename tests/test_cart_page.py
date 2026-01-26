from pages.cart_page import CartPage
from pages.product_page import ProductPage


class TestCartPage:
    def test_cart_page(self, driver):
        cart = CartPage(driver)
        product = ProductPage(driver)

        empty_cart_text = cart.find_element(cart.EMPTY_CART).text
        order_overview_text = cart.find_element(cart.ORDER_OVERVIEW).text

        assert cart.is_contact_us_displayed()
        assert empty_cart_text == 'Your cart is empty!'
        assert order_overview_text == 'Order overview'

        product.open()
        product.add_to_cart()
        product.is_cart_not_empty()

        cart.open()

        assert cart.is_checkout_button_visible()

        cart.remove_items()

        assert empty_cart_text == 'Your cart is empty!'

        assert cart.find_element(cart.REVIEW_ORDER).is_displayed()
        assert cart.find_element(cart.SHIPPING).is_displayed()
        assert cart.find_element(cart.PAYMENT).is_displayed()
