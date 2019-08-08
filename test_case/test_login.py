from myunit import StartEnd
import unittest
import logging
import sys
sys.path.append(r'E:\python\zk-appium\businessView')
from loginView import LoginView


class LoginTest(StartEnd):
    csv_file = r'E:/python/zk-appium/data/abc.csv'
    
    def test_login1(self):
        logging.info("========test_login1========")
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 1)
        l.login_action(data[0], data[1])
        self.assertTrue(l.check_loginStatus())


if __name__ == "__main__":
    unittest.main()