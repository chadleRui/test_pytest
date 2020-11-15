from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    def __init__(self,driver:WebDriver=None):
        self.driver=driver

    def find(self,by,locator):
        return self.driver.find_element(by,locator)

    def finds(self,by,locator):
        return self.driver.find_elements(by,locator)

    def find_by_scroll(self,text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 f'.text("{text}").instance(0));')

