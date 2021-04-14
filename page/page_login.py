import allure
from selenium.webdriver.common.by import By

from AolaiShop_project import page
from AolaiShop_project.base.base_action import BaseAction


class PageLogin(BaseAction):

    username = By.ID,'com.yunmall.lc:id/logon_account_textview'
    password = By.ID,'com.yunmall.lc:id/logon_password_textview'
    login_button = By.ID,'com.yunmall.lc:id/logon_button'

    @allure.step(title='输入用户名')
    def page_input_username(self,username):
        self.base_input(self.username,username)

    @allure.step(title='输入密码')
    def page_input_password(self,password):
        self.base_input(self.password,password)

    @allure.step(title='点击登录按钮')
    def page_click_login_button(self):
        self.base_click(self.login_button)

    @allure.step(title='判断是否有toast提示')
    def page_toast_if_exist(self,toast):
        return self.base_is_toast_exist(toast)

    @allure.step(title='获取toast提示信息')
    def page_get_toast_text(self,toast):
        return self.base_get_toast_text(toast)


    #组合业务方法
    def page_login(self,username,password):
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_button()