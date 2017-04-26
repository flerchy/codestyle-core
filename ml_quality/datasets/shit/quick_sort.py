#!/usr/bin/env python
# -*- coding: utf-8 -*-

def partition(arr, start, end):
    if start >= end:
        return

    index = start
    pivot = arr[start]
    arr[index], arr[end] = arr[end], arr[index]
    while start < end:
        if(arr[start] < pivot):
            arr[start], arr[index] = arr[index], arr[start]
            index = index + 1
        start = start + 1

    arr[index], arr[end] = arr[end], arr[index]
    # print arr
    print "index ---- {0}".format(index)
    print "arr ---- {0}\n".format(arr)
    return index


def part2(arr, start, end):
    pivot = arr[start]
    arr[start] = arr[end]
    # end -= 1
    while start < end:
        while start < end and arr[start] <= pivot:
            start += 1
        if start < end:
            arr[end] = arr[start]
            end -= 1
        while start < end and arr[end] >= pivot:
            end -= 1
        if start < end:
            arr[start] = arr[end]
            start += 1
    arr[start] = pivot
    return start


def qs(arr, start, end):
    if start >= end:
        return
    index = part2(arr, start, end)
    qs(arr, start, index - 1)
    qs(arr, index + 1, end)
    # print arr


if __name__ == '__main__':
    # print partition([3, 2, 5, 1], 0, 3)
    a = [6, 7, 32,32, 1, 8, 5]
    qs(a, 0, 6)
    print a
