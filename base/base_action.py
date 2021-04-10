from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, feature, timeout=30, poll=0.5):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    def base_find_elements(self, feature, timeout=10, poll=1):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    def base_click(self, feature):
        self.base_find_element(feature).click()

    def base_input(self, feature, text):
        self.base_find_element(feature).send_keys(text)

    def base_get_text(self, feature):
        return self.base_find_element(feature).text
