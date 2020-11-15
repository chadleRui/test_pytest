from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_app_po.page.base_page import BasePage


class EditContactDetail(BasePage):
    def remove_contact(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="删除成员"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="确定"]').click()
        from test_appium.test_app_po.page.search_contact import SearchContact
        return SearchContact(self.driver)