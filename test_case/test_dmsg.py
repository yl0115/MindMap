from common.myunit import *
from businessView.message.message_view import Message
import logging
from common.mysql_cline import SQLConnect


class MsgTest(StartEnd):

    def test_1add_friends(self):
        logging.info('消息自动化测试Start')
        msg = Message(self.driver)
        msg.add_friends()

    def test_2group_chat(self):
        msg = Message(self.driver)
        msg.group_chat()
        logging.info('消息自动化测试End')


if __name__ == '__main__':
    unittest.main()
