#!/usr/bin/env python
# -*- coding: utf-8 -*-

from student import student
from types import MethodType

# 根据开比原则，不要随意更改一个类的内容
def set_age(self, age):
	self.real_age = age

stu=student('Zhangsan', 20)
stu2=student('Lisi', 25)

print stu.get_age()
print stu.get_name()

# 1.方法的动态绑定
stu.set_age = MethodType(set_age, stu, student)
stu.set_age(32)
# print stu.__dict__
print stu.get_age()
print stu.real_age

# 'student' object has no attribute 'set_age'
# 2.但是，给一个实例绑定的方法，对另一个实例是不起作用的：
# stu2.set_age(33)

# 3.为了给所有实例都绑定方法，可以给class绑定方法
student.set_age = MethodType(set_age, None, student)
stu2.set_age(22)

print stu2.__dict__
print stu2.real_age

# 4.测试property的用法
stu.score = 98
print stu.score

stu.score = 'aaa'