#!/usr/bin/env python
# -*- coding: utf-8 -*-


def yield_1():
    for x in xrange(1, 10):
        print 'before yield'
        yield x
        print 'after yield'


def hold_client(name):
    yield 'Hello, %s! You will be connected soon' % name
    yield 'Dear %s, could you please wait a bit.' % name
    yield 'Sorry %s, we will play a nice music for you!' % name
    yield '%s, your call is extremely important to us!' % name


def fibonacci(n):
    curr = 1
    prev = 0
    counter = 0
    while counter < n:
        yield curr
        prev, curr = curr, prev + curr
        counter += 1

if __name__ == '__main__':
    print '*********** test yield1******************'
    y1 = yield_1()
    print type(y1)
    print y1.next()
    print 'call y1.next() first'
    for x in y1:
        print x
    # if we call y1.next() again, their will be an exception
    # print y1.next()
    print '***************test hold_client***************'
    hc = hold_client('Peter')
    print hc.next()
    print hc.next()
    print hc.next()
    print hc.next()
    # observously, the last next() function is error. Because the loop has limited.
    # print hc.next()
    print '***************test hold_client***************'
    n = 40
    fib = fibonacci(n)
    for x in xrange(1, n + 1):
        print 'fib({0}) is {1}'.format(x, fib.next())
