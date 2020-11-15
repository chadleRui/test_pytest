from appium import webdriver

from test_appium.test_app_po.page.base_page import BasePage
from test_appium.test_app_po.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            caps={}
            caps["platformName"] = "Android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "True"
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()

    def goto_main_page(self):
        return MainPage(self.driver)