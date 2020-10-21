#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:huangCijin
# datetime:2020/9/20 13:56
# software: PyCharm
import pytest

class Test_hcj:
    def test_001(self):
        assert 1

    def test_002(self):
        assert 1

# if __name__ == '__main__':
#     pytest.main(["-s","-v","--html=reports/pytest.html",
#                  "--alluredir=allure"])   # allure文件生成的目录