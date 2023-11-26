#!/usr/bin/python3
"""Prints the State object with the name passed as argument from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                        format(username, password, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name == state_name).order_by(State.id).first()

    if query:
        print(query.id)
    else:
        print("Not found")
