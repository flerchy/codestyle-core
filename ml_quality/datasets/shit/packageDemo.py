#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1. this is the first method import package.
# from myPackage.classOne import ClassOne
# from myPackage.classTwo import ClassTwo

# 2. this is the second method import package.
# from myPackage import *

# 3. this is third method to import package (must have __init__.py in the package)
import myPackage

print myPackage.__file__

c1 = myPackage.ClassOne()
c2 = myPackage.ClassTwo()

c1.printInfo()
c2.printInfo()
