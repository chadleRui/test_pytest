from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDelContact:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "True"

        self.driver=webdriver.Remote("http://localhost:4723/wd/hub",caps)
        self.driver.implicitly_wait(10)

    def test_del_contact(self):
        # find_name=[]
        search_name="aaaa"
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="测试测试测试公司"]/../../../../..//android.widget.RelativeLayout[1]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="搜索"]').send_keys(search_name)
        names=self.driver.find_elements(MobileBy.XPATH,f'//android.widget.TextView[contains(@text,"{search_name}")]')
        if len(names) >0:
            find_names=[name.get_attribute("text") for name in names]
            if search_name in find_names:
                self.driver.find_element(MobileBy.XPATH, f'//android.widget.TextView[@text="{search_name}"]').click()
                self.driver.find_element(MobileBy.XPATH,'//*[@text="个人信息"]/../../../../..//android.widget.LinearLayout[2]//android.widget.TextView').click()
                self.driver.find_element(MobileBy.XPATH,'//*[@text="编辑成员"]').click()
                self.driver.find_element(MobileBy.XPATH,'//*[@text="删除成员"]').click()
                self.driver.find_element(MobileBy.XPATH,'//*[@text="确定"]').click()
                new_names=self.driver.find_elements(MobileBy.XPATH,f'//android.widget.TextView[contains(@text,"{search_name}")]')
                if search_name not in new_names:
                    print(f"删除{search_name}成功")
                    assert True
                else:
                    print("删除失败，请重新删除")
                    assert False
            else:
                print(f"{find_names}没有你要的名字哦，重新输入一次试试看")
                return False
