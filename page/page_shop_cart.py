import allure
from selenium.webdriver.common.by import By

from AolaiShop_project.base.base_action import BaseAction


class PageShopCart(BaseAction):

    # 选择商品按钮
    select_button = By.ID, 'com.yunmall.lc:id/tv_invalid_tag'
    #全选按钮
    all_select_button = By.ID,'com.yunmall.lc:id/iv_select_all'
    #编辑（完成）按钮
    edit_button = By.ID,'com.yunmall.lc:id/tv_right_second'
    #合计价格
    sum_price = By.ID,'com.yunmall.lc:id/tv_count_money'
    #单价
    single_price = By.ID,'com.yunmall.lc:id/tv_price'
    #数量增加按钮
    add_button = By.ID,'com.yunmall.lc:id/iv_add'
    # 数量减少按钮
    reduce_button = By.ID, 'com.yunmall.lc:id/iv_reduce'
    #删除按钮
    delete_button = By.ID,'com.yunmall.lc:id/tv_del_all'
    #确认按钮
    confirm_button = By.ID,'com.yunmall.lc:id/ymdialog_right_button'

    #选中某一款商品

    def click_select_button(self):
        eles = self.base_find_elements(self.select_button)
        eles_single = eles[0]
        eles_single.click()


    #点击全选
    @allure.step(title='点击全选按钮')
    def click_all_select(self):
        self.base_click(self.all_select_button)

    #点击编辑
    @allure.step(title='点击编辑按钮')
    def click_edit_button(self):
        self.base_click(self.edit_button)

    #点击增加
    @allure.step(title='点击增加按钮')
    def click_add_button(self):
        adds = self.base_find_elements(self.add_button)
        adds_single = adds[0]
        adds_single.click()

    #获取单价
    @allure.step(title='获取商品单价')
    def get_single_price(self):
        Prices = self.base_find_elements(self.single_price)
        pri = Prices[0].text
        return float(pri[2:])

    #获取总价
    @allure.step(title='获取总计价格')
    def get_sum_price(self):
        Price = self.base_get_text(self.sum_price)
        return float(Price[2:])

    #判断购物车是否为空
    @allure.step(title='判断购物车是否为空')
    def if_cart_null(self):
        return self.base_is_toast_exist('购物车还是空的')

    #点击删除按钮
    @allure.step(title='点击删除按钮')
    def click_delete_button(self):
        self.base_click(self.delete_button)

    #点击确认按钮
    @allure.step(title='点击确认按钮')
    def click_confirm_button(self):
        self.base_click(self.confirm_button)

    #增加商品数量看总价格会不会增加组合业务方法
    def page_shopcart_addprice(self):
        # 点击 选中一款商品
        self.click_select_button()
        # 获取当前总价
        sum1_price = self.get_sum_price()
        # print('+' * 20, sum1_price)
        # 点击编辑
        self.click_edit_button()
        # 点击增加
        self.click_add_button()
        # 点击完成
        self.click_edit_button()
        # 获取单价
        single_price = self.get_single_price()
        # print('+' * 20, single_price)
        # 获取现在总价
        sum2_price = self.get_sum_price()
        return sum1_price,single_price,sum2_price


    #清空购物车组合业务方法
    def clear_shopcart(self):
        self.click_edit_button()
        self.click_all_select()
        self.click_delete_button()
        self.click_confirm_button()








