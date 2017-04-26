def merge(a, b):
    la = len(a)
    lb = len(b)
    lc = []
    i = 0
    j = 0
    while i < la and j < lb:
        if(a[i] < b[j]):
            lc.append(a[i])
            i = i + 1
        else:
            lc.append(b[j])
            j = j + 1

    while i < la:
        lc.append(a[i])
        i = i + 1
    while j < lb:
        lc.append(b[j])
        j = j + 1
    return lc

# cnt = 0


def merge2(a, b):
    c = []
    while a and b:
        c.append(a.pop() if a[-1] > b[-1] else b.pop())

    while a:
        c.append(a.pop())

    while b:
        c.append(b.pop())
    c.reverse()
    return c


def merge_sort(arr, x):
    tt = ""
    for i in xrange(0, x):
        tt = tt + "    "

    print "{1}now arr is *******************{0}".format(arr, tt)
    l = len(arr)
    if l == 1:
        return arr

    m = l / 2
    print "{1}m is *******************{0}".format(m, tt)
    # print(arr[0:m])
    # print(arr[m:l])
    a1 = merge_sort(arr[0:m], x + 1)

    print "{1}a1 is *******************{0}".format(a1, tt)

    # print a1
    # print "now a1 is *******************{0}".format(arr)
    b1 = merge_sort(arr[m:l], x + 1)
    print "{1}b1 is *******************{0}".format(b1, tt)
    print "{2}mergeing {0} {1}".format(a1, b1, tt)

    c = merge2(a1, b1)
    print "{1}result is {0}".format(c, tt)
    # cnt = cnt + 1
    return c

if __name__ == '__main__':
    # merge_sort([3, 2])
    print merge_sort([9, 7, 4, 3.2, 8, 6], 0)
