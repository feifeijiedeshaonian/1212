from selenium import webdriver
from selenium. webdriver. support. wait import WebDriverWait
from selenium. webdriver. common. by import By
import time
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import os
import logging
import logging.config
import csv


class Base():

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def findElement(self, locator):
        ele = WebDriverWait(self.driver, self.timeout, self.t). until(lambda x: x.find_element(*locator))
        return ele
    
    def findElements(self, locator):
        ele = WebDriverWait(self.driver, self.timeout, self.t). until(lambda x: x.find_elements(*locator))
        return ele

    def ByAndroidUiautomator(self, element_name):
        time.sleep(1)
        for i in range(10):
            try:
                ret = self.driver.find_element_by_android_uiautomator(element_name)               
                return ret
            except Exception:
                print(u"loading:" + element_name)
                time.sleep(1)
                if i == n-1:
                    print("loading fail:"+element_name)
        raise Exception("element %s could not be found" % element_name)
        
    def sendKeys(self, locator, text):
        ele = self.findElement(locator)
        ele.send_keys(text)

    def click(self, locator):
        ele = self.findElement(locator)
        ele.click()

    def clear(self, locator):
        ele = self.findElement(locator)
        ele.clear()

    def isSelected(self, locator):
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r

    def isElementExist(self, locator):
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def isElementExist2(self, locator):
        eles = self.findElements(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print("定位到元素的个数：%s"%n)
            return True

    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H-%M", time.localtime())
        return self.now

    def screenShot(self, picture_name):
        localtime = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (picture_name, localtime)
        logging.info('get %s screenshot' % picture_name)
        self.driver.get_screenshot_as_file(image_file)

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipeLeft(self):
        l = self.get_size()
        x1 = int(l[0]*0.9)
        y1 = int(l[1]*0.5)
        x2 = int(l[0]*0.1)
        self.driver.swipe(x1, y1, x2, y1, 1000)

    def swipeUp(self):
        l = self.get_size()
        x1 = int(l[0]*0.5)
        y1 = int(l[1]*0.85)
        y2 = int(l[1]*0.15)
        self.driver.swipe(x1, y1, x1, y2, 1000)

    # 缩小
    def pinch(self):
        action1 = TouchAction(driver)
        action2 = TouchAction(driver)
        pinch_action = MultiAction(driver)
        l = self.get_size()
        action1.press(x=l[0]*0.2, y=l[1]*0.2).wait(1000).move_to(x=l[0]*0.4, y=l[1]*0.4).wait(1000).release()
        action2.press(x=l[0]*0.8, y=l[1]*0.8).wait(1000).move_to(x=l[0]*0.6, y=l[1]*0.6).wait(1000).release()
        pinch_action.add(action1, action2)
        pinch_action.perform()

    # 放大
    def zoom(self):
        action1 = TouchAction(driver)
        action2 = TouchAction(driver)
        zoom_action = MultiAction(driver)
        l = self.get_size()
        action1.press(x=l[0]*0.4, y=l[1]*0.4).wait(1000).move_to(x=l[0]*0.2, y=l[1]*0.2).wait(1000).release()
        action2.press(x=l[0]*0.6, y=l[1]*0.6).wait(1000).move_to(x=l[0]*0.8, y=l[1]*0.8).wait(1000).release()
        zoom_action.add(action1, action2)
        zoom_action.perform()

    def get_csv_data(self, csv_file, line):
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row


if __name__ == "__main__":
    driver = webdriver. Firefox()
    driver.get("https://www.zentao.net/user-login.html")
    zentao = Base(driver)
    loc1 = (By.ID, "account")
    loc2 = (By.NAME, "password")
    loc3 = (By.ID, "submit")
    zentao.sendKeys(loc1, "admin1")
    zentao.sendKeys(loc2, "123456")
    zentao.click(loc3)