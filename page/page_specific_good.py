import random
from time import sleep

import allure
from selenium.webdriver.common.by import By

from AolaiShop_project.base.base_action import BaseAction


class PageSpecificGood(BaseAction):

    #加入购物车按钮
    add_shop_cart = By.XPATH,'//*[@text="加入购物车"]'

    #toast文本
    toast_text = By.XPATH,'//*[contains(@text,"成功加入购物车")]'

    #确认按钮
    confirm_button = By.XPATH,'//*[@text="确认"]'

    #购物车按钮
    shop_cart_button = By.ID,'com.yunmall.lc:id/btn_shopping_cart'

    #商品标题
    good_title = By.ID,'com.yunmall.lc:id/tv_product_title'

    #点击加入购物车按钮
    @allure.step(title='点击加入购物车按钮')
    def click_add_shop_cart(self):
        self.base_click(self.add_shop_cart)

    #点击确认按钮
    @allure.step(title='点击确认按钮')
    def click_confirm(self):
        self.base_click(self.confirm_button)

    #点击购物车按钮
    @allure.step(title='点击购物车按钮')
    def click_shop_cart_button(self):
        self.base_click(self.shop_cart_button)
        sleep(1)

    #获取商品标题
    @allure.step(title='获取商品标题')
    def get_title_text(self):
        return self.base_get_text(self.good_title)

    #根据获取的toast 找到商品第一种规格（类型）
    @allure.step(title='根据获取的toast 找到商品第一种规格（类型）')
    def select_specific_type(self,text):
        return text.split(' ')[1]

    @allure.step(title='选择规格')
    def select_type(self):
        while True:
            self.click_confirm()
            if self.if_toast_exist():
                type_name = self.select_specific_type(self.get_toast_info())
                type_xpath = By.XPATH,'//*[@text="{}"]/../*[2]/*[1]'.format(type_name)
                self.base_click(type_xpath)
                sleep(2)
            else:
                break

    @allure.step(title='判断是否有toast提示')
    def if_toast_exist(self):
        return self.base_is_toast_exist('请选择')

    @allure.step(title='获取toast提示文本')
    def get_toast_info(self):
        return self.base_get_toast_text('请选择')

