# ValueError
# try:
#     print 'try...'
#     r = 10 / int('a')
#     print 'result:', r
# except ValueError, e:
#     print 'ValueError:', e
# except ZeroDivisionError, e:
#     print 'ZeroDivisionError:', e
# finally:
#     print 'finally...'
# print 'END'


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    # ZeroDivisionError is sub of StandardError
    except ZeroDivisionError, e:
        print "ZeroDivisionError", e
    except ValueError, e:
        print "ValueError", e
    except StandardError, e:
        print 'Error!'
    finally:
        print 'finally...'

main()


def foo2():
    try:
        10 / 0
    except ZeroDivisionError:
    	# raise
        raise ValueError('input error!')


def main2():
    try:
        foo2()
    except ZeroDivisionError, e:
        print "ZeroDivisionError", e
    except ValueError, e:
        print "ValueError", e
    finally:
        print "main2 END"
main2()
