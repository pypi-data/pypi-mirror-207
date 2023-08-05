#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: duanliangcong
# Mail: 137562703@qq.com
# Created Time:  2022-11-02 15:00:00
#############################################

# pip install twine
# python setup.py sdist
# twine upload dist/*

#############################################
#################使用方法#####################
#############################################
'''
目录结构
UPSDIST
    ddreport        库文件夹
    MANIFEST.in     配置
    setup.py        当前文件

1.cmd进入UPSDIST目录
2.执行命令：python setup.py sdist
3.执行命令：twine upload dist/*
'''



#### 每次更新需要修改 version 字段

from setuptools import setup, find_packages, find_namespace_packages

setup(
    name = "ddreport",
    version = "4.0",
    keywords = ("pip", "pytest", "testReport"),
    description = "pytest测试报告",
    long_description = "1.增加正确的请求展示；2.增加用例运行时动态添加用例；3.添加测试报告中展示图片逻辑；4.api请求优化；5.异常信息优化；6.测试报告优化；7.数据对比采用deepdiff库",
    license = "MIT Licence",

    url = "https://gitee.com/duanliangcong/dlc_pytest-report.git",
    author = "duanliangcong",
    author_email = "137562703@qq.com",
    entry_points={"pytest11": ["test_report=ddreport.testReport"]},

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["requests", "jsonpath", "deepdiff"],
)
