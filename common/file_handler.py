# -- encoding: utf-8 --
# @time:    	2021/1/12 23:49
# @Author: 		jsonLiu
# @Email:  		810030709@qq.com
# @file: 		filehandler
import os


class FileHandler:
    # 项目根路径
    base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    config_path = os.path.join(base_path, 'config')

    locator_path = os.path.join(base_path, 'locatordatas')

    testcase_path = os.path.join(base_path, 'testcases')

    log_path = os.path.join(base_path, r'output\log')

    report_path = os.path.join(base_path, r'output\allure_reports')

    screenshot_path = os.path.join(base_path, r'output\screenshot')


if __name__ == '__main__':
    # print(FileHandler.locator_path)
    # print(FileHandler.config_path)
    pass
