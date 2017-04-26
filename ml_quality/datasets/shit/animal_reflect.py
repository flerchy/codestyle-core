#!/usr/bin/env python
# -*- coding: utf-8 -*-
import types


class Animal(object):

    def __init__(self, age=9):
        self.age = age
        print "Animal constructor is called"

    def run(self):
        print 'Animal is running...'

    def __old__(self):
        return self.age

    def  __len__(self):
    	return 100


class Dog(Animal):

    def __init__(self, age=10):
        super(Dog, self).__init__(age)
        print "Dog constructor is called"

    def run(self):
        super(Dog, self).run()
        print 'Dog is running...'


def testPolymorphism(a):
    a.run()

a = Animal()
a.run()

d = Dog(110)
d.run()
print len(d)
print d.__old__()
# print old(d)
print type(123)
print type('str')
print type(123).__name__
print type(d)
print type(d).__name__
print types.StringType
print types.StringType == type("str")
print type(u'abc')==types.UnicodeType
print type([])==types.ListType
print type(str)==types.TypeType
print type(int)==type(str)==types.TypeType

print isinstance(a, Animal)
print isinstance(a, Dog)
print isinstance(d, Animal)
print isinstance(d, Dog)

print dir(d)
# print d.__new__()
print hasattr(d, 'age')
print hasattr(d, 'age1')
print getattr(d, 'age')
# AttributeError: 'Dog' object has no attribute 'age1'
# print getattr(d, 'age1')
print getattr(d, 'age1', 10)
print hasattr(d, 'run')
run = getattr(d, 'run')
print run
print dir(run)
print run.__class__.__name__
run()

print '***** test Polymorphism *****'
testPolymorphism(d)
