from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class FirstDeskPage(BasePage):
    PAGE_URL = '/shop/category/desks-1'
    PRODUCTS = (By.CLASS_NAME, 'o_wsale_products_item_title.mb-2')
    CART_ICON = (By.XPATH, "//a[@aria-label='eCommerce cart']")

    def check_product_count(self, count):
        products = self.find_elements(self.PRODUCTS)
        assert products
        assert len(products) == count

    def check_is_cart_icon_displayed(self):
        assert self.find_element(self.CART_ICON).is_displayed()
