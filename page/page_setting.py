import allure
from selenium.webdriver.common.by import By

from AolaiShop_project.base.base_action import BaseAction


class PageSetting(BaseAction):
    about_aolai_button = By.XPATH,'//*[@text="关于百年奥莱"]'

    address_manage_button = By.XPATH, '//*[@text="地址管理"]'

    #点击关于百年奥莱
    @allure.step(title='点击关于百年奥莱')
    def click_about_aolai(self):
        self.base_scroll_find_element(self.about_aolai_button).click()

    #点击 地址管理
    @allure.step(title='点击地址管理')
    def click_address_manage(self):
        self.base_scroll_find_element(self.address_manage_button).click()