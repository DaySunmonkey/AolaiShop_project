from selenium.webdriver.common.by import By

from AolaiShop_project import page
from AolaiShop_project.base.base_action import BaseAction


class PageLogin(BaseAction):

    username = By.ID,'com.yunmall.lc:id/logon_account_textview'
    password = By.ID,'com.yunmall.lc:id/logon_password_textview'
    login_button = By.ID,'com.yunmall.lc:id/logon_button'

    def page_input_username(self,username):
        self.base_input(self.username,username)

    def page_input_password(self,password):
        self.base_input(self.password,password)

    def page_click_login_button(self):
        self.base_click(self.login_button)


    #组合业务方法
    def page_login(self,username,password):
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_button()