# -- encoding: utf-8 --
# @time:    	2022/1/25 20:57
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com

import os
from common.base_page import BasePage
from common.file_handler import FileHandler
from page.subpage.progenypage.fund_info import FundInfo
from page.subpage.progenypage.stock_info import StockInfo


class Synthesis(BasePage):

    def click_fund_or_stock_info_button(self, property_name, instance_index):
        # 点击股票或基金按钮
        self._test_params['property_name'] = property_name
        self._test_params['instance_index'] = instance_index
        self.steps(os.path.join(FileHandler.locator_path, 'search.yaml'))

    def goto_fund_info(self) -> FundInfo:
        # 跳转到基金详情页
        return FundInfo(self._driver)

    def goto_stock_info(self) -> StockInfo:
        # 跳转到股票详情页
        return StockInfo(self._driver)

    def add_to_optional(self, property_name):
        # 添加自选
        from appium.webdriver.common.mobileby import MobileBy
        # self.find_ele(MobileBy.XPATH, '//*[@resource-id="com.hundsun.winner.pazq:id/tvOnSearch"]').click()
        # self.find_ele(MobileBy.XPATH, '//*[@resource-id="com.hundsun.winner.pazq:id/search_home_clear_iv"]').click()
        # search_input = self.find_ele(MobileBy.XPATH,
        #                              '//*[@resource-id="com.hundsun.winner.pazq:id/edit_search"]').clear()
        # print(search_input)
        # search_input.send_keys('诺安货币')
        # self.find_ele(MobileBy.XPATH,'//*[contains(@resource-id,"wrap_rv")]//*[@text="诺安货币B"]/../..//android.view.ViewGroup[contains(@index,0)]').click()
        # self.find_ele(MobileBy.XPATH,'//android.view.ViewGroup[contains(@index,1)]').click()

        # self.find_ele(MobileBy.XPATH,'//*[contains(@resource-id,"wrap_rv")]//*[@text="天弘永利债券A"]/../..//*[@resource-id="com.hundsun.winner.pazq:id/iv_item_addFund"]').click()
        # self.find_ele(MobileBy.XPATH,'//*[contains(@resource-id,"code_fund")]/../..//*[@text ="天弘永利债券B"]')
        # ele = self.find_ele(MobileBy.XPATH, "//*[contains(@text,'已添加到自选-我的基金')]")
        # print(ele.text)

        self._test_params['property_name'] = property_name
        self.steps(os.path.join(FileHandler.locator_path, 'search.yaml'))

    def is_and_optional_successful(self):
        text = self.steps(os.path.join(FileHandler.locator_path, 'search.yaml'))
        return text
