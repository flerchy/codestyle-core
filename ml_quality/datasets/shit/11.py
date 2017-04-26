def down_cast_qobject(tp, obj):
    assert obj
    assert isinstance(tp, type)
    assert issubclass(tp, QObject)
    addresses = shiboken.getCppPointer(obj)
    assert isinstance(addresses, collections.Iterable)
    assert len(addresses)
    ptrs = filter(lambda p: p > 0L, addresses)
    assert ptrs
    ptr = ptrs[0]
    assert isinstance(ptr, long)
    wrapped = shiboken.wrapInstance(ptr, tp)
    assert isinstance(wrapped, tp)
    return wrapped
