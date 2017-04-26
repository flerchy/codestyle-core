#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import random


class Answer(object):

    def __init__(self):
        super(Answer, self).__init__()
        self.Point1 = None
        self.Point2 = None
        self.min_dis = 99999


class Point(object):
    global sort_by

    def __init__(self, x, y):
        super(Point, self).__init__()
        self.id = 0
        self.x = x
        self.y = y
        self.x_order = 0

    def __str__(self):
        return '({0},{1}) {2}'.format(self.x, self.y, self.x_order)

    __repr__ = __str__

    def __cmp__(self, other):
        if Point.sort_by == "x":
            if self.x < other.x:
                return -1
            elif self.x == other.x:
                return 0
            else:
                return 1
        else:
            if self.y < other.y:
                return -1
            elif self.y == other.y:
                return 0
            else:
                return 1

    @staticmethod
    def dis(u, v):
        dx = u.x - v.x
        dy = u.y - v.y
        return math.sqrt(dx * dx + dy * dy)


def sort_by_X(s):
    # sort list by X
    Point.sort_by = "x"
    return sorted(s)


def sort_by_Y(s):
    # sort list by Y
    Point.sort_by = "y"
    return sorted(s)


def closest(xsorted_s, ysorted_s, z_s, l, r, ans):
    # if only two points
    if r - l == 1:
        ans.Point1 = xsorted_s[l]
        ans.Point2 = xsorted_s[r]
        ans.min_dis = Point.dis(ans.Point1, ans.Point2)
        return

    if r - l == 2:
        d1 = Point.dis(xsorted_s[l], xsorted_s[l + 1])
        d2 = Point.dis(xsorted_s[r], xsorted_s[l + 1])
        d3 = Point.dis(xsorted_s[r], xsorted_s[l])
        if d1 <= d2 and d1 <= d3:
            ans.min_dis = d1
            ans.Point1 = xsorted_s[l]
            ans.Point2 = xsorted_s[l + 1]
        elif d2 <= d3:
            ans.min_dis = d2
            ans.Point1 = xsorted_s[l + 1]
            ans.Point2 = xsorted_s[r]
        else:
            ans.min_dis = d3
            ans.Point1 = xsorted_s[r]
            ans.Point2 = xsorted_s[l]
        return

    m = (l + r) / 2
    f, g = l, m + 1
    for i in range(l, r + 1):
        if ysorted_s[i].x_order > m:
            z_s[g] = ysorted_s[i]
            g += 1
        else:
            z_s[f] = ysorted_s[i]
            f += 1

    ans1 = Answer()
    closest(xsorted_s, z_s, ysorted_s, l, m, ans1)
    ans2 = Answer()
    closest(xsorted_s, z_s, ysorted_s, m + 1, r, ans2)
    if ans1.min_dis <= ans2.min_dis:
        ans.Point1 = ans1.Point1
        ans.Point2 = ans1.Point2
        ans.min_dis = ans1.min_dis
    else:
        ans.Point1 = ans2.Point1
        ans.Point2 = ans2.Point2
        ans.min_dis = ans2.min_dis

    ysorted_s = sort_by_Y(ysorted_s)
    k = l
    for i in range(l, r + 1):
        if math.fabs(xsorted_s[m].x - ysorted_s[i].x) < ans.min_dis:
            z_s[k] = ysorted_s[i]
            k += 1

    for i in range(l, k):
        for j in range(i + 1, k):
            if z_s[j].y - z_s[i].y >= ans.min_dis:
                break
            dp = Point.dis(z_s[i], z_s[j])
            if (dp < ans.min_dis):
                ans.min_dis = dp
                ans.Point1 = xsorted_s[z_s[i].x_order]
                ans.Point2 = xsorted_s[z_s[j].x_order]


def random_point():
    x = random.uniform(-100, 100)
    x = float(format(x, ".2f"))
    y = random.uniform(-100, 100)
    y = float(format(y, ".2f"))
    return Point(x, y)

if __name__ == '__main__':
    xsorted_s = []
    # for x in xrange(0, 20):
    # xsorted_s.append(random_point(x))
    xsorted_s.append(Point(-59.02, -66.57))
    xsorted_s.append(Point(-90.6, 1.63))
    xsorted_s.append(Point(-1.16, -95.22))
    xsorted_s.append(Point(-12.13, 16.23))
    xsorted_s.append(Point(93.33, 85.58))
    xsorted_s.append(Point(10.7, 35.56))
    xsorted_s.append(Point(-36.45, 88.11))
    xsorted_s.append(Point(29.93, -46.92))
    xsorted_s.append(Point(-53.77, 77.03))
    xsorted_s.append(Point(78.05, 18.89))
    xsorted_s.append(Point(61.9, 93.39))
    xsorted_s.append(Point(-99.05, -26.7))
    xsorted_s.append(Point(-22.95, -74.18))
    xsorted_s.append(Point(-85.92, -30.86))
    xsorted_s.append(Point(-12.52, -23.94))
    xsorted_s.append(Point(9.81, 98.41))
    xsorted_s.append(Point(-34.45, -55.87))
    xsorted_s.append(Point(37.94, -46.34))
    xsorted_s.append(Point(-40.9, -25.26))
    xsorted_s.append(Point(-47.38, 69.44))

    xsorted_s = sort_by_X(xsorted_s)

    for x in xrange(0, len(xsorted_s)):
        xsorted_s[x].x_order = x

    print 'The random Points are [',
    for x in xrange(0, 20):
        print xsorted_s[x],
    print ']'

    ysorted_s = sort_by_Y(xsorted_s)

    print 'The y random Points are [',
    for x in xrange(0, 20):
        print ysorted_s[x],
    print ']'

    ans = Answer()
    z_s = [None] * len(ysorted_s)
    closest(xsorted_s, ysorted_s, z_s, 0, 19, ans)
    print '\nthe final result is:'
    print ans.Point1
    print ans.Point2
    print ans.min_dis
