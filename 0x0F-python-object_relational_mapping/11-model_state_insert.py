#!/usr/bin/python3
"""This script adds the State object Louisiana to the database hbtn_0e_6_usa"""

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
    state_new = State(name="Louisiana")
    session.add(state_new)
    session.commit()
    print('{0}'.format(state_new.id))
    session.close()
