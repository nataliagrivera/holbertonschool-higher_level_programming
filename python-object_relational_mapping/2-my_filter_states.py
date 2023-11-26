#!/usr/bin/python3

"""Display values in the states table based on the given state name"""
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
    cursor = db.cursor()

    # Get the state name from the argument
    state_name = argv[4]

    # Prepare the SQL query using parameterized query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query with parameterized input
    cursor.execute(query, (state_name,))

    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
