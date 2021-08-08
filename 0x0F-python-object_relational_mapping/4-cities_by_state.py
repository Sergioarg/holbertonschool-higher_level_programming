#!/usr/bin/python3
""" Module to connect to the database and print the data from the
    Table: States with specific number.
"""

import MySQLdb
import sys

if __name__ == "__main__":

    usr, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=usr,
                         passwd=password, db=db_name)

    cursor = db.cursor()

    cursor.execute("""SELECT cities.id, cities.name, states.name
                    FROM cities
                    INNER JOIN states
                    ON cities.state_id = states.id
                    ORDER BY cities.id ASC""")

    data = cursor.fetchall()

    for state in data:
        print(state)

    cursor.close()
    db.close()
