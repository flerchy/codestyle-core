#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 定义一个递归函数
def f(n):
	if 1==n:
		return 1
	else:
		return f(n-1)*n

# 求一个斐波拉契数列吧
def fib(n):
	if 1==n or 0==n:
		return 1
	else:
		return fib(n-1)+fib(n-2)


print "fib:", fib(5)
print f(3)

print "my python is lucky"
