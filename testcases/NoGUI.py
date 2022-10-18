# -- encoding: utf-8 --
# @time:    	2022/5/21 2:09
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
#coding=utf-8
from imp import reload

from pyvirtualdisplay import Display
from selenium import webdriver
import time
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

display=Display(visible=False,size=(800,600))
display.start()

# now Firefox will run in a virtual display.
# you will not see the browser.

browser=webdriver.Firefox()
browser.get("http://www.baidu.com")
time.sleep(3)
browser.quit()
display.stop()