from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAddContact:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "True"

        self.driver=webdriver.Remote("http://localhost:4723/wd/hub",caps)
        self.driver.implicitly_wait(10)

    def test_add_contact(self):
        name="aaaa"
        gender="男"
        phone="13111111111"
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"姓名")]/../android.widget.EditText').send_keys(name)
        self.driver.find_element(MobileBy.XPATH,'//*[@text="性别"]/..//*[@text="男"]').click()
        if gender == "男":
            self.driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="男"]').click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="手机号"]').send_keys(phone)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()


        assert self.driver.find_element(MobileBy.XPATH,'//*[@class="android.widget.Toast"]').text == "添加成功"