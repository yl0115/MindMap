# -*- coding:utf-8 -*-
from common.myunit import *
from businessView.my_view import MyView
import logging
from businessView.personal_information.personal_info import PersonalInformation
from businessView.seting_about.general_settings import GeneralSetting
import string, random


# @unittest.skip
class MyTest(StartEnd):
    csv_file = '../data/login/login_input.csv'
    # csv_file = r'F:\testCode\MindUIAutoTest\data\login\login_input.csv'

    password = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    password = password.lower()

    def test_11transition(self):
        pi = PersonalInformation(self.driver)
        try:
            self.assertTrue(pi.transition())
            self.assertTrue(pi.head_portrait())
            self.assertTrue(pi.head_portrait2())

        except AssertionError:
            logging.info('测试失败！')

    def test_12nickname(self):
        pi = PersonalInformation(self.driver)
        try:
            # self.assertTrue(pi.nickname('名字'))
            pi.nicknamefor('昵称', r'/personal_data/nickname.xlsx')
        except AssertionError:
            logging.info('测试失败')
    def test_13mind_code(self):
        pi = PersonalInformation(self.driver)
        try:
            self.assertTrue(pi.mind_codefor('脑图号', r'/personal_data/mind_code.xlsx'))
        except AssertionError:
            logging.info('测试失败')

    def test_14label(self):
        pi = PersonalInformation(self.driver)
        try:
            self.assertTrue(pi.lablefor('个性标签', r'/personal_data/personality_label.xlsx'))
        except AssertionError:
            logging.info('测试失败')

    def test_15start(self):
        mv = MyView(self.driver)
        mv.start()

    def test_2general_setting(self):
        gs = GeneralSetting(self.driver)
        gs.transition()
        gs.about_us()

    def test_5update_tel(self):
        """修改登录手机号码"""
        logging.info('修改登录手机')
        mv = MyView(self.driver)
        # 循环编辑，行数从2开始读取
        for i in range(10, len(self.csv_file)):
            # 调用读取csv方法并传入行数
            data = mv.get_csv_data(self.csv_file, i)
            # 判断当data数组为空时跳出该循环
            if data is None:
                break
            # 调用逻辑方法，并传入csv相应参数
            a = mv.update_tel(data[2], data[7], data[3])
            try:
                # 断言返回结果是否为True
                self.assertTrue(a)
            except AssertionError:
                logging.info('测试失败！')
        logging.info('修改登录手机自动化测试结束')

    def test_3update_pwd(self):
        logging.info('修改登录密码1')
        mv = MyView(self.driver)
        # 循环编辑，行数从2开始读取
        for i in range(10, len(self.csv_file)):
            # 调用读取csv方法并传入行数
            data = mv.get_csv_data(self.csv_file, i)
            # 判断当data数组为空时跳出该循环
            if data is None:
                break
            # 调用逻辑方法，并传入csv相应参数
            a = mv.update_pwd(self.password, data[3])
            try:
                # 断言返回结果是否为True
                self.assertTrue(a)
            except AssertionError:
                logging.info('测试失败！')

    def test_4update_pwd(self):
        logging.info('修改登录密码2')
        mv = MyView(self.driver)
        tag = mv.update_pwd2(self.password, 'yl10200115')
        try:
            self.assertTrue(tag)
        except AssertionError:
            logging.info('测试失败')
        logging.info('修改登录密码自动化测试结束')
        logging.info('密码为：%s' % self.password)


if __name__ == '__main__':
    unittest.main()
