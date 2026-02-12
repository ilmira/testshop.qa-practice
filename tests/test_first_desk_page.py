from pages.first_desk_page import FirstDeskPage


class TestFirstDeskPage:
    def test_first_desk_page(self, first_desk: FirstDeskPage):
        first_desk.open()

        first_desk.check_is_contact_us_displayed('Contact Us')
        first_desk.check_is_cart_icon_displayed()
        first_desk.check_product_count(9)
