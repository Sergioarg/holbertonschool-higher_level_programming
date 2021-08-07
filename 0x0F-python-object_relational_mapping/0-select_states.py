#!/usr/bin/python3
import MySQLdb
import sys

""" Module to connect to the database and print the data from the
    Table: States.

"""
if __name__ == "__main__":

    root = sys.argv[1]
    password = sys.argv[2]
    data_base = sys.argv[3]

    # Open database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=root,
                         passwd=password, db=data_base)

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch a single row using fetchall() method.
    data = cursor.fetchall()

    for element in data:
        print(element)

    # disconnect from server
    db.close()
    cursor.close()
