#!/usr/bin/python3
"""This script takes in an argument and displays all values in the states
where name matches the argument from the database hbtn_0e_0_usa
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """Access to the database and get the states from the database """
    connect-db = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    cursor_db = connect-db.cursor()
    cursor_db.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
                        states.id ASC".format(argv[4]))
    rows_selected = cursor_db.fetchall()
    for row in rows_selected:
        print(row)
