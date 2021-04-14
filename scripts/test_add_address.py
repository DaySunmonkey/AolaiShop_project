from time import sleep

import pytest

from AolaiShop_project.base.base_driver import init_driver
from AolaiShop_project.base.get_yaml import analyze_file
from AolaiShop_project.page.page import PageEntrance

def get_data():
    return analyze_file('data_adress.yaml','test_add_address')

class TestAddAddress():

    def setup(self):
        self.driver = init_driver()
        self.page = PageEntrance(self.driver)

    def teardown(self):
        sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize('args',get_data())
    def test_add_address(self,args):
        receiver = args['receiver']
        phone = args['phone']
        address = args['address']
        postcode = args['postcode']
        toast = args['toast']
        #没有登录先登录
        self.page.page_home.if_login(self.page)
        #点击设置
        self.page.page_me.click_setting_button()
        #点击地址管理
        self.page.page_setting.click_address_manage()
        count = self.page.page_address_list.find_address_list()
        #点击新增地址
        self.page.page_address_list.click_add_address()
        sleep(2)
        #组合输入地址信息
        self.page.page_add_address.add_address(receiver,phone,address,postcode)
        #断言
        if toast ==None:
            assert self.page.page_address_list.find_address_list()>count,'添加失败'
        else:
            assert self.page.page_add_address.if_toast_exist(toast),"保存失败，toast与预期不符"

# if __name__ == '__main__':
#     pytest.main(['-s','test_add_address.py'])

