#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost",
                         port=3306, user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    insert_stmt = "SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC"
    cur.execute(insert_stmt)

    rows = cur.fetchall()
    for i in rows:
        print(i)

    cur.close()
    db.close()
