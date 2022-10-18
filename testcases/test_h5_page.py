# -- encoding: utf-8 --
# @time:    	2022/10/17 0:47
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
# 1、导入驱动对象， 和 selenium 差不多
import time

from appium.webdriver import Remote

caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": r"c:\xxxx.apk",
    # 指定h5需要的浏览器驱动，驱动的版本要和手机浏览器匹配
    "chromedriverExecutableDir": r"C:\xxx\chromedriver",
}

# 2、初始化对象
driver = Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities=caps)
driver.implicitly_wait(5)

el = driver.find_element('xpath', '')
el.click()

time.sleep(2)
# 切换
# 是打印所有的上下文 ['NATIVE_APP', 'WEBVIEW_com.lemon.lemonban']
print(driver.contexts)
driver.switch_to.context(driver.contexts[-1])

# 普通的web自动化测试
time.sleep(2)
print(driver.current_url)

time.sleep(3)
driver.quit()