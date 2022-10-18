# -- encoding: utf-8 --
# @time:    	2022/1/25 20:57
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import os
import time
from common.app import APP
from appium.webdriver.common.mobileby import MobileBy


class TestPAZQLogin:
    """以平安证券划屏为例"""

    def __init__(self):
        self.app = APP()
        self.option = self.app.start().optional().goto_option()
        self.option.click_optional_button()
        self.fund_position = self.option.goto_fund().goto_fund_position()

    def login_pz(self):
        pass

    # def swipe_screen(self, times):
    #     # 滑动四次进入"立即开启"按钮页面
    #     for i in range(1, times + 1):
    #         iphone_size = self.main.get_window_size()
    #         start_x = iphone_size['width'] * 0.9
    #         end_x = iphone_size['width'] * 0.1
    #         start_y = iphone_size['height'] * 0.5
    #         i += 1
    #         self.main.swipe(start_x, start_y, end_x, start_y, 200)
    #         time.sleep(2)
    #     # 点击首页”立即体验“按钮
    #     self.main.find_ele(MobileBy.CLASS_NAME, 'android.widget.ImageView').click()
    #
    # def element_find(self):
    #     locator = (MobileBy.XPATH, "//*[@text='普通交易']")
    #     self.exchange.find_ele(locator).click()
    #     locator2 = (MobileBy.XPATH, "//*[@text='买入卖出']")
    #     self.main.find_ele(locator2).click()

    def fund_manage(self):
            # locator = (MobileBy.XPATH, '//*[@resource-id="com.hundsun.winner.pazq:id/scroll_listview"]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]')
            locator_1 = (MobileBy.XPATH,'//*[contains(@resource-id,"myfund_name_text_view") and @text="富国可转债A"]/../..//android.widget.LinearLayout[1]')
            locator_2 = (MobileBy.XPATH,'//*[@content-desc="继续购买"]')
            locator_3 = (MobileBy.XPATH,'//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ListView[2]/android.view.View[2]/android.widget.TextView[2]')
            # locator_4 = (MobileBy.XPATH,'//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ListView[3]/android.view.View[1]/android.view.View[2]/android.view.View[1]')
            self.fund_position.find_ele(locator_1).click()
            time.sleep(5)
            self.fund_position.find_ele(locator_2).click()
            time.sleep(10)
            self.fund_position.find_ele(locator_3).click()

            locator_4 = (MobileBy.XPATH,'//*[@resource-id="app"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.ListView[1]/android.view.View[2]')
            self.fund_position.find_ele(locator_4).click()

            locator_5 = (MobileBy.XPATH,'//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ListView[3]/android.view.View[1]/android.view.View[2]/android.view.View[1]')
            self.fund_position.find_ele(locator_5).click()
            # self.fund_position.tap([(350, 720),])
            self.fund_position.find_ele((MobileBy.XPATH,'//*[contains(@resource-id,"_secukeyboard")]/android.view.View[2]//*[@text="1"]')).click()
            # self.fund_position.find_ele((MobileBy.XPATH,'//*[contains(@resource-id,"_secukeyboard")]/android.view.View[2]/android.widget.TextView[1]')).click()
            self.fund_position.find_ele((MobileBy.XPATH, '//android.widget.TextView[@text="完成"]')).click()
            self.fund_position.find_ele((MobileBy.XPATH,'//*[@content-desc="支付"]')).click()
            time.sleep(15)
            self.fund_position.tap([(521,1216)])
            self.fund_position.find_ele(MobileBy.XPATH,'//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.TextView[1]').click()
            self.fund_position.tap([(521, 1216)])
            # self.fund_position.find_ele(MobileBy.XPATH,'//android.view.View[@content-desc="已全部阅读并确认"]').click()
            # self.fund_position.tap([(475, 1200)])
            # self.fund_position.tap([(521, 1216)])
            self.fund_position.swipe_screen('已全部阅读并确认')
            self.fund_position.tap([(521, 1216)])
            # self.fund_position.find_ele(MobileBy.XPATH,'//*[@resource-id="_fund_detail"]/android.view.View[2]/android.view.View[2]').click()
            # self.fund_position.find_ele(MobileBy.XPATH,'//*[@text="已全部阅读并确认"]/..//android.view.View[1]')
if __name__ == '__main__':
    LG = TestPAZQLogin()
    LG.fund_manage()
