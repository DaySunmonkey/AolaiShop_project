import allure
from selenium.webdriver.common.by import By

from AolaiShop_project.base.base_action import BaseAction


class PageSelectRegion(BaseAction):
    #省市区
    province_city_area = By.ID,'com.yunmall.lc:id/area_title'

    @allure.step(title='点击选择地区')
    def select_click_region(self):
        self.click_region