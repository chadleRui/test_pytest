import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.test_app_po.page.base_page import BasePage
from test_appium.test_app_po.page.contact_detail import ContactDetail


class SearchContact(BasePage):
    def goto_search_name_detail(self,search_name):
        self.find(MobileBy.XPATH,'//*[@text="搜索"]').send_keys(search_name)
        # WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable((MobileBy.XPATH,f'//android.widget.TextView[contains(@text,"{search_name}")]')))
        names = self.driver.find_elements(MobileBy.XPATH, f'//android.widget.TextView[contains(@text,"{search_name}")]')

        if len(names) > 0:
            find_names = [name.get_attribute("text") for name in names]
            if search_name in find_names:
                self.driver.find_element(MobileBy.XPATH, f'//android.widget.TextView[@text="{search_name}"]').click()
                return ContactDetail(self.driver)
        else:
            return "no such name"
    def verify_name(self,search_name):
        # self.find(MobileBy.XPATH, '//*[@text="搜索"]').send_keys(search_name)
        WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable((MobileBy.XPATH, f'//android.widget.TextView[contains(@text,"{search_name}")]')))
        names = self.driver.find_elements(MobileBy.XPATH, f'//android.widget.TextView[contains(@text,"{search_name}")]')
        # time.sleep(2)
        find_names = [name.get_attribute("text") for name in names]
        if search_name in find_names:
            return "删除失败"
        else:
            return "删除成功"
