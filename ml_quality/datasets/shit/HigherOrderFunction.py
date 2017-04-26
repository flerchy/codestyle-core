#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1.高阶函数


def quert(x):
    return x * x

print quert(3)
# 像map()函数这种能够接收函数作为参数的函数，称之为高阶函数（Higher-order function）
# like java, map(interface, data)
print map(quert, [4, 5, 36])

# 但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场


def mult(x, y):
    return x * 10 + y

print reduce(mult, [1, 3, 5, 7, 9])


# 我们可以看出，map是把一个数组变化为另外一个数组
# reduce则是把数组变化为一个值，相当与调用了n次函数
def str2int(ss):
    return reduce(lambda x, y: x * 10 + y, map(int, ss))

print str2int("555333")

# sorted()函数也是一个高阶函数，它还可以接收一个比较函数来实现自定义的排序。
# 比如，如果要倒序排序，我们就可以自定义一个reversed_cmp函数

print('#############################sorted 高阶函数##########################################3');
def reversed_cmp(x, y):
    if x < y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

print sorted([3, 6, 7, 9, 10], reversed_cmp)

# 2.函数作为返回值


def lazy_sum(*args):
    def add():
        sum = 0
        for x in args:
            sum = sum + x
        return sum
    return add

ls = lazy_sum(3, 4, 15)
print ls
print ls()

ff = lambda x: x + x
print ff(3)
