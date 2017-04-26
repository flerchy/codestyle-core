#!/usr/bin/env python
# -*- coding: utf-8 -*-


def factorial(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    res = [1]
    for i in xrange(1, n + 1):
        res.append(res[i - 1] * i)
    return res[n]

if __name__ == '__main__':
    m = input("please input a number : ")
    fac = factorial(m)
    print "the factorial of {0} is {1}".format(m, fac)
