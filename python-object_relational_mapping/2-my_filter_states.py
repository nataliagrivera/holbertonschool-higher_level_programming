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

    # Prepare the SQL query using string formatting
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    # Execute the query
    cursor.execute(query)

    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
