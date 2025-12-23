from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    PAGE_URL = 'http://testshop.qa-practice.com/shop/cart'
    ORDER_OVERVIEW = By.CLASS_NAME, 'mb-4'
    EMPTY_CART = By.CLASS_NAME, 'js_cart_lines.alert.alert-info'


