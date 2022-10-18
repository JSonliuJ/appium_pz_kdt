# -- encoding: utf-8 --
# @time:    	2022/1/25 20:57
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com

import shlex
import signal
import subprocess
import os
import pytest
from common.app import APP
FH = FileHandler()
test_login_file = os.path.join(FH.locator_path, 'test_login.yaml')
test_params = YamlHandler(test_login_file).read_yaml()

@pytest.fixture(scope='class', autouse=True)
def video_screen():
    cmd = shlex.split("scrcpy --record file.mp4")
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    yield
    os.kill(p.pid, signal.CTRL_C_EVENT)

@pytest.mark.parametrize('property_name', test_params)
@pytest.fixture()
def login():
    """下单夹具. 浏览器，  po 模式当中 login"""
    # TODO: 配置文件
    self.app = APP()
    self.login = self.app.start().main().goto_login().user_pwd_login(property_name)
    return self.app