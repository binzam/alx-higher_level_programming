#!/usr/bin/python3
"""lists all states with a name starting with 'N'
from hbtn_0e_0_usa database."""
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        port=3306,
        password=sys.argv[2],
        database=sys.argv[3],
    )
    cur = database.cursor()
    cur.execute("SELECT * FROM states WHERE NAME LIKE BINARY 'N%'")
    for row in cur.fetchall():
        print(row)
    cur.close()
    database.close()
