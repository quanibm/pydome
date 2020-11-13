class Slide():
    """
    滑动
    """

    def __init__(self, driver):
        self.driver = driver

    def get_screen_size(self):
        """
        获取屏幕size
        """
        # 获取屏幕宽度
        x = self.driver.get_window_size()['width']
        # 获取屏幕高度
        y = self.driver.get_window_size()['height']
        return (x, y)

    def swipe_left(self):
        lsize = self.get_screen_size()
        x1 = int(lsize[0]*.95)
        x2 = int(lsize[0]*.15)
        y1 = int(lsize[1]*.5)
        self.driver.swipe(x1, y1, x2, y1)
        print('向左滑动')

    def swipe_right(self):
        lsize = self.get_screen_size()
        x1 = int(lsize[0]*.15)
        x2 = int(lsize[0]*.95)
        y1 = int(lsize[1]*.5)
        self.driver.swipe(x1, y1, x2, y1)
        print('向右滑动')

    def swipe_up(self):
        lsize = self.get_screen_size()
        x1 = int(lsize[0]*.5)
        y1 = int(lsize[0]*.95)
        y2 = int(lsize[1]*.15)
        self.driver.swipe(x1, y1, x1, y2)
        print('向上滑动')

    def swipe_down(self):
        lsize = self.get_screen_size()
        x1 = int(lsize[0]*.5)
        y1 = int(lsize[0]*.15)
        y2 = int(lsize[1]*.95)
        self.driver.swipe(x1, y1, x1, y2)
        print('向下滑动')
