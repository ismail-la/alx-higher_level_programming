#!/usr/bin/python3
"""Script that prints all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Access to the database and get the cities from the database"""

    url_db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(url_db)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_new = State(name='California')
    city_new = City(name='San Francisco')
    state_new.cities.append(city_new)
    session.add(state_new)
    session.commit()
    session.close()
