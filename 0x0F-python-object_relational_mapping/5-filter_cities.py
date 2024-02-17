#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists
all cities of that state, using the database
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    insert_stmt = "SELECT cities.id, cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s"
    data = [argv[4]]
    cur.execute(insert_stmt, data)

    rows = cur.fetchall()
    j = []
    for i in rows:
        j.append(i[1])
    print(", ".join(j))

    cur.close()
    db.close()