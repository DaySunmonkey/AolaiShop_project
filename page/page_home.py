from selenium.webdriver.common.by import By

from AolaiShop_project import page
from AolaiShop_project.base.base_action import BaseAction


class PageHome(BaseAction):

    me_button = By.ID,'com.yunmall.lc:id/tab_me'

    def click_me(self):
        self.base_click(self.me_button)