from common.myunit import *
from  businessView.home_page.home import Home_Page
import logging
import yaml


class TestAddMind(StartEnd):

    def test_right(self):
        hp = Home_Page(self.driver)
        with open(r'../config/desired_caps.yaml', 'r', encoding='utf-8') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        if data['noReset']:
            logging.info('首页自动化测试开始')
            hp.left_delete()
            logging.info('首页自动化测试结束')
        else:
            for i in range(2):
                hp.get_permission()
                sleep(1)
                logging.info('新安装App没有记录，首页测试结束')



if __name__ == '__main__':
    unittest.main()
