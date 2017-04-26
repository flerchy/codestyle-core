#!/usr/bin/env python
# -*- coding: utf-8 -*-

def bs(arr, key, start, end):
    if end < start:
        return -1
    m = (start + end) / 2
    # print m
    if key == arr[m]:
        return m
    elif key < arr[m]:
        # search left
        return bs(arr, key, start, m - 1)
    else:
        # search right
        return bs(arr, key, m + 1, end)


def bs2(arr, target):
    l = len(arr)
    start, end = 0, l - 1
    while start <= end:
        mid = start + (end - start) / 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end -= 1
        else:
            start += 1
    return -1


if __name__ == '__main__':
    index = bs([1, 2, 2.4, 3, 4], 2.5, 0, 3)
    print index
    index = bs2([1, 3, 5, 7], 5)
    print index
    index = bs2([1, 3, 5, 7], 8)
    print index

