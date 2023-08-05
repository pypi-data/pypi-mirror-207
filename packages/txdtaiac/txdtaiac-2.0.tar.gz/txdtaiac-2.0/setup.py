# -*- coding: utf-8 -*-
# @File  : setup.py.py
# @Time  : 2023/5/6 11:39
# @Author: 唐旭东

from distutils.core import  setup

packages = ['txdtaiac']# 唯一的包名

setup(name='txdtaiac',
    version='2.0',
    author='唐旭东',
    packages=packages,
    package_dir={'requests': 'requests'})