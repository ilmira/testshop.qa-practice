from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    PAGE_URL = '/shop/furn-9999-office-design-software-7?category=9'
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

    def check_is_cart_not_empty(self):
        assert self.find_element(self.NOT_EMPTY_CART).is_displayed()

    def check_number_of_products_in_cart(self, number):
        number_of_products_in_cart = self.find_element(self.NOT_EMPTY_CART)
        assert number_of_products_in_cart
        assert number_of_products_in_cart.text == number

    def check_product_price(self):
        price_of_element = self.find_element(self.PRICE)
        assert price_of_element
        assert price_of_element.text

    def check_product_name(self):
        name_of_element = self.find_element(self.NAME)
        assert name_of_element
        assert name_of_element.text
