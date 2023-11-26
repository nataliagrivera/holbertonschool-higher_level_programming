#!/usr/bin/python3

"""Lists all cities from the hbtn_0e_4_usa database"""
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

    try:
        # Execute the query to retrieve all cities with their respective states
        query = "SELECT cities.id, cities.name, states.name " \
                "FROM cities " \
                "JOIN states ON cities.state_id = states.id " \
                "ORDER BY cities.id ASC"

        # Execute the query
        cursor.execute(query)

        # Fetch and print the results
        results = cursor.fetchall()
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("Error: {}".format(e))

    # Close cursor and database connection
    cursor.close()
    db.close()
