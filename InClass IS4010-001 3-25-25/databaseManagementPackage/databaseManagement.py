# databaseManagement.py

import pyodbc

class DatabaseManagement:
    def connect_to_database(self):
        '''
        Connect to our SQL server instance
        @return the connection object or None on failure
        '''
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                        'Database=IS4010;'
                        'uid=IS4010Login;'
                        'pwd=P@ssword2;')
            return conn
        except:
            # what do we do if we end up here
            # print("Unable to connect to database") # probably not wise
            return None
    def submit_sql_to_server(self, conn, sql_statement):
        '''
        Submit a sql statement to the server
        @param conn connection object: the connection object 
        @param sql statement String: the sql to submit
        @rturn the poydbc cursor object that contains the query results
        '''
        cursor = conn.cursor()
        # modify the sql to return only private schools 
        cursor.execute('SELECT * FROM tAmericanAthleticConference WHERE IsPrivate = 1') # Submit a query to the SQL Server instance and store the results in the cursor object
        return cursor 
        