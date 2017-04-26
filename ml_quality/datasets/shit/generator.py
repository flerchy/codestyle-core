#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 在Python中，这种一边循环一边计算的机制，称为生成器（Generator）。
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
g = (x*x for x in range(1,11))
# for x in g:
# 	print x

def fab(max):
	i, a ,b = 0,0,1
	while i<max:
		yield b
		a, b = b, a+b
		i = i+1

# print fab(6)
# <generator object fab at 0xb7704a7c>

for x in fab(6):
	print x

# 这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def testyield():
	print "test 1"
	yield 1
	print 'test 2'
	yield 2
	print 'test 3'
	yield 3

o = testyield()
o.next()
o.next()
o.next()
o.next()