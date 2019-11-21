
import logging
import os

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from common.desired_caps import mind_desired
from common.functions import Common
import random


class Home_Page(Common):

    def left_delete(self):
        self.find_path(self.class_path('首页', 't')).click()
        text = self.find_path(self.class_path('开始.t', 't'))
        logging.info(text)
        self.slide(text)

    def slide(self, ele):
        """左滑显示按钮功能"""
        # 获取当前元素坐标
        coord = ele.location
        x1 = coord['x'] // 100
        x2 = coord['x']+800
        y1 = coord['y']
        self.swipe(x2,y1,x1,y1,100)
        # TouchAction(self.driver).long_press(ele,duration=None).move_to(x=x1, y=y1).release().perform()

if __name__ == '__main__':
    driver = mind_desired()
    hp = Home_Page(driver)
    hp.a()