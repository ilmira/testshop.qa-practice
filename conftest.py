import pytest
from selenium import webdriver

from pages.cart_page import CartPage
from pages.first_desk_page import FirstDeskPage
from pages.product_page import ProductPage


@pytest.fixture(autouse=True)
def driver(request):
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def cart(driver):
    return CartPage(driver)


def product(driver):
    return ProductPage(driver)


def first_desk(driver):
    return FirstDeskPage(driver)
