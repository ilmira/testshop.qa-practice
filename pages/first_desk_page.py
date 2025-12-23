from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class FirstDeskPage(BasePage):
    PAGE_URL = 'http://testshop.qa-practice.com/shop/category/desks-1'
    PRODUCTS = By.CLASS_NAME, 'o_wsale_products_item_title.mb-2'

