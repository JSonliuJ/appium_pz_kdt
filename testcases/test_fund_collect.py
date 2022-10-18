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
test_search_file = os.path.join(FH.locator_path, 'test_search.yaml')
test_params = YamlHandler(test_search_file).read_yaml()


class TestFundOrCollect:
    """基金收藏"""
    def setup_class(self):
        self.app = APP()
        self.search = self.app.start().main().goto_search().click_search_button()

    @pytest.mark.parametrize(['fund_subject', 'property_name', 'instance_index'], test_params['fund_collect'])
    def test_fund_collect(self, fund_subject, property_name, instance_index):
        self.search.search_stock_or_fund(fund_subject)
        self.search.goto_synthesis().click_fund_or_stock_info_button(property_name,instance_index)
        self.goto_fun_info = self.search.goto_synthesis().goto_fund_info()
        self.goto_fun_info.add_collect()

    def teardown(self):
        self.app.back()

    def teardown_class(self):
        self.app.stop()
