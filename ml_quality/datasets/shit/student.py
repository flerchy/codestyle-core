#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Student(object):

    """docstring for Student"""
    # __slots__ = ('attr1', 'attr2', '_Student__name', '_Student__age')

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return 'Student %s is %d years old' % (self.__name, self.__age)

    __repr__ = __str__

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def is_old(self):
        if(self.__age > 35):
            return 'old'
        elif (self.__age < 10):
            return 'young'
        else:
            return 'medium'

    def __len__(self):
        return len(self.__name)

    def hasmethod(self, method):
        if(hasattr(self, method)):
            fn = getattr(self, method)
            fn()
        else:
            return 'no such method'

    @property
    def score(self):
        print 'get score:'
        return self._score

    @score.setter
    def score(self, value):
        print 'set score:', value
        if not isinstance(value, int):
            raise ValueError('成绩必须是整形!')
        if value < 0 or value > 100:
            raise ValueError('成绩必须在0到100之间!')
        self._score = value


print '__name__ is:', __name__
if __name__ == '__main__':
    # test
    stu = Student('Zhangsan', 20)
    # print stu
    stu3 = Student('Zhangsan', 50)
    # stu.score(80)
    print stu
    stu.address = "120 Dixon Landing Rd#"

    print isinstance(stu, Student)
    print isinstance(stu, object)

    print stu.get_age()
    print stu.get_name()
    print stu.address
    # 'Student' object has no attribute 'address'
    # print stu3.address

    # __len__的特殊性
    print len(stu)
    # 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
    print dir(stu)

    print stu.is_old()

    print stu.hasmethod('is_old')

    # 通过反射知道类的信息和对象的dict（可以修改的属性，以dict方式表示）
    print Student.__name__
    print stu._Student__name
    print stu.__dict__

    # 动态创建一个类的对象
    # stu2 = type('student', (object,), dict(__name='aaa', __age=32))
    # print dir(stu2)
    # print type(stu)
    # print type(stu2)
    # print stu2.__name
    # print stu2.__age
