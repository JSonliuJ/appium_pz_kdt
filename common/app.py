# -- encoding: utf-8 --
# @time:    	2022/1/25 20:57
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com

import os
from appium import webdriver
from common.base_page import BasePage
from common.yaml_handle import YamlHandler
from common.file_handler import FileHandler
from page.main import Main
from page.exchange import Exchange
from page.optional import Optional
from page.financial_management import FinancialManagement
from page.my import MY

config_file = os.path.join(FileHandler.config_path, 'config.yaml')


class APP(BasePage):
    _app_package = ""
    _app_activity = ""

    def start(self):
        if self._driver is None:
            # caps = {
            #     "platformName": "Android",  # 平台名称：ios、Android
            #     "platformVersion": "7.1.2",  # 平台版本
            #     "deviceName": "emulator-5554",  # 设备名称，可不填
            #     # "appPackage": "com.hundsun.winner.pazq",  # 包名
            #     "appPackage": "%s" % self._app_package,  # 包名
            #     # "appActivity": "com.hundsun.winner.pazqapp.ui.home.activity.NewSplashActivity",  # 启动入口页面
            #     "appActivity": "%s" % self._app_activity,
            #     "noRest": True,  # 是否在测试前后重置相关环境，默认False
            #     # "skipServerInstallation": True  # 跳过安装、权限设置等操作
            #     # "skipDeviceInitialization":True
            #     # "unicodeKeyboard": True # 输入中文时设置为True,默认False
            #     # "resetKeyboard":True 是否重置输入法,默认False
            #     # "dontStopAppOnReset": Ture # 首次启动的时候，不停止app ，默认为false
            # }
            self._driver = webdriver.Remote("http://127.0.0.2:4725/wd/hub",YamlHandler(config_file).read_yaml()['app1'])
        else:
            # 二选1
            # self._driver.start_activity(self._app_package,self._app_activity)
            self._driver.launch_app()
        self.set_implicitly_wait(6)
        return self

    def restart(self):
        self._driver.close_app()
        self._driver.launch_app()

    def stop(self):
        self._driver.quit()

    def back(self):
        self._driver.back()

    def main(self) -> Main:
        return Main(self._driver)

    def exchange(self) -> Exchange:
        # 交易页
        return Exchange(self._driver)

    def optional(self) -> Optional:
        # 自选页
        return Optional(self._driver)

    def financial_management(self) -> FinancialManagement:
        return FinancialManagement(self._driver)

    def my(self) -> MY:
        return MY(self._driver)

if __name__ == '__main__':
    app = APP()
    loc = ()
    from appium.webdriver.common.mobileby import MobileBy
    app.start().find_ele(MobileBy.XPATH, '//*[@resource-id="com.hundsun.winner.pazq:id/tvOnSearch"]').click()