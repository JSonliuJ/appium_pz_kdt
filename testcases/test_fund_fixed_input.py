# -- encoding: utf-8 --
# @time:    	2022/4/7 0:01
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import os
import sys
import time

local_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(local_path)

import pytest
from common.app import APP
from common.file_handler import FileHandler
from common.yaml_handle import YamlHandler

FH = FileHandler()
test_fund_position = os.path.join(FH.locator_path, 'test_fund_position.yaml')
test_params = YamlHandler(test_fund_position).read_yaml()


class TestFundContinueBuy:

    def setup_class(self):
        self.app = APP()
        self.option = self.app.start().optional().goto_option()
        self.fund_position = self.option.goto_fund().goto_fund_position()

    @pytest.mark.parametrize(['fund_name', 'fixed_amount'], test_params['fund_fixed_input'])
    def test_fund_fixed_input(self, fund_name, fixed_amount):
        self.option.click_optional_button()
        self.fund_position.goto_position_fund_manage(fund_name)

        self.fund_position.goto_fixed_input(fixed_amount)
