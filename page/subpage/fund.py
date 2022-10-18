# -- encoding: utf-8 --
# @time:    	2022/1/29 14:34
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import os

from common.base_page import BasePage
from common.file_handler import FileHandler
from page.subpage.progenypage.customize_pages import CustomizePages
from page.subpage.progenypage.market_place import MarketPlace
from page.subpage.progenypage.product_search import ProductSearch


class Fund(BasePage):

    def click_fund_button(self):
        self.steps(os.path.join(FileHandler.locator_path, 'fund.yaml'))

    def goto_product_search(self) -> ProductSearch:
        # 产品搜索框
        return ProductSearch(self._driver)

    def goto_marketplace(self) -> MarketPlace:
        # 市场页
        return MarketPlace(self._driver)

    def goto_customize_pages(self) -> CustomizePages:
        # 自选页：自选基金、持仓基金。。。
        return CustomizePages(self._driver)


