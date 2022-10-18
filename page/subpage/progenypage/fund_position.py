# -- encoding: utf-8 --
# @time:    	2022/2/19 16:03
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import os

from common.base_page import BasePage
from common.file_handler import FileHandler
from common.yaml_handle import YamlHandler

path = os.path.join(FileHandler.locator_path, 'fund_position.yaml')
data = YamlHandler(path).read_yaml()['confirm_pay_and_input_pwd']
print(data)
class FundPosition(BasePage):
    def goto_position_fund_manage(self, fund_name):
        # 点击基金进入基金详情
        self._test_params['fund_name'] = fund_name
        print("params",self._test_params)
        self.steps(os.path.join(FileHandler.locator_path, 'fund_position.yaml'))

    def goto_redemption_or_conversion(self):
        # 赎回/转换
        pass

    def goto_fixed_input(self,fixed_amount):
        # 定投
        pass

    def goto_continue_buy(self, buy_amount):
        # 继续购买
        self._test_params['buy_amount'] = buy_amount
        self.steps(os.path.join(FileHandler.locator_path, 'fund_position.yaml'))

    def confirm_pay_and_input_pwd(self):
        self.steps(os.path.join(FileHandler.locator_path, 'fund_position.yaml'))

    def is_continue_buy_succeessful(self):
        text = self.steps(os.path.join(FileHandler.locator_path, 'fund_position.yaml'))
        return text

    def click_complete_button(self):
        self.steps(os.path.join(FileHandler.locator_path, 'fund_position.yaml'))
        return self
