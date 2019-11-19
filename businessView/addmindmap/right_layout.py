from time import sleep
import logging
import os

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from common.desired_caps import mind_desired
from common.functions import Common
import random


class AddMind(Common):
    # 当前模块名称
    module = str(os.path.abspath(__file__).split('\\')[-1][:-3])
    # 底部新建按钮路径
    add_mind = r'//android.widget.Button[@index="2"]'

    def function_kyes(self, num):
        self.forced_wait(1)
        function_key = self.find_paths('//android.widget.TextView')
        function_key[num].click()

    def mind_map(self):
        """
        思维导图自动化
        :return: 
        """
        # 点击底部新建+按钮
        self.find_path(self.add_mind).click()
        logging.info('思维导图自动化测试开始！')
        self.find_path(self.class_path('思维导图', 't')).click()
        self.function_kyes(1)
        self.find_path(self.class_path('保存图片', 't')).click()
        self.toast('图片已经保存到相册', self.module)
        self.function_kyes(1)
        self.find_path(self.class_path('发送文件', 't')).click()
        self.go_back()
        self.function_kyes(1)
        self.find_path(self.class_path('发送图片', 't')).click()
        self.go_back()
        self.function_kyes(1)
        self.find_path(self.class_path('取消', 't')).click()
        self.function_kyes(0)
        logging.info('思维导图测试结束')

    def framework(self):
        """
        组织架构图自动化
        :return: 
        """
        logging.info('组织架构图自动化测试开始')
        # 点击底部新建+按钮
        self.find_path(self.add_mind).click()
        self.find_path(self.class_path('组织架构图', 't')).click()
        self.function_kyes(1)
        self.find_path(self.class_path('保存图片', 't')).click()
        self.toast('图片已经保存到相册', self.module)
        self.function_kyes(1)
        self.find_path(self.class_path('发送文件', 't')).click()
        self.go_back()
        self.function_kyes(1)
        self.find_path(self.class_path('发送图片', 't')).click()
        self.go_back()
        self.function_kyes(1)
        self.find_path(self.class_path('取消', 't')).click()
        self.function_kyes(0)
        logging.info('组织架构图自动化测试结束')

    def flow_chart(self):
        """
        流程图自动化
        :return: 
        """
        logging.info('流程图自动化测试开始')
        self.find_path(self.class_path('流程图', 't')).click()
        self.forced_wait(1)
        self.function_kyes(1)
        self.find_path(self.class_path('保存图片', 't')).click()
        self.toast('图片已经保存到相册', self.module)
        self.function_kyes(1)
        self.find_path(self.class_path('发送文件', 't')).click()
        self.go_back()
        self.function_kyes(1)
        self.find_path(self.class_path('发送图片', 't')).click()
        self.go_back()
        self.function_kyes(1)
        self.find_path(self.class_path('取消', 't')).click()
        self.function_kyes(0)
        logging.info('流程图自动化测试结束')













if __name__ == '__main__':
    driver = mind_desired()
    am = AddMind(driver)
    sleep(6)
    am.mind_map()
