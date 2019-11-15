import logging
from time import sleep
from common.desired_caps import mind_desired
from common.functions import Common


class Message(Common):

    def message(self):
        """点击底部按钮"""
        message_path = '//android.widget.TextView[@text="消息"]'
        self.find_path(message_path).click()

    def add_friends(self):
        # """添加好友"""
        # sleep(1)
        # self.message()
        # sleep(2)
        # # 添加好友path路径(ImageView)
        # image_view_path = '//android.widget.ImageView'
        # # 点击加号按钮
        # add_jia = self.find_paths(image_view_path)
        # add_jia[1].click()
        # # 添加号码按钮路径
        # add_friends_path = '//android.widget.TextView[@text="添加好友"]'
        # # 点击添加好友按钮
        # self.find_path(add_friends_path).click()
        # sleep(0.5)
        # self.go_back()
        logging.info('添加好友')
        pass

    def group_chat(self):
        # self.message()
        # """发起群聊"""
        # # 添加好友path路径(ImageView)
        # image_view_path = '//android.widget.ImageView'
        # # 点击加号按钮
        # add_jia = self.find_paths(image_view_path)
        # add_jia[1].click()
        # # 发起群聊路劲
        # group_chat_path = '//android.widget.TextView[@text="发起群聊"]'
        #
        # # 点击发起群聊按钮
        # self.find_path(group_chat_path).click()
        # self.wait_time(0.5)
        # # 点击返回按钮
        # # self.click_tap(34, 70)
        # self.go_back()
        logging.info('发起群聊')


if __name__ == '__main__':
    driver2 = mind_desired()
    msg = Message(driver2)
    msg.add_friends()
    msg.group_chat()



