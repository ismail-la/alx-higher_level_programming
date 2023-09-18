#!/usr/bin/python3
"""This script changes the name of a State object from
 the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Updates a State object on the database"""

    url_db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(url_db)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_new = session.query(State).filter(State.id == 2).first()
    state_new.name = "New Mexico"
    session.commit()
    session.close()
