
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from web.podemo.register_page import RegisterPage


# 登录PO
class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def scan(self):
        # 微信扫码登录
        pass

    def goto_register(self):
        """
        点击注册
        :return:
        """
        # 点击注册
        # sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return RegisterPage(self.driver)
