#!/usr/bin/python3
""" Prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":

    user, passwd, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, passwd, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()  # invokes sessionmaker.__call__()

    state = session.query(State).order_by(State.id).first()

    if state is None:
        print("Nothing")
    print("{:d}: {}".format(state.id, state.name))

    session.close()
