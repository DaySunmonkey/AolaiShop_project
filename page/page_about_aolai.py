from time import sleep

from selenium.webdriver.common.by import By

from AolaiShop_project.base.base_action import BaseAction


class PageAboutAolai(BaseAction):
    version_update_button = By.XPATH,'//*[@text="版本更新"]'

    def click_version_update(self):
        self.base_click(self.version_update_button)
        # sleep(1)

    def toast_if_exist(self):
        return self.base_is_toast_exist("当前已是最新版本")