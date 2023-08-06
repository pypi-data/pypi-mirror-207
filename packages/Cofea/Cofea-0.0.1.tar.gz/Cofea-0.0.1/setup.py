#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages            #这个包没有的可以pip一下

setup(
    name = "Cofea",      #这里是pip项目发布的名称
    version = "0.0.1",  #版本号，数值大的会优先被pip
    keywords = ["pip", "Cofea"],			# 关键字
    description = "",	# 描述
    long_description = "",
    license = "MIT Licence",		# 许可证

    url = "https://github.com/likeyi19/Cofea",     #项目相关文件地址，一般是github项目地址即可
    author = "Keyi Li",			# 作者
    author_email = "931818472@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["numpy", "scanpy","anndata","skit-learn","seaborn","pandas"]          #这个项目依赖的第三方库
)
