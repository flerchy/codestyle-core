#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys  # 模块，sys指向这个模块对象
import inspect


def foo():
    pass  # 函数，foo指向这个函数对象


class Cat(object):  # 类，Cat指向这个类对象

    def __init__(self, name='kitty'):
        self.name = name

    def sayHi(self):  # 实例方法，sayHi指向这个方法对象，使用类或实例.sayHi访问
        print self.name, 'says Hi!'  # 访问名为name的字段，使用实例.name访问

cat = Cat()  # cat是Cat类的实例对象

print Cat.sayHi  # 使用类名访问实例方法时，方法是未绑定的(unbound)
print cat.sayHi  # 使用实例访问实例方法时，方法是绑定的(bound)
# Cat.sayHi()
cat.sayHi()

def useReflect():
    cat = Cat()
    print "*** all the properties of cat ***"
    print dir(cat)

# ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'sayHi']

    if hasattr(cat, "name"):
        print "cat has attr name"
        setattr(cat, "name", "Tom")
    else:
        print "cat does not has attr name"
    
    print getattr(cat, "name", "kitty")

if __name__ == '__main__':
    useReflect()

import fnmatch as m
print m.__doc__.splitlines()[0] # Filename matching with shell patterns.
print m.__name__                # fnmatch
print m.__file__                # /usr/lib/python2.6/fnmatch.pyc
print m.__dict__.items()[0]     # ('fnmatchcase', <function>)</function>

import gqq
print gqq.__file__
from gqq import decode
# print decode("www.baidu.com")
# print decode.__file__

print Cat.__doc__           # None
print Cat.__name__          # Cat
print Cat.__module__        # __main__
print Cat.__bases__         # (<type>,)
print Cat.__dict__          # {'__module__': '__main__', ...}</type>

im = cat.sayHi
print im.im_func
print im.im_self # cat
print im.im_class # Cat