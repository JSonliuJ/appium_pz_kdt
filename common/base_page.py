# -- encoding: utf-8 --
# @time:    	2022/1/25 20:57
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import os
import sys
local_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(local_path)

import datetime
import inspect
import json
import logging
import time
import pytest
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.wrapper import bounced_process
from common.yaml_handle import YamlHandler


class BasePage:
    _driver: WebDriver
    _test_params = {}

    today = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    today_file = time.strftime("%Y%m%d%H%M%S", time.localtime())

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def set_implicitly_wait(self, t):
        self._driver.implicitly_wait(t)

    def screen_shoot(self, file_name):
        self._driver.save_screenshot(file_name)

    def press_keycode_input(self, keycode):
        self._driver.press_keycode(keycode)

    def tap(self,bound):
        self._driver.tap(bound,)

    @bounced_process
    def find_ele(self, locator, value: str = None):
        element: WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        # element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(locator, value)
        return element

    @bounced_process
    def find_eles(self, locator, value: str = None):
        element: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            print(locator, value)
            elements = self._driver.find_elements(locator, value)
        return elements

    @bounced_process
    def find_element_and_text(self, locator, value: str = None):
        element: WebElement
        element_text = self._driver.find_element(*locator).text if isinstance(locator,
                                                                              tuple) else self._driver.find_element(
            locator, value).text
        return element_text

    def steps(self, path):
        # 操作步骤名称
        operate_name = inspect.stack()[1].function
        data = YamlHandler(path).read_yaml()
        steps = data[operate_name]

        str_instance = json.dumps(steps)
        for key, value in self._test_params.items():
            str_instance = str_instance.replace('${' + key + '}', value)
        steps = json.loads(str_instance)

        for step in steps:
            logging.info(step)
            if 'action' in step.keys():
                action = step['action']
                if action == 'click':
                    self.find_ele(step['by'], step['locator']).click()
                elif action == 'tap':
                    self._driver.tap([eval(step['locator'])],)
                elif action == 'send':
                    self.find_ele(step['by'], step['locator']).clear().send_keys(step['value'])
                elif action == 'secukey_input':
                    for index in step['value']:
                        # step['locator'] = str(step['locator']).replace('@text=""', '@text="{}"').format(index)
                        print(str(step['locator']).replace('@text=""', '@text="{}"').format(index))
                        self.find_ele(step['by'], str(step['locator']).replace('@text=""', '@text="{}"').format(index)).click()
                elif action == 'get_text':
                    text = self.find_ele(step['by'], step['locator']).text
                    if text:
                        return text
                    else:
                        logging.error('no find such text')
                        return
                elif action == "len>0":
                    eles = self.find_eles(step['by'], step['locator'])
                    return eles
            else:
                ele = self.find_ele(step['by'], step['locator'])
                return ele

    def swipe_screen(self, ele_text):
        """
        old=none
        new=driver.page_source
        while 滑动以前的内容 != 滑动以后的内容:
            如果元素找着了(driver.find_element()/page_source.find()):
                break
            如果没找着:
                滑动操作
                time.sleep(3)
                old = new
                new = driver.page_source
        """
        # 获取屏幕大小
        size = self._driver.get_window_size()
        old = None
        new = self._driver.page_source
        while old != new:
            try:
                self._driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % ele_text)
            except:
                self._driver.swipe(size['width'] * 0.5, size['height'] * 0.9, size['width'] * 0.5, size['height'] * 0.1,
                                   200)
                time.sleep(3)
                old = new
                new = self._driver.page_source
            else:
                logging.info('找到底部元素文本值')
                break

    def wait_ele_visible(self, loc, img_name, timeout=20, poll_fre=0.5):
        # 等待元素可见
        global end
        logging.info('{}等待{}元素可见'.format(img_name, loc))
        # 开始等待时间
        start = datetime.datetime.now()
        try:
            logging.info('等待元素可见开始时间：{}'.format(start))
            WebDriverWait(self._driver, timeout, poll_frequency=poll_fre).until(EC.visibility_of_element_located(loc))
        except:
            logging.exception('等待{}元素可见失败'.format(loc))
            raise
        else:
            # 结束等待时间
            end = datetime.datetime.now()
            logging.info('等待元素可见结束时间：{}'.format(end))
        wait_times = (end - start).seconds
        logging.info('总共等待时长:{}'.format(wait_times))

    def wait_element_exist(self, loc, img_name, timeout=20, poll_fre=0.5):
        # 等待元素存在
        global end
        logging.info('{}等待{}元素存在'.format(img_name, loc))
        # 开始等待时间
        start = datetime.datetime.now()
        try:
            logging.info('等待元素存在开始时间：{}'.format(start))
            WebDriverWait(self._driver, timeout, poll_frequency=poll_fre).until(EC.presence_of_element_located(loc))
        except:
            logging.exception('等待{}元素存在失败'.format(loc))
            raise
        else:
            # 结束等待时间
            end = datetime.datetime.now()
            logging.info('等待元素存在结束时间：{}'.format(end))
        wait_times = (end - start).seconds
        logging.info('总共等待时长:{}'.format(wait_times))

    def wait_ele_clickable(self, loc, img_name, timeout=20, poll_fre=0.5):
        # 等待元素可点击
        logging.info('{}等待{}元素可点击'.format(img_name, loc))
        # 开始等待时间
        try:
            WebDriverWait(self._driver, timeout, poll_frequency=poll_fre).until(EC.element_to_be_clickable(loc))
        except:
            logging.exception('等待{}元素可点击失败'.format(loc))
            raise