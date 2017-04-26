#!/usr/bin/env python
# -*- coding: utf-8 -*-

def yieldReturn():
	# r = range(10)
	for x in xrange(1,10):
		yield x*x

# when you call the function, the code you have written in the function body does not run. 
# print yieldReturn()

# for j in yieldReturn():
# 	print j


class WithClass(object):
	"""docstring for WithClass"""
	def __init__(self):
		super(WithClass, self).__init__()
		self.arg = xrange(10)

	def __enter__(self):
		for x in self.arg:
			yield x
		# return range(3)
		
	def __exit__(self, exctype, excvalue, traceback):
		print 'this is end'
		# print self.arg

with WithClass() as w:
	for x in w:
		print x