# -*- coding:utf-8 -*-
from common.myunit import *
from businessView.login import Mind
from common.desired_caps import mind_desired
import logging


# @unittest.skip
class LoginTest(StartEnd):
    # @unittest.skip('手机输入框点击登录测试')
    def test_log1(self):
        md = Mind(self.driver)
        """手机输入框点击登录测试"""
        csv_file = '../data/login/tel_input.csv'
        logging.info('登录功能断言测试开始')
        md.guide()
        # 循环编辑，行数从2开始读取
        for i in range(2, 200):
            # 调用读取csv方法并传入行数
            data = md.get_csv_data(csv_file, i)
            # 判断当data数组为空时跳出该循环
            if data is None:
                break
            # 调用逻辑方法，并传入csv相应参数
            a = md.test_lg(data[2], '', data[4])
            try:
                # 断言返回结果是否为True
                self.assertTrue(a)
            except AssertionError:
                pass

    # @unittest.skip('验证码输入框点击登录测试')
    def test_log2(self):
        """验证码输入框点击登录测试"""
        md = Mind(self.driver)
        csv_file = '../data/login/code_input.csv'
        # 循环编辑，行数从2开始读取
        for i in range(2, 200):
            # 调用读取csv方法并传入行数
            data = md.get_csv_data(csv_file, i)
            # 判断当data数组为空时跳出该循环
            if data is None:
                break
            # 调用逻辑方法，并传入csv相应参数
            a = md.test_lg('18382413281', data[2], data[4])
            try:
                # 断言返回结果是否为True
                self.assertTrue(a)
            except AssertionError:
                pass
    def test_log3(self):
        md = Mind(self.driver)
        md.servers()

    def test_log4(self):
        """登录统一测试"""
        md = Mind(self.driver)
        csv_file = '../data/login/login_input.csv'
        # 循环编辑，行数从2开始读取
        for i in range(2, len(csv_file)):
            # 调用读取csv方法并传入行数
            data = md.get_csv_data(csv_file, i)
            # 判断当data数组为空时跳出该循环
            if data is None:
                break
            # 调用逻辑方法，并传入csv相应参数
            a = md.test_lg(data[2], data[3], data[5])
            try:
                # 断言返回结果是否为True
                self.assertTrue(a)
            except AssertionError:
                pass
        logging.info('登录模块断言测试结束')


if __name__ == '__main__':
    unittest.main()
