from time import sleep

import pytest

from AolaiShop_project.base.base_driver import init_driver
from AolaiShop_project.base.get_yaml import analyze_file
from AolaiShop_project.page.page import PageEntrance



class TestAddShopCart():

    def setup(self):
        self.driver = init_driver()
        self.page = PageEntrance(self.driver)

    def teardown(self):
        sleep(2)
        self.driver.quit()

    def test_add_shop_cart(self):
        #没有登录先登录
        self.page.page_home.if_login(self.page)
        #点击分类
        self.page.page_home.click_category()
        #选择类别
        self.page.page_category.select_category_click()
        #选择商品类型
        self.page.page_category.select_goods_click()
        #选择商品
        self.page.page_goods.click_good()
        title = self.page.page_specific_good.get_title_text()
        self.page.page_specific_good.click_add_shop_cart()
        self.page.page_specific_good.select_type()
        self.page.page_specific_good.click_shop_cart_button()
        assert self.page.page_specific_good.base_if_element_exist(title)

# if __name__ == '__main__':
#     pytest.main(['-s','test_add_shop_cart.py'])