from pages.product_page import ProductPage


class TestProductPage:
    def test_product_page(self, product: ProductPage):
        product.open()

        product.check_is_contact_us_displayed()
        product.check_product_name()
        product.check_product_price()

        product.add_to_cart()
        product.check_is_cart_not_empty()
        product.check_number_of_products_in_cart()
