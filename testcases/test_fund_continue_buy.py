# -- encoding: utf-8 --
# @time:    	2022/2/19 16:06
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

    @pytest.mark.parametrize(['fund_name', 'buy_amount'], test_params['fund_continue_buy'])
    def test_fund_continue_buy(self, fund_name, buy_amount):
        self.option.click_optional_button()
        self.fund_position.goto_position_fund_manage(fund_name)

        self.fund_position.goto_continue_buy(buy_amount)
        time.sleep(15)
        self.fund_position.confirm_pay_and_input_pwd()
        text = self.fund_position.is_continue_buy_succeessful()
        assert '订单提交成功' in text
        self.fund_position.click_complete_button()
