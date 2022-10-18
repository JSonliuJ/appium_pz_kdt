# -- encoding: utf-8 --
# @time:    	2022/1/25 20:57
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import os

from common.base_page import BasePage
from common.file_handler import FileHandler
from page.subpage.progenypage.synthesis import Synthesis


class Search(BasePage):

    def click_search_button(self):
        self.steps(os.path.join(FileHandler.locator_path, 'search.yaml'))
        return Search(self._driver)

    def search_stock_or_fund(self, fund_subject):
        self._test_params['fund_subject'] = fund_subject
        self.steps(os.path.join(FileHandler.locator_path, 'search.yaml'))

    def goto_synthesis(self) -> Synthesis:
        # 综合页
        return Synthesis(self._driver)

    def goto_stack_list_more(self):
        # 基金榜单更多
        pass

    def goto_fund_list_more(self):
        "股票榜单更多"
        pass
