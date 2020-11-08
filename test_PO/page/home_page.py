from selenium.webdriver.common.by import By

from test_PO.page.add_member_page import AddMember
from test_PO.page.base_page import BasePage

#主页继承基类，会自动加载基类的初始化方法，传一个主页的URL过去即可
class HomePage(BasePage):
    baseurl = "https://work.weixin.qq.com/wework_admin/frame#index"
    #定位到添加成员的元素，点击，然后return跳转到添加成员页面
    def add_member(self):
        self.find(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(1)","click")
        return AddMember(self.driver)