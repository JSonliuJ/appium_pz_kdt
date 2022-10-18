# -- encoding: utf-8 --
# @time:    	2022/1/29 15:18
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import os
from common.base_page import BasePage
from common.file_handler import FileHandler
from page.subpage.progenypage.fund_info import FundInfo


class OptionalFundColumn(BasePage):

    def click_added_optional_fund_button(self, property_name, instance_index):
        self._test_params['property_name'] = property_name
        self._test_params['instance_index'] = instance_index
        self.steps(os.path.join(FileHandler.locator_path, 'fund.yaml'))

    def goto_fund_info(self):
        return FundInfo(self._driver)
