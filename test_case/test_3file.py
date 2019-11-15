# -*- coding:utf-8 -*-
import random

from common.myunit import *
from businessView.file_view import FileView
import logging
import unittest


class MyTest(StartEnd):
    def test_file1(self):
        fv = FileView(self.driver)
        logging.info('文件模块自动化测试开始')
        num = str(random.randint(1000, 9999))
        fv.add_file1(num+'第一个')
        fv.add_file2(num+'第二个')
        fv.add_file3(num+'第三个')
        for i in range(3):
            fv.delete_ele2()
        fv.delete_ele1()
        fv.move_ele(num+'移动文件')
        fv.rename_ele(str(random.randint(1, 9))+'重命名')
        fv.rename_ele2('重命名', r'/file_testcase/login.xlsx')
        fv.rename_ele3('重命名', r'/file_testcase/login.xlsx')
        fv.sort_ele()
        fv.multi_select(str(random.randint(100, 999)))


if __name__ == '__main__':
    unittest.main()
