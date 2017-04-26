#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ClassOne:

    def __init__(self):
        self.name = "class one"

    def printInfo(self):
        print("i am class One!")

class ClassTwo:

    def __init__(self):
        self.name = "class one"

    def printInfo(self):
        print("i am class Tw0!")

if __name__ == '__main__':
    c1 = ClassOne()
    c1.printInfo()
