from time import sleep

import pytest

from AolaiShop_project.base.base_driver import init_driver
from AolaiShop_project.base.get_yaml import analyze_file
from AolaiShop_project.page.page import PageEntrance

def get_data():
    return analyze_file('data_search.yaml','test_search')

class TestSearch():
    def setup(self):
        self.driver = init_driver()
        self.page = PageEntrance(self.driver)

    def teardown(self):
        sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize('args',get_data())
    def test_search(self,args):
        message = args['message']
        # 没有登录先登录
        self.page.page_home.if_login(self.page)
        #点击首页
        self.page.page_me.click_main_button()
        #点击放大镜搜索
        self.page.page_home.click_search_button()
        #组合搜索业务方法
        self.page.page_search.search(message)
        #点击系统返回键
        self.page.page_search.base_return_key()
        #断言
        assert self.page.page_search.find_latest_search(message)

# if __name__ == '__main__':
#     pytest.main(['-s', 'test_search.py'])