#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
dic = [(),(15, 1), (10, 5), (9, 3), (5, 4)]


def get_most_val():
    lst = []
    backtrack(lst, [], 1)
    # print lst
    max_val = 0
    for arr in lst:
        val = 0
        weight = 0
        for e in arr:
            val += dic[e][0]
            weight += dic[e][1]
        print arr,
        print val,
        print weight


def backtrack(lst, tmplist, start):
    if len(tmplist) == 4:
        lst.append(copy.deepcopy(tmplist))
    else:
        for x in xrange(start, 5):
            tmplist.append(x)
            backtrack(lst, tmplist, x)
            tmplist.pop()

get_most_val()
