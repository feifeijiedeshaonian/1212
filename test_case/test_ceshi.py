# from myunit import StartEnd
import unittest
from time import sleep
# import logging
import sys
sys.path.append(r'E:\python\zk-appium\businessView')
sys.path.append(r'E:\python\zk-appium\common')
from zhixin_basics import ZhiXin
from desired_caps import appium_desired


class CreateGroup(unittest.TestCase):
    # def setUp(self):
    #     logging.info("======== setUp========")
    #     ZhiXin(self.driver).initialize()

    # def tearDown(self):
    #     logging.info("========tearDown========")
    #     sleep(3)
    #     self.driver.close_app()

    @classmethod
    def setUpClass(cls):
        # logging.info("======== setUpClass========")
        cls.driver = appium_desired()
        status = ZhiXin(cls.driver).login_status
        if status:
            ZhiXin(cls.driver).login_out_zx()
        else:
            pass
        ZhiXin(cls.driver).login_zx2()

    @classmethod
    def tearDownc(cls):
        # logging.info("========tearDownClass========")
        sleep(3)
        ZhiXin(cls.driver).login_out_zx()
        cls.driver.close_app()

    # 右上角加号建群
    def test1(self):
        zhixin = ZhiXin(self.driver)
        zhixin.initialize()
        zhixin.create_group1()
        sleep(3)

    # 组织架构建群
    def test2(self):
        zhixin = ZhiXin(self.driver)
        zhixin.initialize()
        zhixin.create_group2()
        sleep(3)

    # 发送文字与表情
    def test3(self):
        zhixin = ZhiXin(self.driver)
        zhixin.initialize()
        zhixin.create_group1()
        zhixin.send_word("测试测试，软件测试")
        sleep(3)
    
    # 发送图片
    def test4(self):
        zhixin = ZhiXin(self.driver)
        zhixin.initialize()
        zhixin.create_group1()
        zhixin.send_picture()
        sleep(3)

    # 拍摄图片发送
    def test5(self):
        zhixin = ZhiXin(self.driver)
        zhixin.initialize()
        zhixin.create_group1()
        zhixin.take_photo()
        sleep(3)

    # 发送位置
    def test6(self):
        zhixin = ZhiXin(self.driver)
        zhixin.initialize()
        zhixin.create_group1()       
        zhixin.send_location()
        sleep(3)

    # 发送文件
    def test7(self):
        zhixin = ZhiXin(self.driver)
        zhixin.initialize()
        zhixin.create_group1()  
        zhixin.send_document()
        sleep(3)
    
    # 更改群名称
    def test8(self):
        zhixin = ZhiXin(self.driver)
        zhixin.initialize()
        zhixin.create_group1()
        zhixin.group_setting_name("猪八戒")
        sleep(3)

    # 群减人
    def test9(self):
        zhixin = ZhiXin(self.driver)
        zhixin.initialize()
        zhixin.create_group1()
        zhixin.group_setting_group1()
        sleep(3)

    # 群加人
    def test10(self):
        zhixin = ZhiXin(self.driver)
        zhixin.initialize()
        zhixin.create_group1()
        zhixin.group_setting_group2()
        sleep(3)

    # 群解散
    def test11(self):
        zhixin = ZhiXin(self.driver)
        zhixin.initialize()
        zhixin.create_group1()
        zhixin.group_setting_group3()
        sleep(3)


if __name__ == "__main__":
    unittest.main()