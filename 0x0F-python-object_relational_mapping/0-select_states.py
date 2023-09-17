#!/usr/bin/python3
""" This script lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Access to the database and get the states from the database.
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
										passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cursor_db = cursor_db.cursor()
    cursor_db.execute("SELECT * FROM states")
    rows_selected = cursor_db.fetchall()

    for row in rows_selected:
        print(row)
