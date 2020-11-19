import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    search_params= []
    def __init__(self,driver:WebDriver=None):
        with open("../page/browser_page.yaml",encoding="utf-8") as f:
            browser_page=yaml.safe_load(f)
            if driver==None:
                if 'chrome' in str(browser_page):
                    self.driver=webdriver.Chrome()
                elif 'firefox' in str(browser_page):
                    self.driver=webdriver.Firefox()
                else:
                    print("chrome&firefox browser only")
            else:
                self.driver=driver


            self.driver.get(browser_page[0]['page'])
            # print(self.base_url)
        self.driver.implicitly_wait(3)

    def find(self,by,locator):
        element=self.driver.find_element(by,locator)
        return element

    def send(self,by,locator,value):
        element=self.find(by,locator).send_keys(value)
        return element

    def steps(self,path):
        with open(path,encoding="utf-8") as f:
            steps=yaml.safe_load(f)
            # print(steps)
            for step in steps:
                if 'by' in step.keys():
                    # print(f"{step['by']} and {step['locator']}")
                    element=self.find(step['by'],step['locator'])
                if 'action' in step.keys():
                    if step['action'] =='click':
                        element.click()
                    if step['action'] =='send':
                        # print(self.search_params)
                        for param in self.search_params:
                            # print(f"step['value']before====={step['value']}")
                            # print(f"param before====={param}")
                            step['value']=str(step['value']).replace("{value}",param)
                            # print(f"step['value']after====={step['value']}")
                        self.send(step['by'],step['locator'],step['value'])