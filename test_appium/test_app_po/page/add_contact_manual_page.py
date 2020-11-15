from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.test_app_po.page.base_page import BasePage


class AddByManual(BasePage):
    def add_by_manual(self,name,gender,phone):
        self.find(MobileBy.XPATH, '//*[contains(@text,"姓名")]/../android.widget.EditText').send_keys(name)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="性别"]/..//*[@text="男"]').click()
        if gender == "男":
            WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable((MobileBy.XPATH,"//*[@text='女']")))
            # WebDriverWait(self.driver,5).until(lambda x: x.find_element(MobileBy.XPATH,"//*[@text='女']"))
            self.driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="男"]').click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手机号"]').send_keys(phone)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()

        from test_appium.test_app_po.page.add_contact_page import AddContact
        return AddContact(self.driver)