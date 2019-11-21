from common.myunit import *
from  businessView.home_page.home import Home_Page
import logging


class TestAddMind(StartEnd):
    def test_right(self):
        logging.info('首页自动化测试开始')
        hp = Home_Page(self.driver)
        hp.left_delete()
        logging.info('首页自动化测试结束')


if __name__ == '__main__':
    unittest.main()
