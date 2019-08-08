import logging
from selenium. webdriver. common. by import By
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
# from appium.webdriver.common.multi_action import MultiAction
import re
import sys
sys.path.append(r'E:\python\zk-appium\common')
from common import Base
from desired_caps import appium_desired
from time import sleep


class ZhiXin(Base):
    
    def login_zx1(self, username, password):
        base = Base(self.driver)
        
        skip = base.isElementExist([By.ID, "com.cnmts.smart_message:id/tv_jump"])
        if skip:
            base.click([By.ID, "com.cnmts.smart_message:id/tv_jump"])
        else:
            pass
        for i in range(5):
            logging.info("======quanxian_setting======")
            permission_allow = base.isElementExist([By.ID, "com.android.packageinstaller:id/permission_allow_button"])
            if permission_allow:
                logging.info("======quanxian_cunzai======")
                base.click([By.ID, "com.android.packageinstaller:id/permission_allow_button"])
            else:
                break
        logging.info("======login zhixin======")
        base.click([By.ID, "com.cnmts.smart_message:id/tv_change_user"])
        base.sendKeys([By.ID, "com.cnmts.smart_message:id/et_username"], username)
        base.sendKeys([By.ID, "com.cnmts.smart_message:id/et_pwd"], password)
        base.click([By.ID, "com.cnmts.smart_message:id/btn_login"])
        # 需要加一个新用户的判断


        # 电池优化权限
        self.driver.implicitly_wait(40)
        button = base.isElementExist([By.ID, "android:id/button1"])
        if button:
            base.click([By.ID, "android:id/button1"])
        else:
            pass

    def login_zx2(self, username="13820921009", password="960811kai"):
        base = Base(self.driver)
        skip = base.isElementExist([By.ID, "com.cnmts.smart_message:id/tv_jump"])
        if skip:
            base.click([By.ID, "com.cnmts.smart_message:id/tv_jump"])
        else:
            pass
        logging.info("======login zhixin======")
        base.click([By.ID, "com.cnmts.smart_message:id/tv_change_user"])
        base.sendKeys([By.ID, "com.cnmts.smart_message:id/et_username"], username)
        base.sendKeys([By.ID, "com.cnmts.smart_message:id/et_pwd"], password)
        base.click([By.ID, "com.cnmts.smart_message:id/btn_login"])
    
    # 初始化，回到智信界面
    def initialize(self):
        logging.info("========initialize========")
        base = Base(self.driver)
        for i in range(10):
            myself = base.isElementExist([By.ID, "com.cnmts.smart_message:id/message"])
            if myself:
                base.click([By.ID, "com.cnmts.smart_message:id/message"])
                break
            else:
                self.driver.keyevent(4)

    # 退出登录
    def login_out_zx(self):
        base = Base(self.driver)
        logging.info("========login out========")
        for i in range(10):
            myself = base.isElementExist([By.ID, "com.cnmts.smart_message:id/people"])
            if myself:
                base.click([By.ID, "com.cnmts.smart_message:id/people"])
                break
            else:
                self.driver.keyevent(4)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("退出登录")').click()
        sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()

    # 判断是否登录成功
    def login_status(self):
        base = Base(self.driver)
        ele = base.isElementExist([By.ID, "com.cnmts.smart_message:id/img_ming_lu"])
        if ele:
            logging.info("========login success========")
            return True
        else:
            logging.info("========login fail========")
            base.screenShot("login_zx fail")
            return False

    # 智信页面搜索
    def search(self, keyword):
        logging.info("========start serch========")
        base = Base(self.driver)
        base.click([By.ID, "com.cnmts.smart_message:id/search"])
        base.sendKeys([By.ID, "com.cnmts.smart_message:id/query"], keyword)
        base.click([By.ID, "com.cnmts.smart_message:id/layout_item"])

    # 加号建群
    def create_group1(self):
        base = Base(self.driver)
        base.click([By.ID, "com.cnmts.smart_message:id/img_show_more"])
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("发起群聊")').click()
        base.click([By.ID, "com.cnmts.smart_message:id/tv_title"])
        base.findElements([By.ID, "com.cnmts.smart_message:id/tv_full_name"])[1].click()
        sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("智能平台研发部")').click()
        base.findElements([By.ID, "com.cnmts.smart_message:id/radio_select"])[3].click()
        base.click([By.ID, "com.cnmts.smart_message:id/btn_ok"])
    
    # 组织架构建群
    def create_group2(self):
        base = Base(self.driver)
        base.click([By.ID, "com.cnmts.smart_message:id/img_ming_lu"])
        base.click([By.ID, "com.cnmts.smart_message:id/img_sub_head"])
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("发起群聊")').click()
        base.click([By.ID, "com.cnmts.smart_message:id/tv_title"])
        base.findElements([By.ID, "com.cnmts.smart_message:id/tv_full_name"])[1].click()
        sleep(1)
        base.ByAndroidUiautomator('new UiSelector().text("智能平台研发部")').click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("智能平台研发部")').click()
        # base.ByAndroidUiautomator('new UiSelector().text("测试组（平台）")').click()
        base.findElements([By.ID, "com.cnmts.smart_message:id/radio_select"])[3].click()
        base.click([By.ID, "com.cnmts.smart_message:id/btn_ok"])

    # 根据群名称判断,创建群后直接到新群界面
    def create_group_status(self):
        title = Base(self.driver).isElementExist([By.ID, "com.cnmts.smart_message:id/tv_title"])
        if title:
            logging.info("========create group success========")
            return True
        else:
            logging.info("========create group fail========")
            return False

    # 发送文字与表情
    def send_word(self, word):
        base = Base(self.driver)
        for i in range(2):
            base.sendKeys([By.ID, "com.cnmts.smart_message:id/rc_edit_text"], word)
            base.click([By.ID, "com.cnmts.smart_message:id/rc_send_toggle"]) 
        base.click([By.ID, "com.cnmts.smart_message:id/rc_emoticon_toggle"])
        for i in range(3):
            base.click([By.ID, "com.cnmts.smart_message:id/rc_ext_emoji_item"])
        base.click([By.ID, "com.cnmts.smart_message:id/rc_send_toggle"])

    def send_picture(self):
        # 发送图片
        base = Base(self.driver)
        # 需要加+的判断
        ele = base.isElementExist([By.ID, "com.cnmts.smart_message:id/rc_ext_plugin_icon"])
        if ele:
            pass
        else:
            base.click([By.ID, "com.cnmts.smart_message:id/rc_plugin_toggle"])
        base.findElements([By.ID, "com.cnmts.smart_message:id/rc_ext_plugin_icon"])[0].click()
        base.click([By.ID, "com.cnmts.smart_message:id/tv_select"])
        base.click([By.ID, "com.cnmts.smart_message:id/tv_confirm"])

    def take_photo(self):
        # 拍摄图片
        base = Base(self.driver)
        ele = base.isElementExist([By.ID, "com.cnmts.smart_message:id/rc_ext_plugin_icon"])
        if ele:
            pass
        else:
            base.click([By.ID, "com.cnmts.smart_message:id/rc_plugin_toggle"])  
        base.findElements([By.ID, "com.cnmts.smart_message:id/rc_ext_plugin_icon"])[1].click() 
        sleep(2)
        base.findElements([By.CLASS_NAME, "android.view.View"])[1].click()
        sleep(2)
        base.findElements([By.CLASS_NAME, "android.view.View"])[1].click()

    def send_location(self):
        # 发送位置
        base = Base(self.driver)
        ele = base.isElementExist([By.ID, "com.cnmts.smart_message:id/rc_ext_plugin_icon"])
        if ele:
            pass
        else:
            base.click([By.ID, "com.cnmts.smart_message:id/rc_plugin_toggle"])
        base.findElements([By.ID, "com.cnmts.smart_message:id/rc_ext_plugin_icon"])[2].click()
        base.click([By.ID, "com.cnmts.smart_message:id/btn_location_send"])

    def send_document(self):
        # 发送文件
        base = Base(self.driver)
        ele = base.isElementExist([By.ID, "com.cnmts.smart_message:id/rc_ext_plugin_icon"])
        if ele:
            pass
        else:
            base.click([By.ID, "com.cnmts.smart_message:id/rc_plugin_toggle"])
        base.findElements([By.ID, "com.cnmts.smart_message:id/rc_ext_plugin_icon"])[3].click()
        base.click([By.ID, "com.cnmts.smart_message:id/radio_select"])
        base.click([By.ID, "com.cnmts.smart_message:id/layout_send"])
        # self.driver.keyevent(4)
        # self.driver.keyevent(4)
    
    def group_setting_name(self, rename):
        base = Base(self.driver)
        # 点击群设置
        base.click([By.ID, "com.cnmts.smart_message:id/btn_right"])
        # 更改群名称
        base.click([By.ID, "com.cnmts.smart_message:id/tv_change_group_name"])
        base.sendKeys([By.ID, "com.cnmts.smart_message:id/et_content"], rename)
        base.click([By.ID, "com.cnmts.smart_message:id/tv_save"])

    # 群减人
    def group_setting_group1(self):
        base = Base(self.driver)
        # 点击群设置
        base.click([By.ID, "com.cnmts.smart_message:id/btn_right"])
        # 群减人
        number = base.findElement([By.ID, "com.cnmts.smart_message:id/tv_group_member_size"]).text
        a = re.findall(r"\d+\.?\d*", number)
        b = int(a[0])
        if b < 4:
            c = b + 2
            base.findElements([By.ID, "com.cnmts.smart_message:id/iv_avatar"])[c].click()
        else:
            base.findElements([By.ID, "com.cnmts.smart_message:id/iv_avatar"])[6].click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("任少龙")').click()
        base.click([By.ID, "com.cnmts.smart_message:id/btn_sure"])
        sleep(2)

    # 群加人
    def group_setting_group2(self):
        base = Base(self.driver)
        # 点击群设置
        base.click([By.ID, "com.cnmts.smart_message:id/btn_right"])
        number = base.findElement([By.ID, "com.cnmts.smart_message:id/tv_group_member_size"]).text
        a = re.findall(r"\d+\.?\d*", number)
        b = int(a[0])
        # 群加人
        if b < 3:
            d = b + 1
            base.findElements([By.ID, "com.cnmts.smart_message:id/iv_avatar"])[d].click()
        else:
            sleep(2)
            base.findElements([By.ID, "com.cnmts.smart_message:id/iv_avatar"])[5].click()
        base.click([By.ID, "com.cnmts.smart_message:id/query"])
        base.sendKeys([By.ID, "com.cnmts.smart_message:id/query"], "王德晨")
        base.click([By.ID, "com.cnmts.smart_message:id/radio_select"])
        base.click([By.ID, "com.cnmts.smart_message:id/btn_ok"])
    
    def group_setting_group3(self):
        base = Base(self.driver)
        # 点击群设置
        base.click([By.ID, "com.cnmts.smart_message:id/btn_right"])
        # 解散群聊
        sleep(2)
        base.click([By.ID, "com.cnmts.smart_message:id/btn_exit_group"])
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()
    
    # 长按
    def longpress(self):
        base = Base(self.driver)
        el = base.findElements([By.ID, "com.cnmts.smart_message:id/text_message"])[0]
        TouchAction(self.driver).long_press(el, 1000).perform()
        # sleep(3)
        # base.ByAndroidUiautomator(ele).click()

    # # 复制
    # def copy(self):
    #     base = Base(self.driver)
    #     ZhiXin(self.driver).longpress()
    #     base.ByAndroidUiautomator('new UiSelector().text("复制")').click()
    #     ele = base.findElement([By.ID, "com.cnmts.smart_message:id/rc_edit_text"])


if __name__ == "__main__":  
    driver = appium_desired()
    ZhiXin(driver).login_zx1("13820921009", "960811kai")
    ZhiXin(driver).create_group2()
    # ZhiXin(driver).send_word("测试自动化")
    # ZhiXin(driver).send_picture()
    # ZhiXin(driver).take_photo()
    # ZhiXin(driver).send_location()
    # ZhiXin(driver).send_document()
    # ZhiXin(driver).group_setting_name("孙悟空")
    

