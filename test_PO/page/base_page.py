from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

#定义基类，里面有初始化方法，和基本的点击和发送方法，便于其他po继承和使用
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    #定义一个初始为空的url
    baseurl=""
    #定义一个初始化方法，用来启动driver,默认为none意味着只在第一次生成driver，后面就可以复用同一个driver，不用每个po都启动一个新的
    def __init__(self,driver:WebDriver=None):
        if driver == None:
            #通过Chrome的options，复用浏览器
            option = Options()
            option.debugger_address="127.0.0.1:9222"
            self.driver=webdriver.Chrome(options=option)
            self.driver.implicitly_wait(5)
        else:
            self.driver=driver
        #其他po类会重写baseurl属性，这样就完成页面跳转了
        if self.baseurl != "":
            self.driver.get(self.baseurl)

    #定义一个找元素的方法，action和value可以用来做元素的操作
    def find(self,by,locator,action=None,value=None):
        element=self.driver.find_element(by,locator)
        if action == "click":
            element.click()
        if action == "send":
            element.send_keys(value)
        return element

    #同上，用来找元素，不过是找到多个元素
    def finds(self,by,locator):
        return self.driver.find_elements(by,locator)

    def wait_for_click(self,locator,timeout=10):
        WebDriverWait(self.driver,timeout).until(expected_conditions.element_to_be_clickable(locator))
