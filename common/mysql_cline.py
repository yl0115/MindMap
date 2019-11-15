import pymysql
from common.functions import Common
import logging


class SQLConnect(object):
    def __init__(self):
        # 初始化数据库连接信息
        self.db = pymysql.connect('rm-bp1u5te59xv7096ye9o.mysql.rds.aliyuncs.com', 'root', 'Naotu2020_wyf777', 'mind_map')
        # 获取游标
        self.cursor = self.db.cursor()
        self.old_tel = ''
        self.new_tel = ''

    def update_tel(self):

        """
        在数据库中删除，更换后的手机号码
        :return:
        """
        csv_file = '../data/login/login_input.csv'
        # 循环编辑，行数从2开始读取
        for i in range(10, len(csv_file)):
            # 调用读取csv方法并传入行数
            data = Common.get_csv_data(csv_file, i)
            if data is None:
                break
            self.new_tel = data[2]
            self.old_tel = data[7]
            # sql = "update user set tel='%s' where tel='%s'" % (self.new_tel, self.old_tel)
            sql = "delete from user where tel='%s'" % self.old_tel
            try:
                self.cursor.execute(sql)
                self.db.commit()
            except Exception as e:
                logging.info(e)
                self.db.rollback()
            else:
                break

    def select_tel(self):
        """
        查询信息是否被删除
        :return:
        """
        sql = "select * from user where tel='%s'" % self.new_tel
        try:
            self.cursor.execute(sql)
            self.db.commit()
            # 获取字段的描述，默认获取数据库字段名称，重新定义时通过AS关键重新命名即可
            desc = self.cursor.description
            # 列表表达式把数据组装起来
            data_dict = [dict(zip([col[0] for col in desc], row)) for row in self.cursor.fetchall()]
            return data_dict[0]['tel']
        except Exception as e:
            logging.info(e)
            pass
        finally:
            self.db.close()


if __name__ == '__main__':
    import time
    sc = SQLConnect()
    sc.update_tel()
    time.sleep(5)
    sc.select_tel()
