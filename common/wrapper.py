# -- encoding: utf-8 --
# @time:    	2022/1/25 20:57
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com

import logging
import os
from appium.webdriver.common.mobileby import MobileBy
from common.file_handler import FileHandler
import allure


def bounced_process(func):
    logging.basicConfig(level=logging.INFO)

    def wrapper(*args, **kwargs):
        from common.base_page import BasePage
        black_list = [
            # (MobileBy.XPATH, '//*[contains(@resource-id,"not_login_main_ll")]/text="立即登录"'),
            (MobileBy.XPATH, '//*[contains(@resource-id,"ll_content")]//*[@text="确定"]'), # 春节假期公告
            (MobileBy.XPATH, '//*[@text="确认"]'), # 确定按钮
            (MobileBy.XPATH, '//*[@content-desc="确认"]'),
            (MobileBy.XPATH, '//*[@text="继续下单"]'),
            (MobileBy.XPATH, '//*[@text="下次再说"]'),
            (MobileBy.XPATH, '//*[contains(@resource-id,"ll_dialog")]//*[@text="知道了"]'),  # 重要公告：知道了
            (MobileBy.XPATH, '//*[contains(@resource-id,"dialog_button_layout")]/text="确认"'),  # 确认退出登录按钮
            (MobileBy.XPATH, '//*[@resource-id="com.hundsun.winner.pazq:id/BTN_close"]'),  # 确认关闭按钮
            (MobileBy.XPATH, '//*[@resource-id="com.hundsun.winner.pazq:id/tip_del"]'),  # x提示弹框
            (MobileBy.XPATH, '//*[@resource-id="com.hundsun.winner.pazq:id/search_home_clear_iv"]')  # 搜索按钮的x

        ]
        _max_num = 2
        _error_num = 0
        instance: BasePage = args[0]
        try:
            logging.info("run func_name：" + str(func.__name__) + "\n args：" + repr(args[1:]) + "\t" + "kwargs：" + repr(kwargs))
            element = func(*args, **kwargs)
            _error_num = 0
            instance.set_implicitly_wait(6)
            return element
        except Exception as e:
            file_name = '%s.png' % str(instance.today_file)
            instance.screen_shoot(file_name)
            with open(file_name, 'rb') as f:
                content = f.read()
            allure.attach(content, name=file_name, attachment_type=allure.attachment_type.PNG)
            logging.error("element not found, bounced handle！")
            instance._driver.get_screenshot_as_png()
            # 出现弹框异常，减少隐式等待时间，提升处理速度
            instance.set_implicitly_wait(0.5)
            # 当查找弹框元素超过3次未找到，抛出异常
            if _error_num > _max_num:
                raise e
            _error_num += 1
            for ele in black_list:
                logging.info(ele)
                ele_lists = instance.find_eles(*ele)
                if len(ele_lists) > 0:
                    ele_lists[0].click()
                    return wrapper(*args, **kwargs)
            raise e

    return wrapper
