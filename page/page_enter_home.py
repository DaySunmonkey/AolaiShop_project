from selenium.webdriver.common.by import By

from AolaiShop_project import page
from AolaiShop_project.base.base_action import BaseAction


class PageEnterHome(BaseAction):
    skip_button = By.ID,'com.yunmall.lc:id/view_mask'

    def click_skip(self):
        self.base_click(self.skip_button)