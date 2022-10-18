# -- encoding: utf-8 --
# @time:    	2022/1/25 20:57
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import os
import sys

local_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(local_path)

import pytest
from common.app import APP
from common.file_handler import FileHandler
from common.yaml_handle import YamlHandler

FH = FileHandler()
test_search_file = os.path.join(FH.locator_path, 'test_fund.yaml')
test_params = YamlHandler(test_search_file).read_yaml()


class TestFundOrCollect:
    def setup_class(self):
        self.app = APP()
        self.fund = self.app.start().main().goto_fund()
        self.fund.click_fund_button()
        self.ofc = self.fund.goto_customize_pages().click_customize_page_button()

    @pytest.mark.parametrize(['property_name', 'instance_index'], test_params['fund_purchase'])
    def test_fund_purchase(self, property_name, instance_index):
        self.ofc.click_added_optional_fund_button(property_name, instance_index)
        self.fund_info = self.ofc.goto_fund_info()
        self.fund_info.click_purchase_button()

    def teardown(self):
        self.app.back()

    def teardown_class(self):
        self.app.stop()
