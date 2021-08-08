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

    db = MySQLdb.connect(host="localhost", port=3306, user=root,
                         passwd=password, db=db_name)

    cursor = db.cursor()

    cursor.execute("""SELECT cities.name FROM states
                    INNER JOIN cities
                    ON states.id = cities.state_id
                    WHERE states.name = %s
                    ORDER BY cities.id ASC""", (state_name,))

    data = cursor.fetchall()

    city = []
    for row in data:
        city.append(row[0])
    print(*city, sep=", ")

    cursor.close()
    db.close()
