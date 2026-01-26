import time

from pages.cart_page import CartPage
from pages.product_page import ProductPage


class TestProductPage:
    def test_product_page(self, driver):
        product = ProductPage(driver)
        product.open()

        assert product.is_contact_us_displayed()
        assert product.get_product_name() == 'Office Design Software'
        assert product.get_product_price() == '280.00'

        product.add_to_cart()
        assert product.is_cart_not_empty()
        assert product.number_of_products_in_cart() == 1

