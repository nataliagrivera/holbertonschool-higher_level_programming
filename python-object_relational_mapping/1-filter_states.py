#!/usr/bin/python3

"""Lists all states starting with 'N' from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # Create a cursor object
    cur = db.cursor()

    # Execute the query to select states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch and print the results
    for row in cur.fetchall():
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
