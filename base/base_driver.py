from appium import webdriver


def init_driver(no_reset=True):
    info = {
        # 设备信息
        'platformName':'Android',
        'platformVersion':'5.1.1',
        'deviceName':'127.0.0.1:62001',
        # app信息
        'appPackage':'com.yunmall.lc',
        'appActivity':'com.yunmall.ymctoc.ui.activity.MainActivity',
        'automationName' : 'Uiautomator2',
        'noReset':no_reset,
        # 默认输入中文无效，但不会报错，需要在 ”前置代码（启动参数）“ 中增加以下两个参数
        'unicodeKeyboard':True,
        'resetKeyboard':True
    }

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)
