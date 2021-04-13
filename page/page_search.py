import allure
from selenium.webdriver.common.by import By

from AolaiShop_project.base.base_action import BaseAction


class PageSearch(BaseAction):
    #搜索输入框
    search_input = By.ID,'com.yunmall.lc:id/text_search_keyword'
    #搜索按钮
    search_button = By.ID,'com.yunmall.lc:id/button_search'

    #输入搜索内容
    @allure.step(title='输入搜索内容')
    def input_search(self,message):
        self.base_input(self.search_input,message)

    #点击搜索按钮
    @allure.step(title='点击搜索按钮')
    def click_search(self):
        self.base_click(self.search_button)

    #看搜索内容是不是在最近搜索里面
    @allure.step(title='看搜索内容是不是在最近搜索里面')
    def find_latest_search(self,message):
        # 最近搜索
        latest_search = By.XPATH, '//*[@resource-id="com.yunmall.lc:id/keyayout"]/*/*[@text="{}"]'.format(message)
        return self.base_if_elem_exist(latest_search)

    #组合业务方法
    def search(self,message):
        self.input_search(message)
        self.click_search()



