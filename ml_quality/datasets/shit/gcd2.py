#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import sys


def getGCD2(m, n):
    # print m,n
    while n != 0:
        r = m % n
        m = n
        n = r
    return m

# print getGCD2(100, 30)
# print "please input m, n"
while True:
    m = input("please input m : ")
    n = input("please input n : ")
    if n == 0:
        break
    print getGCD2(m, n)
