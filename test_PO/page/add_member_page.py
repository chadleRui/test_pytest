from selenium.webdriver.common.by import By

from test_PO.page.base_page import BasePage


class AddMember(BasePage):
    #模拟客户客户添加成员，添加完返回True
    def add_member_detail(self,username,acctid,phone):
        self.find(By.CSS_SELECTOR,'#username','send',username)
        self.find(By.CSS_SELECTOR,'#memberAdd_acctid','send',acctid)
        self.find(By.CSS_SELECTOR,'#memberAdd_phone','send',phone)
        self.find(By.CSS_SELECTOR,'.js_btn_save','click')
        return True

    #定义检查成员是否添加成功
    def check_add(self,username):
        #空的列表，用来存放下面遍历出来的联系人的名字
        total_titles=[]
        #调用显示等待方法
        locator=(By.CSS_SELECTOR,".ww_checkbox")
        self.wait_for_click(locator)
        print("这里做了显示等待哦！！！！~~~~~")
        while True:
            elements=self.finds(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
            #找到单页面的所有姓名，存入到列表中
            page_titles=[element.get_attribute("title") for element in elements]
            #如果要检查的姓名在当前页面的列表中则返回True
            if username in page_titles:
                return True
            #检查的姓名不在当前页面，将当前页面的所有姓名加入到total_titles列表中
            total_titles.extend(page_titles)
            #获取到总页码和当前页码，如果当前页码与总页码一致，此时仍未找到username，则放回False
            page:str=self.find(By.CSS_SELECTOR,".ww_pageNav_info_text").text
            num,sum=page.split("/",1)
            if int(num) == int(sum):
                return False
            #继续点击翻页按钮
            else:
                self.find(By.CSS_SELECTOR,".js_next_page","click")
        #返回总姓名列表
        return total_titles