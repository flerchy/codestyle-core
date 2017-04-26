#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MyArray(object):
	"""docstring for MyArray"""
	def __init__(self, arg):
		self.index =0
		self.array = arg
		self.length = len(arg)

	def  __str__(self):
		# return str(reduce(lambda x,y:x+y, self.array))
		# return ','.join(map(lambda x:str(x), self.array))
		return ','.join(str(x) for x in self.array)
	# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
	# 然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
	def __iter__(self):
		return self # 实例本身就是迭代对象，故返回自己


	def next(self):
		result =0
		if(self.index<self.length):
			result=self.array[self.index]
			self.index=self.index+1
		else:
			result =0
			raise StopIteration();
		return result

	# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
	def __getitem__(self, n):
		if isinstance(n, int):
			return self.array[n]
		elif isinstance(n, slice):
			print 'n is slice'
			print n
			start = n.start
			stop=n.stop
			# print n.indices
			# print n.step
			# print dir(n)
			return self.array[start:stop:n.step]

	def __setitem__(self, n, value):
		self.array[n] = value

	def __call__(self):
		return ';'.join([str(x) for x in self.array])
	
	def sum2(self):
		return reduce(lambda x,y:x+y, self.array)

testArr = MyArray([3,4,6,7,12,31])

# print map(lambda x:x+2, testArr.array)
# print testArr.array
print testArr

# 由于__iter__，所以可以使用for in __iter__
# for x in testArr:
	# print x
print [x*x*x for x in testArr]

print testArr[::2]

testArr[3] = 5
print testArr

print callable(testArr)
print testArr()
print testArr.sum2()