from common.myunit import *
from  businessView.addmindmap.right_layout import AddMind
import logging



class TestAddMind(StartEnd):
    def test_right(self):
        logging.info('新建自动化测试开始')
        am = AddMind(self.driver)
        # am.mind_map()
        am.framework()
        # am.flow_chart()
        logging.info('新建自动化测试结束')



if __name__ == '__main__':
    unittest.main()
