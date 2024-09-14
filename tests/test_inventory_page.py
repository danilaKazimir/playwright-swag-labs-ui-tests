class TestFooter:
    def test_twitter_link(self, inventory_page, login):
        inventory_page.open_twitter_link()

    def test_facebook_link(self, inventory_page, login):
        inventory_page.open_facebook_link()

    def test_linkedin_link(self, inventory_page, login):
        inventory_page.open_linkedin_link()

    def test_footer_copyright_text(self, inventory_page, login):
        inventory_page.check_footer_copyright_text()
