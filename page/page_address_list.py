import allure
from selenium.webdriver.common.by import By

from AolaiShop_project.base.base_action import BaseAction


class PageAddressList(BaseAction):
    add_address = By.XPATH,'//*[@text="新增地址"]'

    address_list = By.CLASS_NAME,'android.widget.LinearLayout'

    @allure.step(title='点击 新增地址')
    def click_add_address(self):
        self.base_scroll_find_element(self.add_address).click()

    @allure.step(title='查看地址数量')
    def find_address_list(self):
        try:
            alist = self.base_find_elements(self.address_list)
            alist_count = len(alist)
            return alist_count
        except Exception:
            alist_count = 0
            return alist_count