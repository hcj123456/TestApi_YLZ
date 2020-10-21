#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:huangCijin
# datetime:2020/9/21 10:48
# software: PyCharm
import pytest

class Test_HCJ:
    def test_001(self):
        assert 1

    def test_002(self):
        assert 1

# if __name__ == '__main__':
#     pytest.main(["-s","-v","--html=reports/pytest.html",
#                  "--alluredir=allure"])