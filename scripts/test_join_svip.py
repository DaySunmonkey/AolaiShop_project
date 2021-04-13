from time import sleep

import pytest

from AolaiShop_project.base.base_driver import init_driver
from AolaiShop_project.base.get_yaml import analyze_file
from AolaiShop_project.page.page import PageEntrance

def get_data():
    analyze_file('data_svip.yaml','test_join_svip')

class TestVersionUpdate():

    def setup(self):
        self.driver = init_driver()
        self.page = PageEntrance(self.driver)

    def teardown(self):
        sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("args",get_data())
    def test_join_svip(self,args):

        keyword = args['keyword']
        toast = args['toast']

        #判断是否登录，没登录则先登录
        self.page.page_home.if_login(self.page)
        #点击加入超级VIP
        self.page.page_me.click_join_svip()
        #输入邀请码,点击加入
        self.page.page_svip.join_svip()
        assert self.page.page_svip.base_if_in_page_source('toast'),'{}不在page_source中'.format(toast)


#------------------------下面是涉及到webview的操作(以前百年奥莱版本)----------
    # @pytest.mark.parametrize("args",get_data())
    # def test_join_svip(self,args):
        # keyword = args['keyword']
        # toast = args['toast']
    #     # 判断是否登录，没登录则先登录
    #     self.page.page_home.if_login(self.page)
    #     # 点击加入超级VIP
    #     self.page.page_me.click_join_svip()
    #     #切换之前先打印所有环境名
    #     print(self.driver.contexts)
    #     #切换需要的web环境
    #     self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
    #     # 输入邀请码,点击加入
    #     self.page.page_svip.join_svip()

    #     assert self.page.page_svip.base_if_in_page_source('toast'),'{}不在page_source中'.format(toast)

    #     切换 回原生环境
    #     self.driver.switch_to.context('NATIVE_APP')


if __name__ == '__main__':
    pytest.main(['-s','test_join_svip.py'])