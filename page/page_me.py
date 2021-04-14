from time import sleep

import allure
from selenium.webdriver.common.by import By

from AolaiShop_project import page
from AolaiShop_project.base.base_action import BaseAction


class PageMe(BaseAction):
    #用户名文本
    me_username_text = By.ID,'com.yunmall.lc:id/tv_user_nikename'
    #设置按钮
    setting_button = By.ID,'com.yunmall.lc:id/ymtitlebar_left_btn_image'
    #加入超级VIP
    join_svip = By.ID,'com.yunmall.lc:id/tv_my_shop_text'

    #首页按钮
    main_button = By.ID,'com.yunmall.lc:id/tab_home'

    #获取用户名文本
    def get_username_text(self):
        return self.base_get_text(self.me_username_text)

    # 点击首页按钮
    @allure.step(title='点击首页按钮')
    def click_main_button(self):
        self.base_click(self.main_button)

    #点击设置按钮
    def click_setting_button(self):
        self.base_click(self.setting_button)

    #点击加入超级VIP
    def click_join_svip(self):
        self.base_scroll_find_element(self.join_svip).click()
        sleep(2)