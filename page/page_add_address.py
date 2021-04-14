import random
from time import sleep

import allure
from selenium.webdriver.common.by import By

from AolaiShop_project.base.base_action import BaseAction


class PageAddAddress(BaseAction):
    #收件人姓名
    receipt_name = By.ID,'com.yunmall.lc:id/address_receipt_name'
    #电话
    receipt_phone = By.ID,'com.yunmall.lc:id/address_add_phone'
    #所在地区
    region = By.ID,'com.yunmall.lc:id/address_province'
    #省市区
    province_city_area = By.ID,'com.yunmall.lc:id/area_title'
    #详细地址
    detail_address = By.ID,'com.yunmall.lc:id/address_detail_addr_info'
    #邮编
    post_code = By.ID,'com.yunmall.lc:id/address_post_code'
    #默认地址按钮
    default_address_button = By.ID,'com.yunmall.lc:id/address_default'
    #保存按钮
    save_button = By.ID,'com.yunmall.lc:id/button_send'

    @allure.step(title='输入收件人')
    def input_receipt_name(self,receiver):
        self.base_input(self.receipt_name,receiver)

    @allure.step(title='输入收件人电话')
    def input_receipt_phone(self,phone):
        self.base_input(self.receipt_phone, phone)

    @allure.step(title='点击地区')
    def click_region(self):
        self.base_click(self.region)

    @allure.step(title='选择省市区')
    def select_region(self):
        self.click_region()
        sleep(1)
        while True:
            if self.driver.current_activity != 'com.yunmall.ymctoc.ui.activity.ProvinceActivity':
                return
            #所有可选的省市区
            areas = self.base_find_elements(self.province_city_area)
            #所有可选的个数
            area_count = len(areas)
            #随机数下标
            area_index = random.randint(0,area_count-1)
            #获取随机的省市区
            areas[area_index].click()
            sleep(1)
    @allure.step(title='输入详细地址')
    def input_detail_address(self,address):
        self.base_input(self.detail_address,address)

    @allure.step(title='输入邮编')
    def input_post_code(self,postcode):
        self.base_input(self.post_code, postcode)

    @allure.step(title='点击设为默认地址')
    def click_default_address(self):
        self.base_click(self.default_address_button)

    @allure.step(title='点击保存')
    def click_save(self):
        self.base_click(self.save_button)

    @allure.step(title='检查是否有toast提示')
    def if_toast_exist(self,toast):
        return self.base_is_toast_exist(toast)

    #组合业务方法
    def add_address(self,receiver,phone,address,postcode):
        self.input_receipt_name(receiver)
        self.input_receipt_phone(phone)
        self.select_region()
        self.input_detail_address(address)
        self.input_post_code(postcode)
        self.click_default_address()
        self.click_save()



