# -- encoding: utf-8 --
# @time:    	2022/1/25 20:57
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com

# sys.path.append('..') 此方式尝试无法正常导入
import os
import sys
import pytest

local_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(local_path)

from common.app import APP
from common.file_handler import FileHandler
from common.yaml_handle import YamlHandler

FH = FileHandler()
test_login_file = os.path.join(FH.locator_path, 'test_login.yaml')
test_params = YamlHandler(test_login_file).read_yaml()


class TestLogin():

    def setup_class(self):
        self.app = APP()
        self.login = self.app.start().main().goto_login()

    @pytest.mark.parametrize('property_name', test_params)
    def test_uer_pwd_login(self, property_name):
        my = self.login.user_pwd_login(property_name)
        user_name = my.is_login_successful()
        assert user_name == '股神55531447'
        my.swipe_screen('平安证券')
        my.click_logout_button()

    def teardown(self):
        self.app.back()

    def teardown_class(self):
        self.app.stop()
