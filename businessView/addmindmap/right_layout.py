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
    # 随机文件夹
    file_name = str(random.randint(0, 500))
    # 新建中我的文件定位
    my_file = r'//android.widget.TextView[@text="我的文件"]'

    def right_mind(self):

        # 右布局路径
        right_mind_path = r'//android.widget.TextView[@text="思维脑图"]'
        self.find_path(self.add_mind).click()
        self.find_path(right_mind_path).click()
        sleep(1)
        self.go_back()
        sleep(1)
        self.find_path('//android.widget.TextView[@text="保存"]').click()
        self.find_path('//android.widget.EditText[@text="中心主题"]').send_keys(self.file_name)
        ele = self.find_paths('//android.widget.TextView')
        ele[-1].click()
        self.find_path('//android.widget.TextView[@text="我的文件"]').click()
        self.find_path('//android.widget.TextView[@text="确认"]').click()
        self.find_path('//android.widget.TextView[@text="保存"]').click()
        self.wait_time(1)

        try:
            self.wait_time(0.5)
            q = self.find_paths('//android.widget.TextView')
            q[0].click()
            self.wait_time(0.5)
        except StaleElementReferenceException as e:
            self.wait_time(0.5)
            close_path = self.find_paths('//android.widget.TextView')
            close_path[0].click()
            self.wait_time(0.5)
        self.find_path('//android.widget.TextView[@text="不保存"]').click()
        # 判断文件是否存在
        self.find_path('//android.widget.TextView[@text="文件"]').click()
        self.find_path('//android.widget.TextView[@text="我的文件"]').click()
        try:
            if self.find_path('//android.widget.TextView[@text="中心主题%s.m"]' % self.file_name):
                self.go_back()
                pass
        except NoSuchElementException:
            self.get_screen_shot(self.module)

    def mind_file_delete(self):
        """
        删除脑图文件
        :return:
        """

        # 删除按钮
        delete_button = r'//android.widget.TextView[@text="删除"]'
        # 确认按钮
        ack_button = r'android:id/button1'
        self.find_path(self.my_file).click()
        # 获取文件的名字元素
        mind_file_name = '//android.widget.TextView[@text="中心主题%s.m"]' % self.file_name
        mind_path = self.find_path(mind_file_name)
        self.slide(mind_path)
        self.find_path(delete_button).click()
        self.wait_time(1)
        self.find_path(delete_button).click()
        # self.find_id(ack_button).click()
        tag = self.toast('删除成功', self.module)
        if tag:
            self.go_back()
            return True
        else:
            self.get_screen_shot(self.module)
            return False

    def mind_file_remove(self):
        # 移动按钮
        remove_button = r'//android.widget.TextView[@text="移动"]'
        # 获取文件的名字元素
        mind_file_name = '//android.widget.TextView[@text="中心主题%s.m"]' % self.file_name
        # 点击我的文件
        self.find_path(self.my_file).click()
        mind_path = self.find_path(mind_file_name)
        self.slide(mind_path)
        self.find_path(remove_button).click()
        self.go_back()

        pass



    def slide(self, ele):
        """左滑显示按钮功能"""
        # 获取当前元素坐标
        coord = ele.location
        x1 = int(coord['x']) // 100
        y1 = int(coord['y'])
        TouchAction(self.driver).long_press(ele, duration=1).move_to(x=x1, y=y1).release().perform()





if __name__ == '__main__':
    driver = mind_desired()
    am = AddMind(driver)
    sleep(6)
    am.right_mind()
