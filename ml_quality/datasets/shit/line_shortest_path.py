#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Pair(object):

    def __init__(self, data, p1, p2):
        super(Pair, self).__init__()
        self.data = data
        self.p1 = p1
        self.p2 = p2


def Partition(s, x, l, r):
    i, j = l, r
    while True:
        if s[i] < x and i < r:
            i += 1
        if s[j] > x and j > l:
            j -= 1
        if j <= i:
            break
        s[i], s[j] = s[j], s[i]
    return j


def CPair(s, l, r):
    if r - l < 1:
        return Pair(99999, 0, 0)
    m1, m2 = max(s[l:r + 1]), min(s[l:r + 1])
    m = (m1 + m2) / 2
    j = Partition(s, m, l, r)
    d1 = CPair(s, l, j)
    d2 = CPair(s, j + 1, r)
    p, q = max(s[l:j + 1]), min(s[j + 1:r + 1])
    min_d, min_v = d1, d1.data
    if d2.data < d1.data:
        min_d, min_v = d2, d2.data
    if q - p < min_v:
        return Pair(q - p, p, q)
    return min_d


if __name__ == '__main__':
    s = [20.5, 3.7, 2.5, 30, 31]
    d = CPair(s, 0, 4)
    print d.data
    print d.p1
    print d.p2
