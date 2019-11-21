import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, \
    InvalidArgumentException
from common.functions import Common
import logging
import random
import unittest
import os
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait


class FileView(Common):
    new_add = ''
    # 重命名按钮的路径
    rename_path = '//android.widget.TextView[@text="重命名"]'
    # 最后的新建
    new_add_folder = ''
    # 当前模块名称
    module = str(os.path.abspath(__file__).split('\\')[-1][:-3])
    # 生成文件夹名称随机数
    # filename = str(random.randint(1000, 9999))
    # 底部文件按钮路径
    file_path = '//android.widget.TextView[@text="文件"]'
    # 点击新建文件夹按钮
    add_folder_button = '//android.widget.TextView[@text="新建文件夹"]'
    # 输入内容文本框
    send_content = '//android.widget.EditText[@index=1]'
    # 新建文件夹toast弹窗的确认
    add_folder_affirm = '//android.widget.TextView[@text="确认"]'
    # 新建文件夹toast弹窗的取消
    add_folder_cancel = '//android.widget.TextView[@text="取消"]'
    # 移动按钮路径
    move_path = '//android.widget.TextView[@text="移动"]'
    # 重命名按钮路径
    rechristen_path = '//android.widget.TextView[@text="重命名"]'
    # 删除按钮路径
    delete_path = '//android.widget.TextView[@text="删除"]'

    def add_file1(self, filename, tab=1, num=None):
        """
        正常添加一个文件夹流程
        :param num:
        :param tab:
        :param filename: 传入文件夹的名称
        :return:判断新建文件夹元素对象是否存在，存在返回True,反之False
        """
        if tab == 1:
            # 点击底部文件按钮
            self.find_path(self.file_path).click()
        else:
            pass
        if num == 1:
            pass
        else:
            # 调用新建步骤
            self.add_step()
        # 输入新建文件夹名称
        self.find_path(self.send_content).clear()
        self.find_path(self.send_content).send_keys(filename)
        # 点击确认
        self.find_path(self.add_folder_affirm).click()
        # 打印文件夹名称
        # logging.info('文件夹名称为：%s' % filename)
        # 新增文件夹的路径
        self.new_add = '//android.widget.TextView[@text="%s"]' % filename
        try:
            # 获取元素对象,判断是否存在
            self.find_path(self.new_add)
            return True
        except NoSuchElementException:
            return False

    def add_file2(self, filename):
        """
        输入特殊字符值断言
        :param filename: 传入文件夹的名称
        :return: 判断新建文件夹元素对象是否存在，存在返回True,反之False
        """
        # 调用新建步骤
        self.add_step()
        # 输入新建文件夹名称
        self.find_path(self.send_content).clear()
        self.find_path(self.send_content).send_keys(filename)
        # 点击取消按钮
        self.find_path(self.add_folder_cancel).click()
        # 再次点击新建步骤
        self.add_step()
        # 点击确定
        self.find_path(self.add_folder_affirm).click()
        # 新增文件夹的路径
        new_folder = '//android.widget.TextView[@text="%s"]' % filename
        try:
            self.find_path(new_folder)
            return True
        except NoSuchElementException:
            return False

    def add_file3(self, filename):
        time.sleep(0.5)
        # 调用新建步骤
        self.add_file1(filename, tab=2)
        # 新增文件夹的路径
        new_folder = '//android.widget.TextView[@text="%s"]' % filename
        self.find_path(new_folder).click()
        for i in range(3):
            time.sleep(0.5)
            # 点击右上角三横按钮
            new_path = '//android.widget.TextView'
            new_path = self.find_paths(new_path)
            new_path[2].click()
            time.sleep(0.5)
            # 点击新建文件夹按钮
            self.find_path(self.add_folder_button).click()
            # 点击新增的文件夹
            # random_name = str(random.randint(1000, 9999))
            self.add_file1(i, tab=2, num=1)
            new_folder = '//android.widget.TextView[@text="%s"]' % i
            try:
                self.find_path(new_folder).click()
            except NoSuchElementException:
                self.swipe_up()
                self.find_path(new_folder).click()
        for i in range(4):
            if i == 3:
                self.go_back()
                break
            else:
                self.go_back()
                time.sleep(1)
                folder = '//android.widget.TextView'
                folder = self.find_paths(folder)
                self.slide(folder[3])
                # 确认删除按钮路径
                delete_path = '//android.widget.TextView[@text="删除"]'
                self.find_path(delete_path).click()
                try:
                    self.wait_time(5)
                    delete_path = '//android.widget.TextView[@text="删除"]'
                    self.find_path(delete_path).click()
                except NoSuchElementException:
                    # 点击确认
                    self.find_id('android:id/button1').click()

    def move_ele(self, filename):
        """移动文件夹"""
        logging.info('开始执行文件移动')
        # 我的文件路劲
        my_file_path = '//android.widget.TextView[@text="我的文件"]'
        move_paths = '//android.widget.TextView[@text="移动"]'
        self.add_step()
        self.find_path(self.send_content).clear()
        self.find_path(self.send_content).send_keys(filename)
        self.find_path(self.add_folder_affirm).click()
        # 新建文件夹的元素地址
        new_add_folder = '//android.widget.TextView[@text="%s"]' % filename
        new_add_folder = self.find_path(new_add_folder)
        self.slide(new_add_folder)
        # 点击移动按钮
        self.find_path(self.move_path).click()
        self.wait_time(5)
        # 点击我的文件文件件
        self.find_path(my_file_path).click()
        self.find_path(move_paths).click()
        try:
            # 获取Toast提示
            message = '//*[@text=\'{}\']'.format('移动成功')
            toast_element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(message))
            logging.info(toast_element.text)
            return True
        except TimeoutException:
            self.get_screen_shot(self.module)
            return False
        finally:
            logging.info('文件移动结束')

    def delete_ele1(self):
        """删除回收站文件夹"""
        # 回收站的路径
        recycle_path = '//android.widget.TextView[@text="回收站"]'
        self.find_path(recycle_path).click()
        self.wait_time(5)
        try:
            while True:
                # logging.info('开始循环删除回收站%s' % num)
                # 第一个元素的路径
                ele_path = '//android.widget.TextView'
                ele_path = self.find_paths(ele_path)[2]
                time.sleep(1)
                self.slide(ele_path)
                # 确认删除按钮路径
                delete_path1 = '//android.widget.TextView[@text="确认删除"]'
                self.find_path(delete_path1).click()
                delete_path2 = '//android.widget.TextView[@text="删除"]'
                self.find_path(delete_path2).click()
                # 点击确认
                # self.find_id('android:id/button1').click()
                self.wait_time(5)
        except IndexError:
            logging.info('回收站清空完毕')

        except NoSuchElementException:
            logging.info('回收站清空完毕')
        except InvalidArgumentException:
            logging.info('回收站清空完毕')
        except Exception:
            logging.info('回收站清空完毕')
        finally:
            for i in range(10):
                self.go_back()
                if WebDriverWait(self.driver, 1).until(lambda x: x.find_element_by_xpath(
                        '//android.widget.TextView[@text="我的文件"]')):
                    break

    def delete_ele2(self):
        """删除文件主面板上的数据"""
        time.sleep(1)
        file_delete = self.find_paths('//android.widget.TextView')
        self.slide1(file_delete[16])
        # 确认删除按钮路径
        delete_path = '//android.widget.TextView[@text="删除"]'
        self.find_path(delete_path).click()
        self.wait_time(2)
        self.find_path(delete_path).click()
        # 点击确认
        # self.find_id('android:id/button1').click()
        self.wait_time(5)
        pass

    def rename_ele(self, filename):
        logging.info('文件重命名开始start')
        """重命名文件夹"""
        # 新建文件夹
        self.add_step()
        try:
            self.find_path(self.send_content).clear()
            self.find_path(self.send_content).send_keys(filename)
            self.find_path(self.add_folder_affirm).click()
            self.new_add_folder = '//android.widget.TextView[@text="%s"]' % filename
        except StaleElementReferenceException as e:
            logging.info(e)
            self.find_path(self.send_content).clear()
            self.find_path(self.send_content).send_keys(filename)
            self.find_path(self.add_folder_affirm).click()
            self.new_add_folder = '//android.widget.TextView[@text="%s"]' % filename


    def rename_ele2(self, sheet, name_path, a='2'):
        d_list, output_list = self.get_excel(sheet, name_path)
        if a == '1':
            self.datalist(d_list, self.new_add)
        else:
            self.datalist(d_list, self.new_add_folder)

    def datalist(self, datalist, new):
        for i in datalist:
            new_add_folder = self.find_path(new)
            self.slide(new_add_folder)
            self.find_path(self.rename_path).click()
            try:
                self.find_path(self.send_content).clear()
                self.find_path(self.send_content).send_keys(i)
                self.find_path(self.add_folder_affirm).click()
            except StaleElementReferenceException:
                self.find_path(self.send_content).clear()
                self.find_path(self.send_content).send_keys(i)
                self.find_path(self.add_folder_affirm).click()
            try:
                self.find_path(self.add_folder_cancel).click()
                continue
            except StaleElementReferenceException:
                # 新建文件夹的元素地址
                new = '//android.widget.TextView[@text="%s"]' % i
                if i == datalist[-1]:
                    self.new_add_folder = '//android.widget.TextView[@text="%s"]' % i
                continue
            except NoSuchElementException:
                # 新建文件夹的元素地址
                new = '//android.widget.TextView[@text="%s"]' % i
                if i == datalist[-1]:
                    self.new_add_folder = '//android.widget.TextView[@text="%s"]' % i
                continue

    def rename_ele3(self, sheet, name_path):
        """二级目录重命名"""
        logging.info('二级目录重命名')
        # 点击最后一个进入
        self.find_path(self.new_add_folder).click()
        # 点击右上角三横按钮
        new_path = '//android.widget.TextView'
        new_path = self.find_paths(new_path)
        time.sleep(0.5)
        new_path[2].click()
        time.sleep(0.5)
        # 点击新建文件夹按钮
        self.find_path(self.add_folder_button).click()
        # 点击新增的文件夹

        self.add_file1('i', tab=2, num=1)
        self.rename_ele2(sheet, name_path, a='1')
        self.go_back()
        logging.info('文件重命名结束End')

    def sort_ele(self):
        """文件和文件夹排序"""
        logging.info('文件排序开始start')
        # 先新建三个文件
        for i in range(3):
            self.add_file1(i)
        # 排序按钮地址
        sort_path = '//android.widget.TextView[@text="排序"]'
        # 选择名称排序
        name_sort = '//android.widget.TextView[@text="名称"]'
        # 选择时间排序
        time_sort = '//android.widget.TextView[@text="时间"]'
        # 选择文件大小排序
        size_sort = '//android.widget.TextView[@text="大小"]'
        # 完成按钮路劲
        accomplish = '//android.widget.TextView[@text="完成"]'
        for i in range(3):
            # 点击三横，
            self.add_step(tag=1)
            # 点击排序按钮
            self.find_path(sort_path).click()
            if i == 0:
                # 选择名称排序
                self.find_path(name_sort).click()
            elif i == 1:
                # 选择时间排序
                self.find_path(time_sort).click()
            elif i == 2:
                # 选择大小排序
                self.find_path(size_sort).click()
            # 点击完成按钮
            self.find_path(accomplish).click()
        logging.info('文件排序结束End')

    def multi_select(self, filename):
        """文件和文件夹多选"""
        logging.info('文件多选开始start')
        # 多选路径
        multi_select = '//android.widget.TextView[@text="多选"]'
        # 全选路径
        check_all = '//android.widget.TextView[@text="全选"]'
        # 反选路径
        invert_selection = '//android.widget.TextView[@text="反选"]'
        # 移动路径
        move_path = '//android.widget.TextView[@text="移动"]'
        # 新建文件夹按钮
        folder_path = '//android.widget.TextView[@text="新建文件夹"]'
        # 输入框路径
        # 点击三横，
        self.add_step(tag=1)
        # 点击多选按钮
        self.find_path(multi_select).click()
        # 点击全选按钮
        self.find_path(check_all).click()
        # 点击反选按钮
        self.find_path(invert_selection).click()
        # 点击全选按钮
        self.find_path(check_all).click()
        # 点击移动按钮
        self.find_path(move_path).click()
        # 点击新建文件夹按钮
        self.find_path(folder_path).click()
        # 输入文件夹名称
        self.find_path(self.send_content).clear()
        self.find_path(self.send_content).send_keys(filename)
        # 点击确认
        self.find_path(self.add_folder_affirm).click()
        # 打印文件夹名称
        logging.info('文件夹名称为：%s' % filename)
        # 新增文件夹的路径
        new_add = '//android.widget.TextView[@text="%s"]' % filename
        self.find_path(new_add).click()
        # 点击移动按钮
        self.find_path(move_path).click()
        logging.info('文件多选结束End')

    def add_step(self, tag=None):
        """新建流程"""
        time.sleep(0.5)
        # 点击右上角三横按钮
        new_path = '//android.widget.TextView'
        new_path = self.find_paths(new_path)
        new_path[1].click()
        time.sleep(0.5)
        # 为了排序时不点击这个文件
        if tag is None:
            # 点击新建文件夹按钮
            self.find_path(self.add_folder_button).click()


# if __name__ == '__main__':
#     driver = mind_desired()
#     fv = FileView(driver)
#     fv.add_file()
