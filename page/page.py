from AolaiShop_project.page.page_about_aolai import PageAboutAolai
from AolaiShop_project.page.page_add_address import PageAddAddress
from AolaiShop_project.page.page_address_list import PageAddressList
from AolaiShop_project.page.page_goods import PageGoods
from AolaiShop_project.page.page_me import PageMe
from AolaiShop_project.page.page_home import PageHome
from AolaiShop_project.page.page_login import PageLogin
from AolaiShop_project.page.page_me_unlogin import PageMeUnlogin
from AolaiShop_project.page.page_search import PageSearch
from AolaiShop_project.page.page_setting import PageSetting
from AolaiShop_project.page.page_category import PageCategory
from AolaiShop_project.page.page_shop_cart import PageShopCart
from AolaiShop_project.page.page_specific_good import PageSpecificGood
from AolaiShop_project.page.page_svip import PageSvip


class PageEntrance():

    def __init__(self,driver):
        self.driver = driver
    #首页入口
    @property
    def page_home(self):
        return PageHome(self.driver)
    #我的页面-未登录前的状态
    @property
    def page_me_unlogin(self):
        return PageMeUnlogin(self.driver)
    #登录页面入口
    @property
    def page_login(self):
        return PageLogin(self.driver)
    #我的页面入口
    @property
    def page_me(self):
        return PageMe(self.driver)
    #设置页面入口
    @property
    def page_setting(self):
        return PageSetting(self.driver)
    #关于百年奥莱页面入口
    @property
    def page_about_aolai(self):
        return PageAboutAolai(self.driver)
    #超级vip页面入口
    @property
    def page_svip(self):
        return PageSvip(self.driver)
    #地址管理页面入口
    @property
    def page_address_list(self):
        return PageAddressList(self.driver)
    #新增地址页面入口
    @property
    def page_add_address(self):
        return PageAddAddress(self.driver)
    #分类页面入口
    @property
    def page_category(self):
        return PageCategory(self.driver)
    # 选择商品页面入口
    @property
    def page_goods(self):
        return PageGoods(self.driver)
    #具体商品详情页面入口
    @property
    def page_specific_good(self):
        return PageSpecificGood(self.driver)
    #购物车页面页面入口
    @property
    def page_shop_cart(self):
        return PageShopCart(self.driver)
    #搜索页面页面入口
    @property
    def page_search(self):
        return PageSearch(self.driver)