from test_appium.test_app_po.page.app import App


class TestAddContact:
    def setup_class(self):
        self.app = App()
    def setup(self):
        self.main=self.app.start().goto_main_page()

    def teardown(self):
        # self.app.stop()
        pass

    def test_del_contact(self):
        search_name="aaaa"
        result=self.main.goto_contacts_page().click_search().goto_search_name_detail(search_name).goto_more().goto_edit().remove_contact().verify_name(search_name)
        assert result == "删除成功"