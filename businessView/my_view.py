# -*- coding:utf-8 -*-
from selenium.common.exceptions import NoSuchElementException

from common.desired_caps import mind_desired
from common.functions import Common
import os
import logging
# import random
from common.mysql_cline import SQLConnect


class MyView(Common):
    # 当前模块名称
    module = str(os.path.abspath(__file__).split('\\')[-1][:-3])
    # 四大按钮，我的xpath路劲
    my = r"//android.widget.TextView[@text='我的']"
    # 点击我的设置
    setup = r'//android.widget.TextView[@text="我的设置"]'
    # 修改手机号码
    update_login_tel = r'//android.widget.TextView[@text="修改登录手机"]'
    # 原手机号码
    old_tel_path = r'//android.widget.EditText'
    # 新手机号码
    new_tel_path = r'//android.widget.EditText[@text="请输入新手机号码"]'
    # 请输入短信验证码
    sms_code = r'//android.widget.EditText[@text="请输入短信验证码"]'
    # 点击确认修改按钮
    confirm_update = r'//android.widget.TextView[@text="确认修改"]'
    # 修改登录密码
    update_login_pwd = r'//android.widget.TextView[@text="修改登录密码"]'
    # 选择框地址
    circle_path = '//android.widget.TextView[@text="已阅读并同意"]'
    # 保存按钮路径
    save_path = '//android.widget.TextView[@text="保存"]'
    # 获取文本输入框集合
    pwd_path = '//android.widget.EditText'

    def start(self):
        """我的模块"""
        # 点击“我的”按钮
        self.find_path(self.my).click()
        # 点击我的设置
        self.find_path(self.setup).click()

    def update_tel(self, old_tel, new_tel, code):
        # 修改手机号码
        self.find_path(self.update_login_tel).click()
        # 原手机号码
        self.driver.find_elements_by_xpath(self.old_tel_path)[0].send_keys(old_tel)
        # 新手机号码
        self.find_path(self.new_tel_path).send_keys(new_tel)
        # 请输入短信验证码
        self.find_path(self.sms_code).send_keys(code)
        # 点击确认修改按钮
        self.find_path(self.confirm_update).click()
        # 判断是否是我的设置界面
        my_set = '//android.widget.TextView[@text="我的设置"]'
        if self.find_path(my_set):
            # 修改成功后退出操作
            self.logout()
            # 退出程序后清除数据库
            self.data_cleaning()
            return True
        else:
            self.get_screen_shot(self.module)
            return False

    def update_pwd(self, pwd, code):
        try:
            self.find_path(self.update_login_pwd).click()
            input_list = self.find_paths(self.pwd_path)
            input_list[0].send_keys(pwd)
            input_list[1].send_keys(pwd)
            input_list[3].send_keys(code)
            # # 勾选服务协议
            # self.find_path(self.circle_path).click()
            # 点击保存按钮
            self.find_path(self.save_path).click()
            tag = self.toast('保存成功', self.module)
            return tag
        except NoSuchElementException as e:
            logging.info(e)
            self.get_screen_shot(self.module)
            return False

    def update_pwd2(self, pw, new_pwd):
        try:
            self.find_path(self.update_login_pwd).click()
            input_list = self.find_paths(self.pwd_path)
            # 输入旧密码
            input_list[0].send_keys(pw)
            input_list[1].send_keys(new_pwd)
            input_list[2].send_keys(new_pwd)
            # 确认修改按钮路径
            confirm = '//android.widget.TextView[@text="确认修改"]'
            # 点击确认修改按钮
            self.find_path(confirm).click()
            tag = self.toast('修改成功', self.module)
            if tag:
                return True
            else:
                self.get_screen_shot(self.module)
                return False
        except NoSuchElementException as e:
            self.go_back()
            logging.info(e)
            self.get_screen_shot(self.module)
            return False

    @staticmethod
    def data_cleaning():
        """数据库数据清理"""
        sl = SQLConnect()
        sl.update_tel()
        tel = sl.select_tel()
        logging.info('修改数据库信息: %s' % tel)

    def logout(self):
        try:
            self.wait_time(5)
            self.find_path('//android.widget.TextView[@text="退出登录"]').click()
            self.find_path('//android.widget.TextView[@text="确认"]').click()
            # 判断是否返回登录界面
            # 获取登录界面登录按钮元素
            login_button = r"//android.widget.TextView[@text='立即登录']"
            if self.find_path(login_button):
                return True
            else:
                self.get_screen_shot(self.module)
                return False
        except NoSuchElementException as e:
            self.get_screen_shot(self.module)
            logging.info(e)


if __name__ == '__main__':
    driver1 = mind_desired()
    mv = MyView(driver1)
    # mv.update_tel('18382413281', '17318961563', '334005')
    mv.data_cleaning()
    # mv.update_pwd()

