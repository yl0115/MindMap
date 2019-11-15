from common.myunit import *
from  businessView.addmindmap.right_layout import AddMind


# @unittest.skip
class TestAddMind(StartEnd):
    @unittest.skip("跳过新建模块的自动化测试")
    def test_right(self):
        am = AddMind(self.driver)
        am.right_mind()
        am.mind_file_remove()
        am.mind_file_delete()


if __name__ == '__main__':
    unittest.main()
