#!/usr/bin/python3
""" Module to connect to the database and print the data from the
    Table: States with specific number.
"""

import MySQLdb
import sys

if __name__ == "__main__":

    root = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    name_state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=root,
                         passwd=password, db=db_name)

    cursor = db.cursor()

    cursor.execute("""SELECT * FROM states
                      WHERE name = %s
                      ORDER BY id ASC""", (name_state,))

    data = cursor.fetchall()

    for state in data:
        print(state)

    db.close()
