from time import sleep

import pytest
from AolaiShop_project.base.get_yaml import analyze_file
from AolaiShop_project.base.base_driver import init_driver
from AolaiShop_project.page.page import  PageEntrance


def get_data():
    return analyze_file('data_login.yaml','test_login')

class TestLogin():

    def setup(self):
        self.driver = init_driver(no_reset=False)
        self.page = PageEntrance(self.driver)

    def teardown(self):
        sleep(2)
        self.driver.quit()


    # def test_if_login(self):
    #     self.page.page_home.if_login(self.page)

    @pytest.mark.parametrize("args",get_data())
    def test_login(self,args):
        #解析YAML数据
        username = args["username"]
        password = args["password"]
        toast = args["toast"]
        self.page.page_home.click_me()
        self.page.page_me_unlogin.click_go_login_button()
        self.page.page_login.page_login(username,password)
        sleep(2)
        if toast is None:
            assert self.page.page_me.get_username_text()=='Aolai_test520','登录前后用户名不一致!'
        else:
            assert self.page.page_login.page_toast_if_exist(toast)


    # @pytest.mark.parametrize("args",[{"username":"Aolai_test520", "password":"aolaitest520"}])
    # def test_login(self,args):
    #     username = args["username"]
    #     password = args["password"]
    #     self.page.page_home.click_me()
    #     self.page.page_me_unlogin.click_go_login_button()
    #     self.page.page_login.page_login(username,password)
    #     print('-*20',self.page.page_me.get_username_text())
    #     try:
    #         assert self.page.page_me.get_username_text() == 'Aolai_test520', '登录用户名前后不一致!'
    #         print('登录成功')
    #     except AssertionError as e:
    #         print('登录失败')


# if __name__ == '__main__':
#     pytest.main(['-s','test_login.py'])

