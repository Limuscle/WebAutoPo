from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver
from selenium import webdriver
from web.qjlBackend.index_page import IndexPage


# 登录PO
class LoginPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://backend-test.qianjinlian.com/")
        self.driver.maximize_window()

    def goto_index(self):
        """
        登录进入首页
        :return:
        """
        # 输入手机号
        self.driver.find_element(By.CSS_SELECTOR, "#app > div > form > div:nth-child(2) > div > div > input").send_keys("15118845720")
        # 输入密码
        self.driver.find_element(By.CSS_SELECTOR, "#app > div > form > div:nth-child(3) > div > div > input").send_keys("LLLLyyyy_1111")
        # 立即登录
        self.driver.find_element(By.CSS_SELECTOR, "#app > div > form > div:nth-child(6) > div > button:nth-child(2)").click()
        # 输入验证码666666
        self.driver.find_element(By.CSS_SELECTOR, "#app > div > form > div:nth-child(4) > div > "
                                                  "div.el-input.el-input--small.el-input--prefix > input").send_keys("666666")
        # 登录
        self.driver.find_element(By.CSS_SELECTOR, "#app > div > form > div:nth-child(6) > div > button:nth-child(1)").click()
        # sleep(10)
        # return到首页
        return IndexPage(self.driver)

    def goto_resetPassword(self):
        """
        重置密码，重置密码后跳到登录页
        :return:
        """
        # 点击忘记密码
        self.driver.find_element(By.CSS_SELECTOR, ".el-link--inner").click()
        # 输入手机号
        self.driver.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div/div[2]/form/div[1]/div/div/input").send_keys("15118845720")
        # 点击发送验证码 -- 跳过
        # 获取弹出窗口，输入验证码 -- 跳过
        # 点击确定 -- 跳过
        # 输入短信验证码666666
        self.driver.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div/div[2]/form/div[2]/div/div[1]/input").send_keys("666666")
        # 点击下一步
        self.driver.find_element(By.CSS_SELECTOR, ".el-icon-arrow-right").click()
        # 输入新密码
        self.driver.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div/div[2]/form/div[1]/div/div/input").send_keys("LLLLyyyy_1111")
        # 重复输入
        self.driver.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div/div[2]/form/div[2]/div/div/input").send_keys("LLLLyyyy_1111")
        # 点击确认
        self.driver.find_element(By.CSS_SELECTOR, ".el-icon-arrow-right").click()
        # 点击登录
        self.driver.find_element(By.CSS_SELECTOR, ".el-icon-arrow-right").click()
        # return到登录
        return LoginPage()

