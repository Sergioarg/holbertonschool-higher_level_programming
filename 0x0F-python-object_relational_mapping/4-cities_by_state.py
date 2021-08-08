#!/usr/bin/python3
""" Module to connect to the database and print the data from the
    Table: States with specific number.
"""

import MySQLdb
import sys

from sqlalchemy.sql.functions import user

if __name__ == "__main__":

    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=db_name)

    cursor = db.cursor()

    cursor.execute("""SELECT cities.id, cities.name, states.id FROM cities
                    INNER JOIN states ON cities.id = states.id
                    ORDER BY cities.id ASC""")

    data = cursor.fetchall()

    for state in data:
        print(state)

    db.close()
