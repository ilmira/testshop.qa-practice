from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class FirstDeskPage(BasePage):
    PAGE_URL = 'http://testshop.qa-practice.com/shop/category/desks-1'
    PRODUCTS = (By.CLASS_NAME, 'o_wsale_products_item_title.mb-2')
    FIRST_PRODUCT = (By.XPATH, "//a[@itemprop='name' and text()='Customizable Desk']")
    CART_ICON = (By.XPATH, "//a[@aria-label='eCommerce cart']")

    def get_product_count(self):
        products = self.find_elements(self.PRODUCTS)
        return len(products)

    def select_first_product(self):
        return self.find_element(self.FIRST_PRODUCT)

    def is_cart_icon_displayed(self):
        return self.find_element(self.CART_ICON).is_displayed()

