# -*- coding:utf-8 -*-
import time
import os
import csv
import logging

from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait

from baseView.base_View import BaseView
import pandas as pd


class Common(BaseView):
    def wait_time(self, num):
        self.driver.implicitly_wait(num)

    @staticmethod
    def forced_wait(num=1):
        time.sleep(num)

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipe_up(self):
        """
        向上滑
        :return:
        """
        size = self.get_size()
        x1 = int(size[0] * 0.2)
        y1 = int(size[0] * 0.9)
        y2 = int(size[1] * 0.1)
        self.driver.swipe(x1, y1, x1, y2, 1000)

    def swipe_down(self):
        """
        向下滑动
        :return:
        """
        size = self.get_size()
        x1 = int(size[0] * 0.5)
        y1 = int(size[0] * 0.1)
        y2 = int(size[0] * 0.9)
        self.driver.swipe(x1, y1, x1, y2)

    def swipe_right(self):
        """
        向右滑动
        :return:
        """
        size = self.get_size()
        x1 = int(size[0] * 0.2)
        x2 = int(size[0] * 0.9)
        y1 = int(size[0] * 0.5)
        self.driver.swipe(x1, y1, x2, y1)

    def swipe_left(self):
        """
        向左滑
        :return:
        """
        size = self.get_size()
        x1 = int(size[0] * 0.9)
        y1 = int(size[1] * 0.5)
        x2 = int(size[0] * 0.2)
        self.driver.swipe(x1, y1, x2, y1, 1000)

    @staticmethod
    def get_time():
        """获取当前时间"""
        now = time.strftime("%Y-%m-%d %H_%M_%S ")
        return now

    def get_screen_shot(self, module):
        """截图并存放到指定位置"""
        new_time = self.get_time()
        image_file = os.path.dirname(
            os.path.dirname(__file__))+'\\screenshots\\%s_%s.png' % (module, new_time)
        self.driver.get_screenshot_as_file(image_file)
        logging.info('截图已保存')

    @staticmethod
    def get_csv_data(csv_file, line):
        """data读取数据"""

        with open(csv_file, 'r', encoding='utf-8')as f:
            reader = csv.reader(f)
            for index, row in enumerate(reader, 1):
                if index == line:
                    f.close()
                    return row

    @staticmethod
    def get_excel(sheet, name_path):
        """
        输入
        :param sheet: 
        :param name_path: 
        :return: 
        """
        # 获取当前文件目录的上级目录
        filename = os.path.dirname(os.path.dirname(__file__))
        filename = os.path.join(filename + '/data%s' % name_path)
        data = pd.read_excel(filename, sheet_name="%s" % sheet, header=0)
        # 输入的数组集合
        input_num = []
        # 输出的数组集合
        output_str = []
        # 获取excel的总行数和总列数
        row_col = data.shape
        for i in range(row_col[0]):
            input_num.append(data.loc[i]['输入'])
            output_str.append(data.loc[i]['期望结果'])

        return input_num, output_str

    @staticmethod
    def get_excel_result(sheet, name_path):
        # 获取当前文件目录的上级目录
        filename = os.path.dirname(os.path.dirname(__file__))
        filename = os.path.join(filename + '/data%s' % name_path)
        data = pd.read_excel(filename, sheet_name="%s" % sheet, header=0)
        input_num = []
        # 获取excel的总行数和总列数
        row_col = data.shape
        for i in range(row_col[0]):
            input_num.append(data.loc[i]['期望结果'])

        return input_num

    def click_tap(self, num1, num2):
        self.driver.tap([(num1, num2)], 0)

    def dblclick(self, num1, num2):
        self.driver.tap([(num1, num2)], 0)
        self.driver.tap([(num1, num2)], 0)

    def toast(self, msg, module):
        try:
            # 获取Toast提示
            message = '//*[@text=\'{}\']'.format(msg)
            WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(message))
            return True
        except TimeoutException:
            self.get_screen_shot(module)
            toast_element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(message))
            logging.info('提示有误——：'+ toast_element.text)
            return False

    def go_back(self):
        self.wait_time(5)
        """返回按钮位置点击"""
        try:
            # 定位到第一个文件夹图标元素
            folder_path = '//android.widget.TextView'
            folder_path = self.find_paths(folder_path)
            folder_path[0].click()
        except StaleElementReferenceException:
            # 定位到第一个文件夹图标元素
            folder_path = '//android.widget.TextView'
            folder_path = self.find_paths(folder_path)[0].click()

    @staticmethod
    def HUAWEI_operation(self):
        pass

    @staticmethod
    def abs_path(content, tag):
        """
        固定文字
        :param content: 
        :param tag: 
        :return: 
        """
        if tag == 't':
            return '//android.widget.TextView[@text="%s"]' % content
        if tag == 'e':
            return '//android.widget.EditText[@text="%s"]' % content

    @staticmethod
    def class_path(content, tag):
        """
        固定文字
        :param content: 
        :param tag: 
        :return: 
        """
        if tag == 't':
            return '//android.widget.TextView[contains(@text,"%s")]' % content
        if tag == 'e':
            return '//android.widget.EditText[contains(@text,"%s")]' % content

    def slide(self, ele):
        """左滑显示按钮功能"""
        # 获取当前元素坐标
        coord = ele.location
        # x1 = coord['x'] // 100
        # y1 = coord['y']
        # TouchAction(self.driver).long_press(ele,duration=None).move_to(x=x1, y=y1).release().perform()
        x1 = coord['x']
        x2 = coord['x']+800
        y1 = coord['y']+50
        self.swipe(x2,y1,x1,y1,500)

    def slide1(self, ele):
        """左滑显示按钮功能"""
        # 获取当前元素坐标
        coord = ele.location
        # x1 = coord['x'] // 100
        # y1 = coord['y']
        # TouchAction(self.driver).long_press(ele,duration=None).move_to(x=x1, y=y1).release().perform()
        x1 = coord['x']//4
        x2 = coord['x']
        y1 = coord['y']
        self.swipe(x2,y1,x1,y1,500)

    def is_not_exist(self, ele):
        """
        判断元素是否存在
        :param ele: 
        :return: 
        """
        WebDriverWait(self.driver, 1).until(lambda x: x.find_element_by_xpath('//android.widget.TextView[@text="%s"]' % ele))

    def get_permission(self):
        self.find_id('com.android.packageinstaller:id/permission_allow_button').click()

