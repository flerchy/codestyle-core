#!/usr/bin/env python
# -*- coding: utf-8 -*-

# dict就可以迭代
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for key in d:
    print key, d[key]
    # print d[key]
# for value in d:
    # print value
# for value in d.itervalues()
# for k, v in d.iteritems()。
for k, v in d.iteritems():
    print k, "----", v

# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
from collections import Iterable
print isinstance([1, 2, 3], Iterable)
print isinstance(123, Iterable)

# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
    print i, value
