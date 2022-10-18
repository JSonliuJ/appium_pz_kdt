# -- encoding: utf-8 --
# @time:    	2022/2/19 15:58
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
from common.base_page import BasePage
from page.subpage.progenypage.fund_position import FundPosition


class Fund(BasePage):
    # 路径：自选页-->自选-->基金栏
    def goto_fund_option(self):
        # 基金自选
        pass

    def goto_fund_position(self) -> FundPosition:
        # 基金持仓
        return FundPosition(self._driver)