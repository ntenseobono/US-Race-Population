import psycopg2
import psqlConfig as config
from psycopg2.extensions import AsIs


def connect():
    '''
    Establishes a connzection to the database with the following credentials:
        user - username, which is also the name of the database
        password - the password for this database on perlman

    Returns: a database connection.

    Note: exits if a connection cannot be established.
    '''
    try:
        connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        print("Connection sucessful\n")
    except Exception as e:
        print("Connection error: ", e)
        exit()
    return connection


def get_national_total_population(connection, race):
    '''
    Retrieves all earthquakes with a magnitude greater than the specified magnitude     

    Parameters:
        connection - the connection to the database
        magnitude - retrieve all earthquakes above this magnitude from the data

    Returns:
        a collection of all earthquakes above this magnitude, or None if the query fails.
    '''
    try:
        cursor = connection.cursor()
        # query = "EXECUTE format('SELECT SUM($1) FROM racepopulation', %s)" 
        query = "EXECUTE SELECT SUM($1) FROM racepopulation"
        "USING race;"
        cursor.execute(query, race)
        return cursor.fetchall()

    except psycopg2.Error as e:
        print ("Something went wrong when executing the query: ", e)
        return None

def get_state_total_population(connection, race, state):
    '''
    '''
    try:
        cursor = connection.cursor()
        query = 'SELECT "%s" FROM racepopulation WHERE Label ILIKE "%s" AND "%s" IS NOT NULL'
        cursor.execute(query, (race, state, race))
        return cursor.fetchall()
    
    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None
    
def compare_total_population(connection, race): 
    '''
    '''
    try:
        cursor = connection.cursor()
        query_one = get_national_total_population(connection, race)
        query_two = get_national_total_population(connection, race)
        return cursor.fetchall()
    
    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None
        

 
def main():
    '''
    '''
    # Connect to the database
    connection = connect()
    results = test(connection, 'Total')
    # Execute a simple query: how many earthquakes above the specified magnitude are there in the data?
    # results = get_national_total_population(connection, 'Total')

    if results is not None:
        print("Query results: ")
        for item in results:
            print(item)

    # Disconnect from database
    connection.close()

main()