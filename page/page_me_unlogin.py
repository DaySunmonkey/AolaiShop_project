import allure
from selenium.webdriver.common.by import By

from AolaiShop_project import page
from AolaiShop_project.base.base_action import BaseAction


class PageMeUnlogin(BaseAction):

      go_login_button = By.ID,'com.yunmall.lc:id/textView1'


      @allure.step(title='点击去登录按钮')
      def click_go_login_button(self):
          self.base_click(self.go_login_button )