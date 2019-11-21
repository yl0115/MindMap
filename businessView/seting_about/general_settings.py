from common.functions import Common
import os


class GeneralSetting(Common):
    # 当前模块名称
    module = str(os.path.abspath(__file__).split('\\')[-1][:-3])
    # 通用设置的xpath路径
    general_setting_path = '//android.widget.TextView[@text="通用设置"]'
    # 按钮关闭中的路径
    switch_off_path = '//android.widget.Switch[@text="关闭"]'
    # 按钮关闭中的路径
    switch_on_path = '//android.widget.Switch[@text="开启"]'

    # 关于我们的xpath路径
    about_us_path = '//android.widget.TextView[@text="关于我们"]'
    # 反馈投诉的xpath路径
    feedback_path = '//android.widget.TextView[@text="反馈投诉"]'
    # 版本介绍的xpath路径
    version_path = '//android.widget.TextView[@text="版本介绍"]'
    # 服务协议的xpath路径
    service_path = '//android.widget.TextView[@text="《服务协议》"]'
    # 隐私协议的xpath路径
    vip_path = '//android.widget.TextView[@text="《隐私协议》"]'

    def transition(self):
        # 点击通用设置
        self.find_path(self.general_setting_path).click()
        # 打开所有开关
        result = self.find_paths(self.switch_off_path)
        for i in range(len(result)):
            result[i].click()
        # 点击返回按钮
        self.go_back()
        # 再次点击通用设置
        self.find_path(self.general_setting_path).click()
        result = self.find_paths(self.switch_on_path)
        for i in range(len(result)):
            result[i].click()
        # 再次点击返回
        self.go_back()

    def about_us(self):
        # 点击关于我们
        self.find_path(self.about_us_path).click()
        self.find_path(self.feedback_path).click()
        # radio单选框图标地址
        imagelist = self.find_paths(r'//android.widget.ImageView')
        for i in range(4):
            imagelist[i].click()
        self.find_path(self.abs_path('请输入你的宝贵意见和建议', 'e')).send_keys('请输入你的宝贵意见和建议12212')
        self.find_path(self.abs_path('常用联系方式(选填)', 'e')).send_keys('常用联系方式(选填)1233')
        self.find_path(self.abs_path('提交', 't')).click()
        self.toast('发送完成', self.module)
        self.forced_wait(2)
        self.go_back()
        self.find_path(self.version_path).click()
        self.go_back()
        self.find_path(self.service_path).click()
        self.swipe_up()
        self.go_back()
        self.find_path(self.vip_path).click()
        self.swipe_up()
        self.go_back()
        self.forced_wait()
        # 点击返回按钮
        self.go_back()
