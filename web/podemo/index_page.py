from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver
from selenium import webdriver

from web.podemo.login_page import LoginPage
from web.podemo.register_page import RegisterPage


# 首页的PO
class IndexPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.maximize_window()

    def goto_login(self):
        """
        进入登录页面
        :return:
        """
        # click login button
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        # return LoginPage
        return LoginPage(self.driver)

    def goto_register(self):
        """
        进入到注册页面
        :return:
        """
        # click register button
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        # return RegisterPage
        return RegisterPage(self.driver)
