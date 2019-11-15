import unittest
from BSTestRunner import BSTestRunner
import time
import logging
import sys


path = r'F:\testCode\MindUIAutoTest'
sys.path.append(path)

test_dir = '../test_case'
report_dir = '../reports'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir+'/'+now+'test_report.html'
with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title='脑图App自动化测试报告', description='mindMap Android app 测试报告')
    logging.info('start run test case....')
    runner.run(discover)



