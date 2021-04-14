from time import sleep

import pytest

from AolaiShop_project.base.base_driver import init_driver
from AolaiShop_project.page.page import PageEntrance


class TestShopCart():
    def setup(self):
        self.driver = init_driver()
        self.page = PageEntrance(self.driver)

    def teardown(self):
        self.driver.quit()

    def shopcart_null_toadd(self):
        # 点击分类
        self.page.page_home.click_category()
        # 选择类别
        self.page.page_category.select_category_click()
        # 选择商品类型
        self.page.page_category.select_goods_click()
        # 选择商品
        self.page.page_goods.click_good()
        title = self.page.page_specific_good.get_title_text()
        self.page.page_specific_good.click_add_shop_cart()
        self.page.page_specific_good.select_type()
        #进入购物车页面
        self.page.page_specific_good.click_shop_cart_button()

    #增加商品数量看总价格会不会增加测试方法
    def test_add_price(self):
        #没有登录先登录
        self.page.page_home.if_login(self.page)
        #点击 购物车
        self.page.page_home.click_shopcart()
        #判断当前购物车是否为空
        if self.page.page_shop_cart.if_cart_null():
            #添加商品到购物车
            self.shopcart_null_toadd()
        #增加商品数量看总价格会不会增加组合业务方法
        price = self.page.page_shop_cart.page_shopcart_addprice()
        print(price)
        sum1_price = price[0]
        single_price = price[1]
        sum2_price = price[2]
        assert sum2_price == (sum1_price + single_price)

    #清空购物车测试方法
    def test_clear_shopcart(self):
        # 没有登录先登录
        self.page.page_home.if_login(self.page)
        # 点击 购物车
        self.page.page_home.click_shopcart()
        # 判断当前购物车是否为空
        if self.page.page_shop_cart.if_cart_null():
            # 添加商品到购物车
            self.shopcart_null_toadd()
        #清空购物车
        self.page.page_shop_cart.clear_shopcart()
        #断言
        assert self.page.page_shop_cart.if_cart_null()


if __name__ == '__main__':
    pytest.main(['-s', 'test_shop_cart.py'])

