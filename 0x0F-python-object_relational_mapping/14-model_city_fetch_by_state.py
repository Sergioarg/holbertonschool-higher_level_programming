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

    all_elements = session.query(State.name, City.id, City.name).filter(
        State.id == City.state_id).order_by(City.id)

    for city_state in all_elements:
        print("{:s}: ({:d}) {:s}".format(
            city_state[0], city_state[1], city_state[2]))

    session.close()
