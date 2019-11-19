from common.myunit import *
from  businessView.addmindmap.right_layout import AddMind


# @unittest.skip
class TestAddMind(StartEnd):
    # @unittest.skip("跳过新建模块的自动化测试")
    def test_right(self):
        am = AddMind(self.driver)
        # am.mind_map()
        am.framework()
        am.flow_chart()



if __name__ == '__main__':
    unittest.main()
