#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = range(1, 11)
print x

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
y = [z * z for z in x if z % 2 == 0]
print y

# 奇数的平方
y2 = [z * z for z in x if z % 2 == 1]
print y2

# 还可以使用两层循环，可以生成全排列：
z = [x + y for x in 'abc' for y in 'xyz']
print z

# 最后把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
# operation before loop and filter after loop.
l = [x.lower() for x in L]
print l

# 廖雪松布置的作业
# isinstance(321,str) false 判断是否为字符串
L = ['Hello', 'World', 'Just a TEST', 18, 32, 'Apple', None]
l = [x.lower() for x in L if isinstance(x, str)]
print l
# filter int value.
print(
    '############################################filter int value########################################')
intValue = [x for x in L if isinstance(x, int)]
print intValue
