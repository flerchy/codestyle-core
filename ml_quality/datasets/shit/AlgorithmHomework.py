#!/usr/bin/env python
import math
import random

dic = (0, 3, 6, 9)


def divisible_by_two(num):
    # if its binary string ending with 0. num can be divisible by 2.
    bnum = bin(num)
    return True if bnum[-1] == '0' else False


def divisible_by_three(num):
    # Given a binary number, the sum of its odd bits minus the sum of its even bits is divisible
    # by 3 iff the original number was divisible by 3.
    while num > 9:
        bnum = list(bin(num))[2:]
        num = abs(sum(int(i) for i in bnum[::2]) - sum(int(i) for i in bnum[1::2]))
    return True if num in dic else False


def divisible_by_five(num):
    # the num end with 0 or 5
    return True if str(num)[-1] in ('0', '5') else False


def display_numbers(num):
    ret = []
    while num > 1 and divisible_by_five(num):
        num /= 5
        ret.append(5)
    while num > 1 and divisible_by_three(num):
        num /= 3
        ret.append(3)
    while num > 1 and divisible_by_two(num):
        num /= 2
        ret.append(2)
    return None if len(ret) == 0 else '*'.join(str(x) for x in ret) + "*" + str(num)


if __name__ == '__main__':

    values = [random.randint(10000, 27000) for i in range(10)]
    print 'random values are:'
    print values
    for value in values:
        print '{0} : {1}'.format(value, display_numbers(value))
