from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_app_po.page.base_page import BasePage
from test_appium.test_app_po.page.edit_contact_detail import EditContactDetail


class DetailMoreOps(BasePage):
    def goto_edit(self):
        self.find(MobileBy.XPATH, '//*[@text="编辑成员"]').click()
        return EditContactDetail(self.driver)