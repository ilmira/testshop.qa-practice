from pages.first_desk_page import FirstDeskPage


class TestFirstDeskPage:
    def test_first_desk_page(self, driver):
        first_desk = FirstDeskPage(driver)
        first_desk.open()

        products = first_desk.find_elements(first_desk.PRODUCTS)
        contact_us = first_desk.find_element(first_desk.CONTACT_US)

        assert contact_us and contact_us.text == 'Contact Us'
        assert len(products) == 9
        assert products[0].text == 'Customizable Desk'
        assert products[8].text == 'Desk Stand with Screen'
