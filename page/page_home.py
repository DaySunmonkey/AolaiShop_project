from selenium.webdriver.common.by import By

from AolaiShop_project import page
from AolaiShop_project.base.base_action import BaseAction


class PageHome(BaseAction):

    me_button = By.ID,'com.yunmall.lc:id/tab_me'

    def click_me(self):
        self.base_click(self.me_button)

    def if_login(self,page):
        self.click_me()
        if self.driver.current_activity !="com.yunmall.ymctoc.ui.activity.LogonActivity":
            return
        else:
            #没有登录，就去登录
            page.page_me_unlogin.click_go_login_button()
            #登录
            page.page_login.page_login('Aolai_test520', 'aolaitest520')

