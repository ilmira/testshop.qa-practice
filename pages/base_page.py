from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By


class BasePage:
    CONTACT_US = (By.CSS_SELECTOR, 'a[href="/contactus"]')
    BASE_PAGE = 'http://testshop.qa-practice.com'
    PAGE_URL = ''

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(f'{self.BASE_PAGE}{self.PAGE_URL}')

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click_element(self, element):
        element = self.wait.until(EC.element_to_be_clickable(element))
        element.click()

    def check_is_contact_us_displayed(self):
        contact_us = self.find_element(self.CONTACT_US)
        assert contact_us.is_displayed() and contact_us.text == 'Contact Us'
