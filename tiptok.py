from appium import webdriver
from utils.slide import Slide
from time import sleep


desired_caps = {
    # adb logcat>~/Desktop/log.log
    # Displayed
    "platformName": "Android",
    "platfromVersion": "6.0.1",
    "deviceName": "emulator-5554",
    "appPackage": "com.ss.android.ugc.aweme",
    "appActivity": ".splash.SplashActivity",
    "autoAcceptAlerts": 'true'
}
driver_server = 'http://127.0.0.1:4723/wd/hub'


class Action(Slide):

    def __init__(self):
        self.desired_caps = desired_caps
        self.driver = webdriver.Remote(driver_server, self.desired_caps)
        self.driver.implicitly_wait(15)
        Slide.__init__(self, self.driver)

    def pass_windows(self):
        """
        同意协议
        """
        self.driver.find_element_by_id(
            'com.ss.android.ugc.aweme:id/a_b').click()
        # 点击不更新（这一步最新版客户端可省略，我是为了向大家演示出现的情况，故意没有更新最新版的）
        # self.driver.find_element_by_id(
        #     'com.ss.android.ugc.aweme:id/bxs').click()
        # print('手机弹窗的权限接受')
        # self.driver.switch_to.alert.accept()
        sleep(5)
        self.driver.find_element_by_id(
            'com.android.packageinstaller:id/permission_allow_button').click()
        sleep(5)
        self.driver.find_element_by_id(
            'com.android.packageinstaller:id/permission_allow_button').click()
        print('完成权限验证')
        sleep(10)
        # 根据系统指示上滑一次
        print('根据系统指示上滑一次')
        self.swipe_up()
        sleep(10)
        for i in range(800):
            print('持续上滑')
            self.swipe_up()
            sleep(4)

    def close_app(self):
        """
        关闭app
        """
        self.driver.close_app()

    def run(self):
        self.pass_windows()
        self.close_app()


if __name__ == "__main__":
    action = Action()
    action.run()
    # while True:
    #     try:
    #         action = Action()
    #         action.run()
    #     except:
    #         continue

    # def comments(self):
    #     sleep(2)
    #     self.driver.tap([(500, 1200)], 500)

    # def scroll(self):
    #     """
    #     无限滚动
    #     """
    #     while True:
    #         self.driver.swipe(self.start_x, self.start_y,
    #                           self.start_y-self.distance)

    #         # 设置延时等待

    #         sleep(10)

    # def main(self):
    #     """
    #     初始化函数
    #     """
    #     self.comments()
    #     self.scroll()


# if __name__ == '__main__':
#     action = Action()
#     action.main()
