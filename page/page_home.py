import allure
from selenium.webdriver.common.by import By

from AolaiShop_project import page
from AolaiShop_project.base.base_action import BaseAction


class PageHome(BaseAction):
    #我的页面按钮
    me_button = By.ID,'com.yunmall.lc:id/tab_me'

    #分类页面按钮
    category_button = By.ID,'com.yunmall.lc:id/tab_category'

    #购物车页面按钮
    shopcart_button = By.ID,'com.yunmall.lc:id/tab_shopping_cart'

    #放大镜搜索按钮
    search_button = By.ID,'com.yunmall.lc:id/ymtitlebar_left_btn_image'

    #点击我的
    @allure.step(title='点击我的页面')
    def click_me(self):
        self.base_click(self.me_button)

    # 点击分类
    @allure.step(title='点击分类页面')
    def click_category(self):
        self.base_click(self.category_button)

    # 点击购物车
    @allure.step(title='点击购物车页面')
    def click_shopcart(self):
        self.base_click(self.shopcart_button)

    #点击放大镜搜索
    @allure.step(title='点击放大镜搜索')
    def click_search_button(self):
        self.base_click(self.search_button)

    #判断是否登录，没登录就先登录
    @allure.step(title='判断是否登录，没登录就先登录')
    def if_login(self,page):
        self.click_me()
        if self.driver.current_activity !="com.yunmall.ymctoc.ui.activity.LogonActivity":
            return
        else:
            #没有登录，就去登录
            page.page_me_unlogin.click_go_login_button()
            #登录
            page.page_login.page_login('Aolai_test520', 'aolaitest520')

