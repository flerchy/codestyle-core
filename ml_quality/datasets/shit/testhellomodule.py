#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import Python.module.hello

import sys
# 如何在文件夹外部引用一个模块
sys.path.append('module')
import hello

hello.test()