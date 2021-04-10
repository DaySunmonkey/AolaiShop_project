from time import sleep

import pytest

from AolaiShop_project.base.base_driver import init_driver
from AolaiShop_project.page.page_entrance import  PageEntrance


class TestLogin():

    def setup(self):
        self.driver = init_driver()
        self.page = PageEntrance(self.driver)

    def teardown(self):
        sleep(2)
        self.driver.quit()

    def test_login(self):
        # self.page.page_enter_home.click_skip()
        sleep(5)
        self.page.page_home.click_me()

        self.page.page_me_unlogin.click_go_login_button()
        self.page.page_login.page_login('Aolai_test520','aolaitest520')
if __name__ == '__main__':
    pytest.main(['-s','test_login.py'])

