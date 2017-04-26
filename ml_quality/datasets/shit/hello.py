#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；
' a test module '

__author__ = 'GQQ'

import sys


def test():
    # sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：
    # 运行python hello.py获得的sys.argv就是['hello.py']；
    # 运行python hello.py Michael获得的sys.argv就是['hello.py', 'Michael]。
    args = sys.argv
    print 'sys.argv length is ' + str(len(args))
    if len(args) == 1:
        print 'Hello,' + args[0]
    elif len(args) == 2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'
# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该hello模块时，if判断将失败，
print "__name__ is " + __name__
if __name__ == '__main__':
    test()
