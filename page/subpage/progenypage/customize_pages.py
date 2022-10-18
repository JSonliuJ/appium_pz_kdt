# -- encoding: utf-8 --
# @time:    	2022/1/29 14:57
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import os

from common.base_page import BasePage
from common.file_handler import FileHandler
from page.subpage.progenypage.optional_fund_column import OptionalFundColumn


class CustomizePages(BasePage):
    # 基金自选页
    def click_customize_page_button(self):
        # 自选页按钮
        self.steps(os.path.join(FileHandler.locator_path, 'fund.yaml'))
        return OptionalFundColumn(self._driver)

    def goto_optional_fund_column(self) -> OptionalFundColumn:
        # 自选基金栏
        return OptionalFundColumn(self._driver)

    def goto_open_fund(self):
        pass

    def goto_thread(self):
        # 线索
        pass

    def goto_fund_ranking(self):
        # 基金排行页
        pass

    def goto_optional_information(self):
        # 资讯页
        pass