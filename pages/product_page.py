from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    PAGE_URL = 'http://testshop.qa-practice.com/shop/furn-9999-office-design-software-7?category=9'
    ADD_TO_CART = (By.ID, 'add_to_cart')
    NAME = (By.CSS_SELECTOR, 'h1[itemprop="name"]')
    PRICE = (By.CSS_SELECTOR, 'span[class="oe_currency_value"]')
    NOT_EMPTY_CART = (By.XPATH, "//sup[@class='my_cart_quantity badge text-bg-primary']")
    CART = (By.XPATH, "//a[@aria-label='eCommerce cart']")

    def add_to_cart(self):
        add_to_cart_button = self.find_element(self.ADD_TO_CART)
        self.click_element(add_to_cart_button)

    def go_to_cart(self):
        cart = self.find_element(self.CART)
        self.click_element(cart)

    def is_cart_not_empty(self):
        return self.find_element(self.NOT_EMPTY_CART).is_displayed()

    def number_of_products_in_cart(self):
        return self.find_element(self.NOT_EMPTY_CART).text

    def get_product_price(self):
        price_element = self.find_element(self.PRICE)
        return price_element.text

    def get_product_name(self):
        name_element = self.find_element(self.NAME)
        return name_element.text
