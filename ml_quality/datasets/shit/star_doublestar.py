#!/usr/bin/env python
# -*- coding: utf-8 -*-


def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

    for key, value in kw.iteritems():
        print key, ' [corresponds to] ', value
    # print args[0]
    # print args[1]
    # print kw["name"],  kw["id"]

func(3, 4, 5, 6, 7, name='zhangsan', id='1')

arr = ('a', 'b', 'c')
func(3, 4, 5, *arr, **{'name': 'peter', 'id': 3})


def foo(x, y, z):
    print "x=" + str(x)
    print "y=" + str(y)
    print "z=" + str(z)

print "##################with list#################"
mylist = [1, 2, 3]
foo(*mylist)

print "###################with dicT#################"
mydict = {"x": 4, "y": 5, "z": 6}
foo(**mydict)

print "###################with tuple#################"
foo(*(3, 2, 1))
