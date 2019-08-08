import unittest
from time import sleep
import sys
sys.path.append(r'E:\python\zk-appium\common')
from common import Base
from desired_caps import appium_desired
import logging
sys.path.append(r'E:\python\zk-appium\businessView')
from zhixin_basics import ZhiXin


class StartEnd(unittest.TestCase):

    # def setUp(self):
    #     logging.info("======== setUp========")
    #     ZhiXin(self.driver).initialize()

    # def tearDown(self):
    #     logging.info("========tearDown========")
    #     sleep(3)
    #     self.driver.close_app()

    @classmethod
    def setUpClass(cls):
        logging.info("======== setUpClass========")
        cls.driver = appium_desired()
        status = ZhiXin(cls.driver).login_status
        if status:
            ZhiXin(cls.driver).login_out_zx()
        else:
            pass
        ZhiXin(cls.driver).login_zx2()

    @classmethod
    def tearDownc(cls):
        logging.info("========tearDownClass========")
        sleep(3)
        ZhiXin(cls.driver).login_out_zx()
        cls.driver.close_app()