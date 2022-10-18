# -- encoding: utf-8 --
# @time:    	2022/2/19 15:52
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import os

from common.base_page import BasePage
from common.file_handler import FileHandler
from page.subpage.progenypage.fund import Fund
from appium.webdriver.common.mobileby import MobileBy
from common.yaml_handle import YamlHandler

config_file = os.path.join(FileHandler.config_path, 'config.yaml')


class Option(BasePage):

    def click_optional_button(self):
        self.find_ele(MobileBy.XPATH, YamlHandler(config_file).read_yaml()['main_tab_locator']['optional']).click()
        return Option(self._driver)

    def goto_option(self):
        # 自选
        pass

    def goto_position(self):
        # 持仓
        pass

    def goto_fund(self) -> Fund:
        # 基金
        return Fund(self._driver)
