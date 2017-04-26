#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import logging
logging.basicConfig(level=logging.DEBUG)


print mdb.__file__
print logging.__file__

con = mdb.connect('localhost', 'root', '355itu11', 'test')

# with con:

#     cur = con.cursor()
#     cur.execute("DROP TABLE IF EXISTS Writers")
#     cur.execute("CREATE TABLE Writers(Id INT PRIMARY KEY AUTO_INCREMENT, \
#                  Name VARCHAR(25))")
#     cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
#     cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
#     cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
#     cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
#     cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")
print "###########################method one#################################"

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Writers")

    rows = cur.fetchall()

    print rows

    for row in rows:
        print row
        print row[0], row[1]

print "###########################method two#################################"
with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Writers")

    for i in range(cur.rowcount):

        row = cur.fetchone()
        print row[0], row[1]

print "###########################method three(The dictionary cursor)#################################"

with con:

    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute("SELECT * FROM Writers LIMIT 4")

    rows = cur.fetchall()

    logging.debug("rows is {0}".format(rows))
    for row in rows:
        print row["Id"], row["Name"]
        # print row.Id, row.Name

print "###########################Column headers#################################"
with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Writers LIMIT 5")

    rows = cur.fetchall()
    logging.debug(rows)

    desc = cur.description

    logging.debug(desc)
    print "%s %10s" % (desc[0][0], desc[1][0])
    print "%s %3s" % (desc[0][0], desc[1][0])


    for row in rows:
    	print type(row).__name__    
        print "%2s %3s" % row
# >>> print "%5s" % "abc"
#   abc
# >>> print "%5s" % "abcdefs"
# abcdefs
# >>> print "%5s %5s" % ("abcdefs", "abc")
# abcdefs   abc
# >>> print "%5s %5s" % ("abcdefs", "abcde")
# abcdefs abcde
# >>> 
