from selenium.webdriver.common.by import By


from AolaiShop_project.base.base_action import BaseAction


class PageSvip(BaseAction):
    invitecode = By.XPATH,'//*[@class="android.widget.EditText"]'
    svip_button = By.XPATH,'//*[@text="立即成为会员"]'

    '''避免踩坑：变量和函数名不能一致，不然识别不出来，会报错'''

    def input_invitecode(self):
        self.base_input(self.invitecode,'lihao')

    def click_svip_button(self):
        self.base_click(self.svip_button)

    #组合业务方法
    def join_svip(self):
        self.input_invitecode()
        self.click_svip_button()