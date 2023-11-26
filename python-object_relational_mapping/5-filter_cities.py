#!/usr/bin/python3

"""Lists all cities of a given state from the hbtn_0e_4_usa database"""
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
        # Prepare the query to retrieve cities of the specified state
        query = "SELECT cities.name " \
                "FROM cities " \
                "JOIN states ON cities.state_id = states.id " \
                "WHERE states.name = %s " \
                "ORDER BY cities.id ASC"

        # Execute the query with the state name as a parameter
        cursor.execute(query, (argv[4],))

        # Fetch and print the results
        results = cursor.fetchall()
        cities = ", ".join(city[0] for city in results)
        print(cities)

    except MySQLdb.Error as e:
        print("Error: {}".format(e))

    # Close cursor and database connection
    cursor.close()
    db.close()
