# -*- coding:utf-8 -*-
import unittest
import logging
from time import sleep

from common.desired_caps import mind_desired


class StartEnd(unittest.TestCase):
    driver = mind_desired()
    @classmethod
    def setUp(cls):
        # logging.info('----------自动化开始测试----------')
        pass

    @classmethod
    def tearDown(cls):
        # logging.info('----------自动化测试结束----------')
        # sleep(5)
        # self.driver.close_app()
        pass

