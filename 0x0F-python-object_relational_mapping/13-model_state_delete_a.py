#!/usr/bin/python3
"""This script deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Deletes State objects on the database """

    url_db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(url_db)
    Session = sessionmaker(bind=engine)
    session = Session()
    st = session.query(State).filter(State.name.contains('a'))
    if st is not None:
        for state in st:
            session.delete(state)
    session.commit()
    session.close()
