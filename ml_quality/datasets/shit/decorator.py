#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools

def log(func):
	def  wrapper(*args, **kw):
		print 'call %s():' % func.__name__
		func(*args, **kw)
	return wrapper

def log2(text=None):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			if(text!=None):
				print 'begin %s %s():' % (text, func.__name__)
			else:
				print 'begin operate %s()' % (func.__name__)
			func(*args, **kw)
			if(text!=None):
				print 'end %s %s():' % (text, func.__name__)
			else:
				print 'end operate %s()' % (func.__name__)

		return wrapper
	return decorator

@log2("call")
def now():
	print "2014-07-17"

@log2()
def othermethod():
	print 'othermethod'

now()

othermethod()

# 如果没有functools的导入，那么now的__name__属性会发生变化，因为其原理log(now)
print now.__name__

# 偏函数
def addrank(num, rank = 1):
	return num + rank

print addrank(8)
print addrank(8, 2)

#如何做到连胜三级

# 简单总结functools.partial的作用就是，把一个函数的某些参数（不管有没有默认值）给固定住（也就是设置默认值），
# 返回一个新的函数，调用这个新函数会更简单。
# 注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值：
rank3 = functools.partial(addrank, rank = 3)
print rank3(8)
print rank3(8, rank = 2)