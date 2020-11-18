from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


desired_caps = {
    "platformName": "Android",
    "platfromVersion": "9",
    "deviceName": "ec54d6d5",
    "appPackage": "com.tencent.mm",
    "appActivity": ".ui.LauncherUI"
}
driver_server = 'http://127.0.0.1:4723/wd/hub'

# driver = webdriver.Remote(driver_server, desired_caps)


class Moments():
    """
    docstring
    """

    def __init__(self):
        self.desired_caps = desired_caps
        self.driver = webdriver.Remote(driver_server, self.desired_caps)
        self.wait = WebDriverWait(self.driver, 300)

    def login(self):
        print('点击登录按钮----')
        login = self.wait.until(EC.presence_of_element_located(
            (By.ID, 'com.tencent.mm:id/fam')))
        login.click()
        # 输入手机号码
        phone = self.wait.until(EC.presence_of_element_located(
            (By.ID, 'com.tencent.mm:id/bhn')))
        phone_num = input('请输入手机号')
        phone.send_keys(phone_num)
        print('点击下一步中')
        button = self.wait.until(EC.presence_of_element_located(
            (By.ID, 'com.tencent.mm:id/e3i')))
        button.click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().test("用微信号/QQ号/邮箱登录")').click()

        # pass_w = input('请输入密码：')
        # password = self.wait.until(
        #     EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/hz')))
        # password.send_keys(pass_w)
        # login = self.wait.until(EC.element_to_be_clickable(
        #     (By.ID, 'com.tencent.mm:id/alr')))
        # login.click()

        # # 提示 叉掉
        # tip = self.wait.until(EC.element_to_be_clickable(
        #     (By.ID, 'com.tencent.mm:id/an2')))
        # tip.click()

    def main(self):
        self.login()


M = Moments()
M.main()
