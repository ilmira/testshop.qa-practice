from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    PAGE_URL = '/shop/cart'
    ORDER_OVERVIEW = (By.CLASS_NAME, 'mb-4')
    EMPTY_CART = (By.CLASS_NAME, 'js_cart_lines.alert.alert-info')
    REVIEW_ORDER = (By.XPATH, "//p[text()='Review Order']")
    SHIPPING = (By.XPATH, "//p[text()='Shipping']")
    PAYMENT = (By.XPATH, "//p[text()='Payment']")
    REMOVE = (By.XPATH, "//a[@class='js_delete_product' and @title='Remove from cart']")
    CHECKOUT = (By.XPATH, "//a[@name='website_sale_main_button' and text()='Checkout']")

    def remove_items(self):
        remove_buttons = self.find_elements(self.REMOVE)
        if remove_buttons:
            self.click_element(remove_buttons[0])

    def check_is_checkout_button_visible(self):
        assert self.find_element(self.CHECKOUT).is_displayed()

    def check_cart_alert_text(self, text):
        assert self.find_element(self.EMPTY_CART).text == text

    def check_order_overview_text(self):
        assert self.find_element(self.ORDER_OVERVIEW).text == 'Order overview'

    def check_cart_shipping(self):
        assert self.find_element(self.SHIPPING).is_displayed()

    def check_cart_payment(self):
        assert self.find_element(self.PAYMENT).is_displayed()

    def check_cart_review_order(self):
        assert self.find_element(self.REVIEW_ORDER).is_displayed()
