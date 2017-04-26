#!/usr/bin/env python
def add_all(x):
    now = 1
    summ = now
    i = 1
    while i <= 100:
        now = now * x
        summ = summ + now
        i = i + 1
        return summ


def final(x):
    return 1 / (1 - x)

sum1 = add_all(0.3)
sum2 = final(0.3)
print sum1
print sum2
