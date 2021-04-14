import random
from time import sleep

import allure
from selenium.webdriver.common.by import By

from AolaiShop_project.base.base_action import BaseAction


class PageGoods(BaseAction):
    #具体商品
    specific_goods = By.ID,'com.yunmall.lc:id/iv_element_1'

    @allure.step(title='点击商品')
    def click_good(self):
        glist = self.base_find_elements(self.specific_goods)
        glist_count = len(glist)
        glist_index = random.randint(0, glist_count - 1)
        glist[glist_index].click()
        sleep(1)