import random
from time import sleep

import allure
from selenium.webdriver.common.by import By

from AolaiShop_project.base.base_action import BaseAction


class PageCategory(BaseAction):
    #左侧类别列表
    category_list = By.ID,'com.yunmall.lc:id/tv_category_name'
    #右侧 商品
    goods = By.ID,'com.yunmall.lc:id/iv_img'

    @allure.step(title='点击选择类别')
    def select_category_click(self):
        Clist = self.base_find_elements(self.category_list)
        Clist_count = len(Clist)
        Clist_index = random.randint(0,Clist_count-1)
        Clist[Clist_index].click()
        sleep(1)

    @allure.step(title='点击商品类型')
    def select_goods_click(self):
        Glist = self.base_find_elements(self.goods)
        Glist_count = len(Glist)
        Glist_index = random.randint(0,Glist_count-1)
        Glist[Glist_index].click()
        sleep(1)