from pages.product_page import ProductPage


class TestProductPage:
    def test_product_page(self, driver):
        product = ProductPage(driver)
        product.open()

        add_to_cart = product.find_element(product.ADD_TO_CART)
        contact_us = product.find_element(product.CONTACT_US)
        name = product.find_element(product.NAME)
        price = product.find_element(product.PRICE)

        assert contact_us and contact_us.text == 'Contact Us'
        assert add_to_cart and add_to_cart.text == 'Add to cart'
        assert name.text == 'Office Design Software'
        assert price.text == '280.00'
