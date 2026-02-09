from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class FirstDeskPage(BasePage):
    PAGE_URL = '/shop/category/desks-1'
    PRODUCTS = (By.CLASS_NAME, 'o_wsale_products_item_title.mb-2')
    FIRST_PRODUCT = (By.XPATH, "//a[@itemprop='name' and text()='Customizable Desk']")
    CART_ICON = (By.XPATH, "//a[@aria-label='eCommerce cart']")

    def check_product_count(self):
        products = self.find_elements(self.PRODUCTS)
        assert products
        assert len(products) == 9

    def check_first_product(self):
        first_product = self.find_element(self.FIRST_PRODUCT)
        assert first_product
        assert first_product.text == 'Customizable Desk'

    def check_is_cart_icon_displayed(self):
        assert self.find_element(self.CART_ICON).is_displayed()
