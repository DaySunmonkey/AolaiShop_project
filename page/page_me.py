from selenium.webdriver.common.by import By

from AolaiShop_project import page
from AolaiShop_project.base.base_action import BaseAction


class PageMe(BaseAction):
    me_username_text = By.ID,'com.yunmall.lc:id/tv_user_nikename'


    def get_username_text(self):
        return self.base_get_text(self.me_username_text)