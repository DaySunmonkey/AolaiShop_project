from AolaiShop_project.page.page_me import PageMe
from AolaiShop_project.page.page_home import PageHome
from AolaiShop_project.page.page_login import PageLogin
from AolaiShop_project.page.page_me_unlogin import PageMeUnlogin


class PageEntrance():

    def __init__(self,driver):
        self.driver = driver

    @property
    def page_home(self):
        return PageHome(self.driver)

    @property
    def page_me_unlogin(self):
        return PageMeUnlogin(self.driver)

    @property
    def page_login(self):
        return PageLogin(self.driver)

    @property
    def page_me(self):
        return PageMe(self.driver)

