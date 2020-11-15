from test_appium.test_app_po.page.app import App


class TestAddContact:
    def setup_class(self):
        self.app = App()
    def setup(self):
        self.main=self.app.start().goto_main_page()

    def teardown(self):
        # self.app.stop()
        pass

    def test_add_contact(self):
        name="aaaa"
        gender="男"
        phone="13111111111"
        result=self.main.goto_contacts_page().add_contact().add_by_manual().add_by_manual(name,gender,phone).verify_toast()
        assert result == "添加成功"