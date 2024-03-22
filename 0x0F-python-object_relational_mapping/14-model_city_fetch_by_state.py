#!/usr/bin/python3
"""prints all cities with state name"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.base import instance_dict
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    instances = session.query(State, City)\
                       .filter(State.id == City.state_id)\
                       .order_by(City.id).all()

    for state, city in instances:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
