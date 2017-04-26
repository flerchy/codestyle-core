#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import logging
import time
logging.basicConfig(level=logging.DEBUG)


class Dao(object):

    """docstring for Dao"""

    def __init__(self):
        super(Dao, self).__init__()
        # self.arg = arg
        self.con = mdb.connect('localhost', 'root', '355itu11', 'test')

    def doSelect(self, sql):
        with self.con:
            cur = self.con.cursor(mdb.cursors.DictCursor)

            logging.info('sql is {0}'.format(sql))
            cur.execute(sql)
            rows = cur.fetchall()
            # logging.debug("rows is {0}".format(rows))
            return rows

    def doInsert(self, *args):
        with self.con:
            cur = self.con.cursor()
            for arg in args:
                print 'arg is', arg
                # arg2 = ('1005', 'Michael', 'michael@test.org', '12345', '1435643143.863552')
                cur.execute('insert into `user` (id,`name`,email, passwd,last_modified) values (%s, %s, %s, %s, %s)', arg)

    def doUpdate(self, **kw):
        sql_front = 'update `user` set '
        sql_tail = ' where id = %s;'
        vals = []
        msql = []
        for key, value in kw.iteritems():
            # msql += " {0} = %s ".format(key)
            if key != 'id':
                msql.append("{0} = %s".format(key))
                vals.append(value)

        # append id for update
        vals.append(kw["id"])
        sql = '{0}{1}{2}'.format(sql_front, ','.join(msql), sql_tail)
        print sql
        # logging.debug('sql is ', sql)
        print vals
        # logging.debug('values is ', vals)
        with self.con:
            cur = self.con.cursor()
            cur.execute(sql, vals)

if __name__ == '__main__':

    print "############################# select ########################################"
    d = Dao()
    rows = d.doSelect("select * from `user`")
    for x in rows:
        logging.info('{0} {1} {2}'.format(x["id"], x["name"], x["email"]))
    print ""
    rows = d.doSelect("select * from `user` where id in (100,1000)")
    for x in rows:
        logging.info('{0} {1} {2}'.format(x["id"], x["name"], x["email"]))

    print "############################# insert ########################################"

    # ins = []
    # ins.append((1005, 'Michael', 'michael@test.org', '12345', time.time()))
    # ins.append((1008, 'Peter', 'peter@test.org', '12345', time.time()))
    # ins.append((10001, 'Test', 'Test@test.org', '12345', time.time()))
    # d.doInsert(*ins)

    print "############################# update ########################################"
    d.doUpdate(id=1005 ,name='Gary', email='Gary@test.org', last_modified=time.time())
