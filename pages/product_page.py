from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    PAGE_URL = 'http://testshop.qa-practice.com/shop/furn-9999-office-design-software-7?category=9'
    ADD_TO_CART = By.ID, 'add_to_cart'
    NAME = By.CSS_SELECTOR, 'h1[itemprop="name"]'
    PRICE = By.CSS_SELECTOR, 'span[class="oe_currency_value"]'
