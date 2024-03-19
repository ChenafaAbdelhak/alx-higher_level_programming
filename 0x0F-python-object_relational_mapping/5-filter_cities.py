#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') FROM
                cities INNER JOIN states ON states.id=cities.state_id AND
                states.name=%s""",
                (sys.argv[4],))
    row = cur.fetchone()[0]
    if row:
        print(row)
    else:
        print("")
    cur.close()
    db.close()
