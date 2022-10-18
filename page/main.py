# -- encoding: utf-8 --
# @time:    	2022/1/25 20:57
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com

# 首页
from common.base_page import BasePage
from page.subpage.fund import Fund
from page.subpage.login import Login
from page.subpage.search import Search


class Main(BasePage):

    def goto_login(self) -> Login:
        return Login(self._driver)

    def goto_search(self) -> Search:
        # 搜索
        # self._driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.hundsun.winner.pazq:id/tvOnSearch"]').click()
        return Search(self._driver)

    def goto_massage(self):
        # 消息
        pass

    def goto_robot(self):
        pass

    def goto_check_balance(self):
        # 查看资产
        pass

    def goto_fund(self) -> Fund:
        # 基金页
        return Fund(self._driver)

