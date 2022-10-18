# -- encoding: utf-8 --
# @time:    	2022/1/25 20:57
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com

import os
import sys
from common.app import APP
rootpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(rootpath)

class TestBase:
    app = APP()

    def app_back(self):
        self.app.back()

    def app_quit(self):
        self.app.stop()
