#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 取前N个元素，也就是索引为0-(N-1)的元素，可以用循环
# 特别注意的是，在语句的前面不能有空格，否则，就会报“安装错误”
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r = []
n = 3
for i in range(3):
    r.append(L[i])
print r
print L[0:4]
# 既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
# 字符串'xxx'或Unicode字符串u'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串

# test slice
for x in L[3:  5]:
    print x
