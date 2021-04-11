from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    #查找元素
    def base_find_element(self, feature, timeout=120, poll=1):
        by = feature[0]
        value = feature[1]
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    #查找一组元素
    def base_find_elements(self, feature, timeout=100, poll=1):
        by = feature[0]
        value = feature[1]
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    #点击元素
    def base_click(self, feature):
        self.base_find_element(feature).click()

    #输入元素
    def base_input(self, feature, text):
        self.base_find_element(feature).send_keys(text)

    #获取文本信息
    def base_get_text(self, feature):
        return self.base_find_element(feature).text

    # 判断toast是否存在
    def base_is_toast_exist(self,message):
        message_xpath = By.XPATH, "//*[contains(@text,'{}')]".format(message)
        try:
            self.base_find_element(message_xpath)
            return True
        except TimeoutError as e:
            return False

    #获取toast文本信息
    def base_get_toast_text(self,message):
        message_xpath = By.XPATH, "//*[contains(@text,'{}')]".format(message)
        if self.base_is_toast_exist(message):
            return self.base_find_element(message_xpath).text
        else:
            # return False
            raise Exception('toast不存在')

    #滑动找元素
    def scroll_find_element(self,feature,direction):
        """ 边滑边找某个元素的特征
            :param feature:元素的特征"""
        page_source = ''
        while True:
            try:
                return self.base_find_element(feature)
                break
            except Exception:
                self.scroll_page_one(direction)
                if self.driver.page_source == page_source:
                    print('滑到底了')
                    break
                page_source = self.driver.page_source

    def scroll_page_one(self,direction='up'):
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






