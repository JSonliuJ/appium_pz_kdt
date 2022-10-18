# -- encoding: utf-8 --
# @time:    	2022/1/25 20:57
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com

import os
from common.base_page import BasePage
from common.file_handler import FileHandler
from page.my import MY

class Login(BasePage):

    def user_pwd_login(self, property_name):

        self._test_params['property_name'] = property_name
        self.steps(os.path.join(FileHandler.locator_path, 'login.yaml'))
        return MY(self._driver)

    def iphone_login(self):
        from page.main import Main
        return Main(self._driver)

    def wx_login(self):
        pass

    def register(self):
        pass
