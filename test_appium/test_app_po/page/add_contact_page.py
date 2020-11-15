from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_app_po.page.base_page import BasePage


class AddContact(BasePage):
    def add_by_manual(self):
        self.find(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        #本地引用，解决PO中出现循环引用的场景
        from test_appium.test_app_po.page.add_contact_manual_page import AddByManual
        return AddByManual(self.driver)

    def verify_toast(self):
        result = self.find(MobileBy.XPATH,'//*[@class="android.widget.Toast"]').text
        return result