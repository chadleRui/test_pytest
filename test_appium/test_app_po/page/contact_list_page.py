from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_app_po.page.add_contact_page import AddContact
from test_appium.test_app_po.page.base_page import BasePage
from test_appium.test_app_po.page.search_contact import SearchContact


class ContactList(BasePage):
    def add_contact(self):
        self.find_by_scroll("添加成员").click()
        return AddContact(self.driver)
    def click_search(self):
        self.find(MobileBy.XPATH,'//*[@text="测试测试测试公司"]/../../../../..//android.widget.RelativeLayout[1]').click()
        return SearchContact(self.driver)