from pages.first_desk_page import FirstDeskPage


class TestFirstDeskPage:
    def test_first_desk_page(self, driver):
        first_desk = FirstDeskPage(driver)
        first_desk.open()

        assert first_desk.is_contact_us_displayed()
        assert first_desk.is_cart_icon_displayed()
        assert first_desk.get_product_count() == 9
        assert first_desk.select_first_product().text == 'Customizable Desk'
