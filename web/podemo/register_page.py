from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from time import time


# 注册PO
class RegisterPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        """
        注册用户
        :return:
        """
        self.driver.find_element(By.ID, "corp_name").send_keys("企业名称")
        # self.driver.find_element(By.ID, "corp_name").send_keys(corpname)
        self.driver.find_element(By.CSS_SELECTOR, "#manager_name").send_keys("管理员一")
        self.driver.find_element(By.ID, "register_tel").send_keys("13012345678")
        self.driver.find_element(By.ID, "iagree").click()
        self.driver.find_element(By.ID, "submit_btn").click()
        return True
