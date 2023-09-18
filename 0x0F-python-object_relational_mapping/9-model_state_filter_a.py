#!/usr/bin/python3
"""Script that lists all State objects that contain the letter a from
the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """ Access to the database and get a state from the database """

    url_db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(url_db)
    Session = sessionmaker(bind=engine)
    session = Session()
    st = session.query(State).filter(State.name.contains('a'))
    if st is not None:
        for state in st:
            print('{0}: {1}'.format(state.id, state.name))
