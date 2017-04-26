#!/usr/bin/python
# -*- coding: utf-8 -*-


class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        print self.__class__
        return '<%s:%s>' % (self.__class__.__name__, self.name)


# f = Field('zhangsan', 'int')
# print f

class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


# s = StringField('username')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):

    def __new__(
        cls,
        name,
        bases,
        attrs,
        ):

        # print 'cls', cls

        print 'attrs:', attrs

        # print 'name', name
        # print 'bases', bases

        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        # 将以前attrs中的属性装入到mapping中去

        mappings = dict()
        for (k, v) in attrs.iteritems():
            if isinstance(v, Field):
                print 'Found mapping: %s==>%s' % (k, v)
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__table__'] = name  # 假设表名和类名一致
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        print 'attrs:', attrs
        return type.__new__(cls, name, bases, attrs)


class Model(dict):

    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        print kw
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'"
                                  % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for (k, v) in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__,
                ','.join(fields), ','.join(params))
        print 'SQL: %s' % sql
        print 'ARGS: %s' % str(args)


# testing code:

class User(Model):

    id = IntegerField('uid')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


u = User(id=12345, name='Michael', email='test@orm.org',
         password='my-pwd')

u.save()
print User.__mappings__
print u.__mappings__
print dir(u)
