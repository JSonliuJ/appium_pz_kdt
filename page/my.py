# -- encoding: utf-8 --
# @time:    	2022/1/25 20:57
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com

import os
from appium.webdriver.common.mobileby import MobileBy
from common.base_page import BasePage
from common.file_handler import FileHandler
from common.yaml_handle import YamlHandler

config_file = os.path.join(FileHandler.config_path, 'config.yaml')


class MY(BasePage):

    def goto_login(self):
        from page.subpage.login import Login
        return Login()

    def is_login_successful(self):
        # self.find_ele(MobileBy.XPATH,
                      # YamlHandler(config_file).read_yaml()['main_tab_locator']['my']).click()
        text = self.steps(os.path.join(FileHandler.locator_path, 'my.yaml'))
        return text

    def click_logout_button(self):
        # 点击退出登录按钮
        self.steps(os.path.join(FileHandler.locator_path, 'my.yaml'))