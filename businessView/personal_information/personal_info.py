from time import sleep
import os
import yaml
from selenium.common.exceptions import NoSuchElementException

from common.functions import Common
from common.desired_caps import mind_desired
import logging


class PersonalInformation(Common):
    # 当前模块名称
    module = str(os.path.abspath(__file__).split('\\')[-1][:-3])
    # 通用完成按钮
    accomplish_path = '//android.widget.TextView[@text="完成"]'
    # 个人信息界面判定条件
    information_path = '//android.widget.TextView[@text="个人信息"]'
    tag = True

    def transition(self):
        """
        1、点击我的界面上进入个人信息界面
        :return:
        """
        my_path = '//android.widget.TextView[@text="我的"]'
        self.find_path(my_path).click()
        # 点击进入个人信息的view
        # pf = '//android.view.View[@index="4"]'
        pf = '//android.widget.TextView[@index="4"]'
        self.find_path(pf).click()
        try:
            self.find_path(self.information_path)
            return True
        except NoSuchElementException:
            self.get_screen_shot(self.module)
            return False

    def head_portrait(self):
        """
        拍照更换头像
        此处针对华为nova3写的自动化程序
        :return:表示操作正常，False表示更换头像失败并截图保存
        """
        # 头像路径
        portrait_path = '//android.widget.TextView[@text="头像"]'
        # 拍照选择框，拍照
        choose_photos1 = '//android.widget.TextView[@text="拍照"]'
        # 点击头像
        self.find_path(portrait_path).click()
        # 点击拍照按钮
        self.find_path(choose_photos1).click()
        with open(r'../config/desired_caps.yaml', 'r', encoding='utf-8') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        if data['noReset']:
            pass
        else:
                self.get_permission()
        self.forced_wait()
        # 点击返回按钮
        self.driver.keyevent(4)
        try:
            # 判断是否返回到个人信息界面
            self.find_path(self.information_path)
            return True
        except NoSuchElementException:
            self.get_screen_shot(self.module)
            return False

    def head_portrait2(self):
        """
        从相册选择照片进行更换头像
        :return: True
        """
        # 头像路径
        portrait_path = '//android.widget.TextView[@text="头像"]'
        choose_photos2 = '//android.widget.TextView[@text="从相册选择"]'
        self.find_path(portrait_path).click()
        self.find_path(choose_photos2).click()
        self.driver.keyevent(4)
        try:
            self.find_path(self.information_path)
            return True
        except NoSuchElementException:
            self.get_screen_shot(self.module)
            self.go_back()
            return False

    def nickname(self, nick_name, toast_out):
        """
        修改昵称
        :return:
        """
        # 昵称路径
        nickname_path = '//android.widget.TextView[@text="昵称"]'
        # 输入昵称框
        nickname_send_path = '//android.widget.EditText'
        # 点击昵称
        self.find_path(nickname_path).click()
        # 输入昵称
        self.find_path(nickname_send_path).send_keys(nick_name)
        # 点击完成按钮
        self.find_path(self.accomplish_path).click()
        if self.toast(toast_out, self.module):
            return True
        else:
            logging.info('我走的else')
            self.get_screen_shot(self.module)
            self.go_back()
            return False

    def nicknamefor(self, sheet, name_path):
        d_list, output_list = self.get_excel(sheet, name_path)
        for i in range(len(d_list)):
            self.nickname(d_list[i], output_list[i])
        pass

    def mind_code(self, m_code, toast_out):
        """
        修改脑图号
        :return:
        """
        # 脑图号输入框路径
        mind_code_input_path = '//android.widget.EditText'

        # 点击脑图号
        self.find_path(self.abs_path('脑图号', 't')).click()
        # 输入脑图号
        self.find_path(mind_code_input_path).clear()
        self.find_path(mind_code_input_path).send_keys(m_code)
        # 点击完成按钮
        self.find_path(self.accomplish_path).click()
        if self.toast(toast_out, self.module):
            self.go_back()
            return True
        else:
            self.go_back()
            return False

    def mind_codefor(self, sheet, code_path):
        d_list, output_list = self.get_excel(sheet, code_path)
        for i in range(len(d_list)):
            context = self.mind_code(d_list[i], output_list[i])
            if not context:
                break

    def label(self, labels, toast_out):
        """
        修改个性标签
        :return:
        """
        # 个性标签路径
        label_path = '//android.widget.TextView[@text="个性标签"]'
        # 个性标签输入框路径
        label_input_path = '//android.widget.EditText'

        # 点击个性标签
        self.find_path(label_path).click()
        # 输入个性标签
        self.find_path(label_input_path).send_keys(labels)
        # 点击完成按钮
        self.find_path(self.accomplish_path).click()
        if self.toast(toast_out, self.module):
            return True
        else:
            self.get_screen_shot(self.module)
            return False

    def lablefor(self, sheet, lable_path):
        # 个性标签路径
        label_path = '//android.widget.TextView[@text="个性标签"]'
        # 点击个性标签
        self.find_path(label_path).click()
        # 点击完成按钮
        self.find_path(self.accomplish_path).click()
        # 获取excel文字
        d_list, output_list = self.get_excel(sheet, lable_path)
        for i in range(len(d_list)):
            self.tag = self.label(d_list[i], output_list[i])
        self.go_back()
        return self.tag


if __name__ == '__main__':
    driver = mind_desired()
    pi = PersonalInformation(driver)
    pi.transition()
