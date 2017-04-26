#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import sys


def getGCD(m, n):
    # print m,n
    while n != 0:
        r = m % n
        m = n
        n = r
    return m


def getGCD2(m, n):
    # print m,n
    t = min(m, n)
    while t > 1:
        if m % t == 0 and n % t == 0:
            return t
        else:
            t -= 1
    return 1

# print getGCD(100, 30)
# print "please input m, n"
while True:
    m = input("please input m : ")
    n = input("please input n : ")
    if n == 0:
        break
    print getGCD2(m, n)
