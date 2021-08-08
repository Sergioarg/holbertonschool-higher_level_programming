#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_city import Base, City
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":

    user, passwd, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, passwd, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State.name.label('state__name'),
                          State.id.label('state__id'),
                          City.id.label('city_id'),
                          City.name.label('city_name')
                          ).join(City, State.id == City.state_id)

    for city in query.order_by(City.id):
        print("{}: ({}) {}".format(
            city.state__name, city.city_id, city.city_name))

    session.close()
