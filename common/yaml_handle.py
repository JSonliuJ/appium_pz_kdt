# -- encoding: utf-8 --
# @time:    2020/12/5 14:29
# @Author: jsonLiu
# @Email: 810030709@qq.com
# @file: yamlhandler.py
import yaml
from yaml import FullLoader


class YamlHandler:
    def __init__(self, file):
        self.file = file

    def read_yaml(self, encoding='utf8'):
        with open(self.file, mode='r', encoding=encoding) as f:
            # TODO: f.read() 和 f 都可以作为参数
            # data = yaml.load(f.read(), Loader=FullLoader)
            data = yaml.safe_load(f.read())
        f.close()
        return data

    def write_yaml(self, data, encoding='utf-8'):
        with open(self.file, mode='w', encoding=encoding) as f:
            # return yaml.dump(data, stream=f, allow_unicode=True)
            return yaml.safe_dump(data, stream=f, allow_unicode=True)


if __name__ == '__main__':
    import os
    from common.file_handler import FileHandler

    test_search_path = os.path.join(FileHandler.locator_path, 'fund_position.yaml')

    data = YamlHandler(test_search_path).read_yaml()['confirm_pay_and_input_pwd'][5]
    print(data['value'])
    print(type(data['value']))

