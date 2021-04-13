import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    #查找元素
    def base_find_element(self, feature, timeout=30, poll=0.1):
        by = feature[0]
        value = feature[1]
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    #查找一组元素
    def base_find_elements(self, feature, timeout=30, poll=0.1):
        by = feature[0]
        value = feature[1]
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    #点击元素
    def base_click(self, feature):
        self.base_find_element(feature).click()

    #输入元素
    def base_input(self, feature, text):
        input = self.base_find_element(feature)
        input.clear()
        input.send_keys(text)

    #获取单个文本信息
    def base_get_text(self, feature):
        return self.base_find_element(feature).text

    #判断元素是否存在(通用方法)
    def base_if_element_exist(self,element):
        message_xpath = By.XPATH, '//*[contains(@text,"{}")]'.format(element)
        try:
            self.base_find_element(message_xpath,5,0.1)
            return True
        #这里一定得是TimeoutException，而不是TimeoutError
        #TimeoutException超时会继续执行里面代码，TimeoutError就会报错，不管里面的代码
        except TimeoutException:
            return False

    # 判断元素是否存在(个别方法)
    def base_if_elem_exist(self,element):
        try:
            self.base_find_element(element,5,0.1)
            return True
        except TimeoutException:
            return False

    # 判断toast是否存在
    def base_is_toast_exist(self,message):
        message_xpath = By.XPATH, '//*[contains(@text,"{}")]'.format(message)
        try:
            self.base_find_element(message_xpath,5,0.1)
            return True
        except TimeoutException:
            return False

    #获取toast文本信息
    def base_get_toast_text(self,message):
        message_xpath = By.XPATH, '//*[contains(@text,"{}")]'.format(message)
        if self.base_is_toast_exist(message):
            return self.base_find_element(message_xpath,5,0.1).text
        else:
            # return False
            raise Exception('toast不存在')

    #滑动找元素
    def base_scroll_find_element(self,feature,direction='up'):
        """ 边滑边找某个元素的特征
            :param feature:元素的特征"""
        page_source = ''
        while True:
            try:
                return self.base_find_element(feature)
                break
            except Exception:
                self.base_scroll_page_one(direction)
                if self.driver.page_source == page_source:
                    print('滑到底了')
                    break
                page_source = self.driver.page_source

    def base_scroll_page_one(self,direction='up'):
        """ 边滑边找某个元素的特征
            :param feature:元素的特征
            :param direction:方向
            "up"：从下往上
            "down"：从上往下
            "left"：从右往左
            "down"：从左往右
            :return: """
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']

        center_x = width/2
        center_y = height/2

        left_x = width/4*1
        left_y = center_y
        right_x = width/4*3
        right_y = center_y

        up_x = center_x
        up_y = height/4*1
        bottom_x = center_x
        bottom_y = height/4*3

        if direction=='up':
            self.driver.swipe(bottom_x,bottom_y,up_x,up_y)
        if direction=='down':
            self.driver.swipe(up_x,up_y,bottom_x,bottom_y)
        if direction=='left':
            self.driver.swipe(right_x,right_y,left_x,left_y)
        if direction=='right':
            self.driver.swipe(left_x,left_y,right_x,right_y)
        else:
            raise Exception('请确认参数是否正确：up/down/left/right')

    def base_if_in_page_source(self,keyword,tomeout=10,poll=0.1):
        '''针对webview里的的toast'''
        #结束时间
        end_time = time.time()+tomeout
        while True:
            if end_time<time.time():
                return False
            if keyword in self.driver.page_source:
                return True
            time.sleep(poll)

    #返回键方法
    def base_return_key(self):
        self.driver.press_keycode(4)








