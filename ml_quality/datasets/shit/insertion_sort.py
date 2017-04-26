#!/usr/bin/env python
# -*- coding: utf-8 -*-


def insertion_sort(a):
    l = len(a)
    for i in xrange(0, l - 1):
        print "i is :: " + str(i)
        for j in xrange(i + 1, 0, -1):
            # print "j is :: " + str(j)
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
            else:
            	break
        print a
    print a

if __name__ == '__main__':
    insertion_sort([7,6,3,1,8,5])
