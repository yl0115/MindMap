# from time import sleep
#
# from appium import webdriver
#
#
# class Demo(object):
#     driver = None
#
#     def hospital(self):
#         desires_caps = {
#             'platformName': 'Android',
#             'deviceName': 'FIG-TL00',
#             'platformVersion': '5.1.1',
#             'udid': 'KDV4C17C26001518',
#             'app': r'F:\testCode\MindUIAutoTest\App\wenxin.apk',
#             'appPackage': 'com.tencent.mm',
#             'appActivity': 'com.tencent.mm.ui.LauncherUI',
#             'noReset': True,
#             'unicodeKeyboard': True,
#             'resetKeyboard': True,
#             'automationName': 'uiautomator2'
#         }
#         self.driver = webdriver.Remote('http://' + '127.0.0.1' + ":" + '4723' + '/wd/hub', desires_caps)
#         self.driver.implicitly_wait(5)
#         sleep(6)
#         self.driver.tap([(601, 317)], 0)
#         sleep(2)
#         self.driver.tap([(320, 1942)], 0)
#         sleep(1)
#         self.driver.tap([(281, 1360)], 0)
#         sleep(1)
#
#         self.driver.tap([(694, 628)], 0)
#         sleep(3)
#
#         self.driver.tap([(694, 628)], 0)
#         self.swipe_up()
#         for i in range(1000):
#             self.driver.tap([(626, 1251)], 0)
#
#     def get_size(self):
#         x = self.driver.get_window_size()['width']
#         y = self.driver.get_window_size()['height']
#         return x, y
#
#     def swipe_up(self):
#         """向上滑动"""
#         size = self.get_size()
#         x1 = int(size[0] * 0.2)
#         y1 = int(size[0] * 0.9)
#         y2 = int(size[1] * 0.1)
#         self.driver.swipe(x1, y1, x1, y2, 1000)
#
#
# if __name__ == '__main__':
#     d = Demo()
#     d.hospital()
import random

# print([i for i in range(10) if i != 4][random.randint(0, 8)])
# print([i for i in range(
#
# 10) if i != 5][random.randint(0, 9)])
# print([i for i in range(10) if i % 2 == 0][random.randint(0, 2)])
# print([i for i in range(10) if i % 2 == 0][random.randint(0, 6)])
# print([i for i in range(10) if i % 2 == 0][random.randint(0, 9)])
# while True:
#     input('点击生成随机数...')
#     print(['杨雷', '杨雷1', '杨雷2', '杨雷3'][random.randint(0, 3)])

# num1 = [1,2,3,4,5,'ee']
# num2 = [1,2,3,4,5,'22']
# for i in range(len(num1)):
#     print(num1[i], num2[i])

# def a():
#     return '脑图号只能修改一次'
#
#
# v = a()
# if v == '脑图号只能修改一次':
#     print('True')
# else:
#     print('False')
# num = [1, 3, '脑图号', 4]
#
# for i in num:
#
#     if i == '脑图号':
#         break
#     print(i)


# def textview(classname):
#     return '\'//android.widget.TextView[@text="%s"]\'' % classname
#
# print(textview('d'))
# def class_path(content, tag):
#     if tag == 't':
#         return '\'//android.widget.TextView[@text="%s"]\'' % content
#     if tag == 'e':
#         return '\'//android.widget.EditText[@text="%s"]\'' % content
# a = class_path('请输入你的宝贵意见和建议', 'e')
# print(type(a))
# print(a)

# def a():
#     return 'dd', '44'
#
# b = a()
# print(b[1])
# print(type(b[1]))
import yaml

def qq():
    with open(r'../config/desired_caps.yaml', 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    if data['noReset']:
        print(data['noReset'])
    else:
        print(11)

qq()