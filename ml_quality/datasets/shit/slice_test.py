# this is traditional loops
print "this is **********slice_test.py**************"
s = ["sdf", "user1", "biingpang", "shelloc"]
i = 0
while i < 3:
    print s[i]
    i = i + 1

# print
# print "s[0:2] is:"
# print s[0:2]
#
# print 'space'[1:2]
# print 'asdfuierer'[-3:]
# print (1, 2, 3, 4, 'abc')[-2:]
# print

print '#############################print key###############################33'
dict = {"key1": "val1", "key2": "val2", "key3": "val3"}
for key in dict:
    print dict[key], key

print '#############################print value###############################33'
for value in dict.itervalues():
    print value
print '#############################print key value###############################33'
for k, v in dict.iteritems():
    print k, v

print range(1,10)
print [x * x for x in range(1, 10) if x % 2 == 0]

kandv = [k + '+' + v for k, v in dict.iteritems()]
print kandv


L = ['Hello', 'World', 18, 'Apple', None]
print [str(s).lower() for s in L]
# you can add charge after loop. operation before loop.
print [s.lower() for s in L if isinstance(s, str)]



