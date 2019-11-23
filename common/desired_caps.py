# -*- coding:utf-8 -*-
from appium import webdriver
import yaml
import logging
import logging.config
import os


CON_LOG = r'../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def mind_desired():
    with open(r'../config/desired_caps.yaml', 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    # 获取当前文件的上级目录
    base_dir = os.path.dirname(os.path.dirname(__file__))
    # app存放位置拼接
    app_path = os.path.join(base_dir, 'App', data['app'])
    desires_caps = {
        'platformName': data['platformName'],
        'deviceName': data['deviceName'],
        'platformVersion': data['platformVersion'],
        # 'udid': data['udid'],
        'app': app_path,
        'appPackage': data['appPackage'],
        'appActivity': data['appActivity'],
        'noReset': data['noReset'],
        'unicodeKeyboard': data['unicodeKeyboard'],
        # 设置超时等待时间
        # 'newCommandTimeout': "200000",
        'resetKeyboard': data['resetKeyboard'],
        'automationName': data['automationName']
    }
    logging.info('start app')
    driver = webdriver.Remote('http://'+str(data['ip'])+":"+str(data['port'])+'/wd/hub', desires_caps)
    driver.implicitly_wait(5)
    f.close()
    return driver


if __name__ == '__main__':
    mind_desired()



