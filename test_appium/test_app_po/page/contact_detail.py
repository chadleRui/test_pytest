from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_app_po.page.base_page import BasePage
from test_appium.test_app_po.page.detail_more_options_page import DetailMoreOps


class ContactDetail(BasePage):
    def goto_more(self):
        self.driver.find_element(MobileBy.XPATH,
                                         '//*[@text="个人信息"]/../../../../..//android.widget.LinearLayout[2]//android.widget.TextView').click()
        return DetailMoreOps(self.driver)