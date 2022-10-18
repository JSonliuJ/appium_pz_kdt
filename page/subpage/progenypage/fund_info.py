# -- encoding: utf-8 --
# @time:    	2022/1/25 20:57
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import os

from appium.webdriver.common.mobileby import MobileBy

from common.base_page import BasePage
from common.file_handler import FileHandler


class FundInfo(BasePage):
    # 基金详情页
    def add_collect(self):
        # 点击收藏
        self.steps(os.path.join(FileHandler.locator_path, 'fund.yaml'))
        return FundInfo(self._driver)

    def click_fixed_invest_button(self):
        self.steps(os.path.join(FileHandler.locator_path, 'fund.yaml'))

    def goto_fixed_invest(self):
        # 定投
        pass

    def click_purchase_button(self):
        self.steps(os.path.join(FileHandler.locator_path, 'fund.yaml'))
        return self

    def goto_purchase(self):
        # 购买页
        pass
