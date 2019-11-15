# -*- coding:utf-8 -*-
from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from common.desired_caps import mind_desired
from common.functions import Common
import logging
import os
import random


class Mind(Common):

    # 当前模块名称
    module = str(os.path.abspath(__file__).split('\\')[-1][:-3])

    def guide(self):
        sleep(2)
        self.swipe_left()
        self.wait_time(5)
        self.swipe_left()
        self.click_tap(255,255)

    def test_lg(self, tel, code, msg):
        """
        :return:
        """
        login_edit = r"//android.widget.EditText"
        login_button = r"//android.widget.TextView[@text='立即登录']"
        # 设置等待时间
        self.wait_time(10)
        # 输入手机号码
        a = self.driver.find_elements_by_xpath(login_edit)
        a[0].clear()
        a[0].send_keys(tel)
        # 输入验证码
        a[1].clear()
        a[1].send_keys(code)
        # 点击“立即登录”按钮
        self.driver.find_element_by_xpath(login_button).click()
        self.driver.implicitly_wait(5)
        try:
            # 获取Toast提示
            message = '//*[@text=\'{}\']'.format(msg)
            WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(message))
            # logging.info(toast_element.text)
            return True
        except TimeoutException:
            self.get_screen_shot(self.module)
            return False
        # logging.info('登录成功，登录账号：%s，登陆验证码：%s' % (tel, code))

    def servers(self):
        self.swipe_up()
        self.find_path('//android.widget.TextView[@text="我已阅读并同意 《服务协议》确认登录"]').click()
        self.wait_time(0.5)
        self.swipe_up()
        self.go_back()

    # def wechat(self):
    #     # 绑定微信
    #     binding_wechat = r'//android.widget.TextView[@text="绑定微信"]'
    #     self.driver.find_element_by_xpath(binding_wechat).click()
    #
    # def qq(self):
    #     # 绑定QQ
    #     binding_qq = r'//android.widget.TextView[@text="绑定QQ"]'
    #     self.driver.find_element_by_xpath(binding_qq).click()
    #
    # def general_setup(self):
    #     # 通用设置
    #     general_set = r'//android.widget.TextView[@text="通用设置"]'
    #     self.driver.find_element_by_xpath(general_set).click()
    #
    # def about(self):
    #     # 关于我们
    #     about_us = r'//android.widget.TextView[@text="关于我们"]'
    #     self.driver.find_element_by_xpath(about_us).click()

    def login_out(self):
        # 退出登录
        login_out = r'//android.widget.TextView[@text="退出登录"]'
        self.driver.find_element_by_xpath(login_out).click()
        # 获取当前截图
        self.get_screen_shot(self.module)
        msg = '提交成功'
        message = '//*[@text=\'{}\']'.format(msg)
        toast_element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(message))
        logging.info(toast_element.text)


if __name__ == '__main__':
    driver1 = mind_desired()
    md = Mind(driver1)
    md.test_lg('', '', msg='111')
    md.login_out()

