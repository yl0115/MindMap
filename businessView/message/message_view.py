import logging
import os
from common.desired_caps import mind_desired
from common.functions import Common


class Message(Common):

    # 当前模块名称
    module = str(os.path.abspath(__file__).split('\\')[-1][:-3])

    def add_friends(self):
        """
        添加好友
        :return: 
        """
        # 点击底部按钮
        self.find_path(self.abs_path('消息', 't')).click()
        self.forced_wait()
        # 添加好友path路径(ImageView)
        image_view_path = '//android.widget.ImageView'
        # 点击加号按钮
        add_jia = self.find_paths(image_view_path)
        add_jia[1].click()
        self.find_path(self.abs_path('添加好友', 't')).click()
        self.find_path(self.abs_path('脑图号', 'e')).send_keys('99999999')
        self.driver.keyevent(66)
        self.forced_wait()
        self.find_paths('//android.widget.ImageView')[1].click()
        self.find_path(self.abs_path('请输入验证消息', 'e')).send_keys('nihao')
        self.find_path(self.abs_path('发送', 't')).click()
        self.toast('请求发送成功', self.module)
        self.go_back()
        self.forced_wait()
        add_jia[0].click()
        self.go_back()
        self.go_back()


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



