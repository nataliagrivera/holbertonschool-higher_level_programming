#!/usr/bin/python3

"""Lists all states starting with 'N' from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    u_name = argv[1]
    psw = argv[2]
    base = argv[3]

    # Connecting to MySQL database
    db = MySQLdb.connect(host="localhost", user=u_name,
                        passwd=psw, db=base, port=3306)

    # Creating cursor object
    cur = db.cursor()

    # Executing MySql Query
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    # Obtaining Query Result & prints the result in rows
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)

    # Clean Up
    cur.close()
    db.close()
