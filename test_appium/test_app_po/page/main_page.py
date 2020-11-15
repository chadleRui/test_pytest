from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_app_po.page.base_page import BasePage
from test_appium.test_app_po.page.contact_list_page import ContactList


class MainPage(BasePage):
    def goto_contacts_page(self):
        self.find(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        return ContactList(self.driver)