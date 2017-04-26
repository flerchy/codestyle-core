#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb


def doUpdate(con, tp):
    cur = con.cursor()

    print tp
    cur.execute("UPDATE Writers SET Name = %s WHERE Id = %s", tp)
    print "Number of rows updated:", cur.rowcount

con = mdb.connect('localhost', 'root', '355itu11', 'test')


def doUpdate2(con, name, iid):
    print name
    print iid
    cur = con.cursor()
    mlist = [name, iid]
    print mlist
    # cur.execute("UPDATE Writers SET Name = %s WHERE Id = %s".format(name, iid))
    cur.execute("UPDATE Writers SET Name = %s WHERE Id = %s", mlist)

    print "Number of rows updated:", cur.rowcount
    # print tuple(name, iid)

with con:
    # doUpdate(con, ("Guy de Maupasant", "16"))
    val = {"iid":16, "name":"Guy de Maupasant2"}
    doUpdate2(con, **val)

