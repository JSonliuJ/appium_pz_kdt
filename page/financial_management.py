# -- encoding: utf-8 --
# @time:    	2022/1/25 20:57
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com

from common.base_page import BasePage
from page.main import Main

main = Main()


class FinancialManagement(BasePage):

    def goto_fund(self):
        main.goto_fund()
