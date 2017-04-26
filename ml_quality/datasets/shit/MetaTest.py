#!/usr/bin/python
# -*- coding: utf-8 -*-


class ListMetaclass(type):

    def __new__(cls, name, bases, attrs):

        # print name
        # print cls
        # print bases
        print attrs

        def add(self, value):
            self.append(value)

        attrs['add'] = add

        def getfirst(self):
            return self[0]

        attrs['getfirst'] = getfirst

        return type.__new__(cls, name, bases, attrs)


class MyList(list):

    """一个关于Meta的测试"""

    __metaclass__ = ListMetaclass  # 指示使用ListMetaclass来定制类

    # def __init__(self, arg):
    # self.arg = arg

# test

l = MyList()
l.add(3)
l.add(4)
print l.getfirst()
print l
print l.__dict__
print dir(l)

# print dir(MyList)

# print MyList.__class__
# print MyList.__doc__
# print MyList.__metaclass__
