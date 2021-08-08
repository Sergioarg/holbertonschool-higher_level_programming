#!/usr/bin/python3
""" Module to connect to the database and print the data from the
    Table: States that inicialize with "N".
"""

import MySQLdb
import sys

if __name__ == "__main__":

    root = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Open database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=root,
                         passwd=password, db=db_name)

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch a single row using fetchall() method.
    data = cursor.fetchall()

    for state in data:
        if (state[1][0] == 'N'):
            print(state)

    # disconnect from server
    cursor.close()
    db.close()
