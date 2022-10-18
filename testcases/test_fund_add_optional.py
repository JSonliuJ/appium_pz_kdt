# -- encoding: utf-8 --
# @time:    	2022/1/25 20:57
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com

import os
import sys
import pytest

local_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(local_path)

from common.app import APP
from common.file_handler import FileHandler
from common.yaml_handle import YamlHandler

FH = FileHandler()
test_search_file = os.path.join(FH.locator_path, 'test_search.yaml')
test_params = YamlHandler(test_search_file).read_yaml()


class TestFundAddOptional:
    """'添加自选"""
    def setup_class(self):
        self.app = APP()
        self.search = self.app.start().main().goto_search()  # app.start.main() 固定格式

    @pytest.mark.parametrize(['fund_subject', 'property_name'], test_params['fund_add_to_optional'])
    def test_add_to_optional(self, login,fund_subject, property_name):

        self.search.click_search_button()
        self.search.search_stock_or_fund(fund_subject)
        self.search.goto_synthesis().add_to_optional(property_name)
        text = self.search.goto_synthesis().is_and_optional_successful()
        assert text == "已添加到自选-我的基金"

    def teardown(self):




        self.app.back()

    def teardown_class(self):
        self.app.stop()
