# -- encoding: utf-8 --
# @time:    	2022/1/25 20:57
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com

# 自选页
from common.base_page import BasePage

from page.subpage.progenypage.option import Option


class Optional(BasePage):

    def goto_option(self) -> Option:
        return Option(self._driver)

    def goto_market(self):
        pass

    def goto_serarch(self):
        pass
