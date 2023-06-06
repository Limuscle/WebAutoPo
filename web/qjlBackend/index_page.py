from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class IndexPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def indexData(self):
        # 计算存证数量是否正确
        a = self.driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/section/div[1]/div/div[1]/div[1]/div/div[2]/span").text
        b = self.driver.find_elements(By.CSS_SELECTOR, ".app-container")
