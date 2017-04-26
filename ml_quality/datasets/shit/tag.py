#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps

def tags(tag):
    def tag_fun(func):
    	@wraps(func)
        def execm(name):
            # print func.__name__
            return '<{0}>{1}</{0}>'.format(tag, name)
        return execm
    return tag_fun

# def  author(name):
#     def tag_fun(func):
#         @wraps(func)
#         def execm():
#             return '<{0}>{1}</{0}>'.format(tag, name)
#         return execm
#     return tag_fun

# @tags("p")
@tags("strong")
def get_text(name):
    """this is get_text method"""
    return "Hello " + name

print get_text("Peter")

# that is
v1 = tags('strong')
v2 = v1(get_text)
v3 = v2("John")
print v3
print ""

# debug
print get_text.__name__
print get_text.__doc__
print get_text.__module__
