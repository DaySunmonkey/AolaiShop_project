from time import sleep

import pytest

from AolaiShop_project.base.base_driver import init_driver
from AolaiShop_project.page.page import PageEntrance


class TestVersionUpdate():

    def setup(self):
        self.driver = init_driver()
        self.page = PageEntrance(self.driver)

    def teardown(self):
        sleep(2)
        self.driver.quit()

    def test_version_update(self):
        #如果没有登录，就先登录
        self.page.page_home.if_login(self.page)
        #我-点击设置
        self.page.page_me.click_setting_button()
        #设置-点击关于百年奥莱
        self.page.page_setting.click_about_aolai()
        #关于-点击版本更新
        self.page.page_about_aolai.click_version_update()
        #断言是否是最新版本
        assert self.page.page_about_aolai.toast_if_exist()

if __name__ == '__main__':
    pytest.main(['-s','test_version_update.py'])