#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa
where name matches the argument."""
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
    state_name = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE NAME LIKE BINARY '{}'"
                .format(state_name))
    for row in cur.fetchall():
        print(row)
    cur.close()
    database.close()
