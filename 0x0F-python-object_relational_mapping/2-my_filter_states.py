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
    state_name = sys.argv[4]

    # Open database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=root,
                         passwd=password, db=db_name)

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name='{}' ORDER BY id ASC".format(
            state_name))

    # Fetch a single row using fetchall() method.
    data = cursor.fetchall()

    for state in data:
        print(state)

    # disconnect from server
    db.close()
    cursor.close()
