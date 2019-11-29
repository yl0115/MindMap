from time import sleep
import logging
import os
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException

from common.desired_caps import mind_desired
from common.functions import Common
import random


class AddMind(Common):
    # 当前模块名称
    module = str(os.path.abspath(__file__).split('\\')[-1][:-3])
    # 底部新建按钮路径
    add_mind = r'//android.widget.Button[@index="2"]'
    # 随机生成的数字
    num = random.randint(1, 999)

    def function_kyes(self):
        self.forced_wait(1)
        function_key = self.find_paths('//android.widget.TextView')
        function_key[1].click()
        self.find_path(self.abs_path('保存图片', 't')).click()
        self.toast('图片已经保存到相册', self.module)
        function_key[1].click()
        self.find_path(self.abs_path('发送文件', 't')).click()
        self.go_back()
        self.forced_wait(1)
        function_key[1].click()
        self.find_path(self.abs_path('发送图片', 't')).click()
        self.go_back()
        self.forced_wait(1)
        function_key[1].click()
        self.find_path(self.abs_path('取消', 't')).click()
        function_key[0].click()

    def mind_map(self):
        """
        思维导图自动化
        :return: 
        """
        # 点击底部新建+按钮
        self.find_path(self.add_mind).click()
        logging.info('思维导图自动化测试开始！')
        self.find_path(self.abs_path('思维导图', 't')).click()
        # 调用右上角功能
        self.function_kyes()
        logging.info('思维导图测试结束')

    def framework(self):
        """
        组织架构图自动化
        :return: 
        """
        # 点击底部新建+按钮
        self.find_path(self.add_mind).click()
        logging.info('组织架构图自动化测试开始')
        self.find_path(self.abs_path('组织架构图', 't')).click()
        self.forced_wait()
        # 对图形进行操作
        # self.click_tap(518,661)
        self.click_tap(518,661)
        self.find_path(self.abs_path('组织部门', 'e')).send_keys(self.num)
        # 调用右上角功能
        self.function_kyes()
        # 点击保存按钮
        self.find_path(self.abs_path('保存', 't')).click()
        # 再次点击保存
        self.find_path(self.abs_path('保存', 't')).click()

        # ============分支===========
        logging.info('测试组织架构图发送功能')

        self.find_path(self.abs_path('文档', 't')).click()
        self.find_path(self.abs_path('组织架构图', 't')).click()
        self.slide(self.find_path(self.class_path(self.num, 't')))
        self.find_path(self.abs_path('发送', 't')).click()
        self.forced_wait()
        self.find_paths('//android.widget.ImageView')[0].click()
        self.find_path(self.abs_path('发送', 't')).click()
        self.toast('发送成功', self.module)

        self.slide(self.find_path(self.class_path(self.num, 't')))
        self.find_path(self.abs_path('发送', 't')).click()
        self.find_path(self.abs_path('发送', 't')).click()
        self.forced_wait()
        self.find_paths('//android.widget.ImageView')[0].click()
        self.find_path(self.abs_path('发送', 't')).click()
        try:
            self.toast('发送成功', self.module)
            self.slide(self.find_path(self.class_path(self.num, 't')))
            self.find_path(self.abs_path('删除', 't')).click()
            self.find_path(self.abs_path('删除', 't')).click()
            self.toast('删除成功', self.module)
            self.go_back()
            self.find_path(self.abs_path('文档', 't')).click()
            self.find_path(self.abs_path('回收站', 't')).click()
            self.slide(self.find_path(self.class_path(self.num, 't')))
            self.find_path(self.abs_path('还原', 't')).click()
            self.find_path(self.abs_path('确认还原', 't')).click()
            self.toast('还原成功', self.module)
            self.go_back()
        except TimeoutException:
            self.go_back()
            self.slide(self.find_path(self.class_path(self.num, 't')))
            self.find_path(self.abs_path('删除', 't')).click()
            self.find_path(self.abs_path('删除', 't')).click()
            self.toast('删除成功', self.module)
            self.go_back()
            self.find_path(self.abs_path('文档', 't')).click()
            self.find_path(self.abs_path('回收站', 't')).click()
            self.slide(self.find_path(self.class_path(self.num, 't')))
            self.find_path(self.abs_path('还原', 't')).click()
            self.find_path(self.abs_path('确认还原', 't')).click()
            self.toast('还原成功', self.module)
            self.go_back()

    def framework_second(self):
        logging.info('测试组织架构图选路劲功能')
        # 点击底部新建+按钮
        self.find_path(self.add_mind).click()
        self.find_path(self.abs_path('组织架构图', 't')).click()
        self.forced_wait()
        # 对图形进行操作
        # self.click_tap(518,661)
        self.click_tap(518,661)
        self.find_path(self.abs_path('组织部门', 'e')).send_keys(self.num)
        # 调用右上角功能
        self.function_kyes()
        # 点击保存按钮
        self.find_path(self.abs_path('保存', 't')).click()
        # 点击选择路径
        self.find_path(self.class_path('路径：文件', 't')).click()
        # 点击组织架构图
        self.find_path(self.abs_path('组织架构图', 't')).click()
        # 点击确定
        self.find_path(self.abs_path('确认', 't')).click()
        self.find_path(self.abs_path('保存', 't')).click()
        # 修改后放开
        # self.toast('当前目录已存在该文件', self.module)
        # text = '组织部门' + str(self.num)
        # self.find_path(self.abs_path(text, 'e')).send_keys(self.num)
        # self.find_path(self.abs_path('保存', 't')).click()

    def framework_function(self):
        logging.info('测试组织架构图的底部功能栏')
        # 点击底部新建+按钮
        self.find_path(self.add_mind).click()
        self.find_path(self.abs_path('组织架构图', 't')).click()
        self.forced_wait()
        # 对图形进行操作
        self.click_tap(518, 661)
        self.forced_wait()
        textview = self.find_paths('//android.widget.TextView')
        textview[3].click()
        textview[4].click()
        textview[5].click()
        textview[6].click()
        textview[2].click()
        textview[2].click()
        textview[2].click()
        textview[7].click()
        self.forced_wait()
        function_key = self.find_paths('//android.widget.TextView')
        function_key[0].click()
        self.find_path(self.abs_path('保存', 't')).click()
        self.find_path(self.abs_path('取消', 't')).click()
        self.forced_wait()
        function_key[0].click()
        self.find_path(self.abs_path('不保存', 't')).click()






    def flow_chart(self):
        """
        流程图自动化
        :return: 
        """
        logging.info('流程图自动化测试开始')
        self.find_path(self.abs_path('流程图', 't')).click()
        self.forced_wait()
        # 对图形进行操作
        self.forced_wait()
        self.click_tap(537, 994)
        self.forced_wait()
        self.click_tap(537, 994)
        self.find_path(self.abs_path('开始', 'e')).send_keys(random.randint(1, 999))
        # 调用右上角功能
        self.function_kyes()
        # 点击保存按钮
        self.find_path(self.abs_path('保存', 't')).click()
        # 再次点击保存
        self.find_path(self.abs_path('取消', 't')).click()
        self.forced_wait()
        function_key = self.find_paths('//android.widget.TextView')
        function_key[0].click()
        self.find_path(self.abs_path('不保存', 't')).click()
        logging.info('流程图自动化测试结束')













if __name__ == '__main__':
    driver = mind_desired()
    am = AddMind(driver)
    sleep(6)
    am.mind_map()
