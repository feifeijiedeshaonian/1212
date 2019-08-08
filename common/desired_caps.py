from appium import webdriver
from time import sleep
import yaml
import logging
import logging.config
import os


base_dir = os.path.dirname(os.path.dirname(__file__))
CON_LOG = os.path.join(base_dir, 'config', 'log.conf')
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def appium_desired():

    yaml_path = os.path.join(base_dir, 'config', 'desired_caps.yaml')

    with open(yaml_path, 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    desired_caps = {}
    desired_caps["platformName"] = data["platformName"]
    desired_caps["platformVersion"] = data["platformVersion"]
    desired_caps["deviceName"] = data["deviceName"]
    desired_caps["udid"] = data["udid"]
    app_path = os.path.join(base_dir, 'app', data['appname'])
    desired_caps["app"] = app_path
    desired_caps["appPackage"] = data["appPackage"]
    desired_caps["appActivity"] = data["appActivity"]
    desired_caps["noReset"] = data["noReset"]
    desired_caps["unicodeKeyboard"] = data["unicodeKeyboard"]
    desired_caps["resetKeyboard"] = data["resetKeyboard"]
    desired_caps['automationName'] = 'uiautomator2'
    logging.info("start app...")
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    sleep(5)
    return driver


if __name__ == "__main__":
    appium_desired()