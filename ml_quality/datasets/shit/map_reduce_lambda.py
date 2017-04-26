#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The first argument func is the name of a function
# and the second a sequence (e.g. a list) seq. map() applies the function func to all the elements of the sequence seq.
# It returns a new list with the elements changed by func
print "**************** test map with lambda ************************"
temp = (36.5, 37, 37.5, 39)
Fahrenheit = map(lambda x: (float(9) / 5) * x + 32, temp)
Celsius = map(lambda x: (float(5) / 9) * (x - 32), Fahrenheit)
print Fahrenheit
print Celsius

'''
map() can be applied to more than one list. The lists have to have the same length. map() will apply its lambda function to the elements of the argument lists, i.e. it first applies to the elements with the 0th index, then to the elements with the 1st index until the n-th index is reached:
'''
print "**************** test multiple parameters ************************"
a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]
print map(lambda x, y: x + y, a, b)
# [18, 14, 14, 14]
print map(lambda x, y, z: x + y + z, a, b, c)
# [17, 10, 19, 23]
print map(lambda x, y, z: x + y - z, a, b, c)
# [19, 18, 9, 5]

'''
The function filter(function, list) offers an elegant way to filter out all the elements of a list, for which the function function returns True. 
The function filter(f,l) needs a function f as its first argument. f returns a Boolean value, i.e. either True or False. This function will be applied to every element of the list l. Only if f returns True will the element of the list be included in the result list.
'''
print "**************** test filter ************************"
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
odds = filter(lambda x: x % 2, fib)
evens = filter(lambda x: x % 2 == 0, fib)
print odds, evens

'''
The function reduce(func, seq) continually applies the function func() to the sequence seq. It returns a single value. 

If seq = [ s1, s2, s3, ... , sn ], calling reduce(func, seq) works like this:
At first the first two elements of seq will be applied to func, i.e. func(s1,s2) The list on which reduce() works looks now like this: [ func(s1, s2), s3, ... , sn ]
In the next step func will be applied on the previous result and the third element of the list, i.e. func(func(s1, s2),s3)
The list looks like this now: [ func(func(s1, s2),s3), ... , sn ]
Continue like this until just one element is left and return this element as the result of reduce()
We illustrate this process in the following example:

'''
print "**************** test reduce ************************"

sumArr = reduce(lambda x, y: x + y, [47, 11, 42, 13])
print sumArr
maxValue = reduce(lambda x, y: x if x >= y else y, [47, 111, 42, 13])
print maxValue
sumArray = reduce(lambda x, y: x + y, range(1, 101))
print sumArray