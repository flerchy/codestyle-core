#!/usr/bin/env python
def geometric(a, x, n):
    f, now, i = a, a, 1
    while i <= n:
        now = now * x
        f, i = f + now, i + 1
    g = a / (1 - x)

    print "f is " + str(f) + "\ng is " + str(g)
    print "sub of f and g is " + (str)(f - g)

if __name__ == '__main__':
    a1 = raw_input('please input a, default value is 47 : ')
    x1 = raw_input('please input x, default value is 0.72 : ')
    n1 = raw_input('please input n, default value is 10 : ')

    geometric(a=int(a1) if a1.isdigit() else 47, x=float(x1) if x1.isdigit() else 0.72, n=int(n1) if n1.isdigit() else 10)
