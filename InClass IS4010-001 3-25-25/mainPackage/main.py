# main.py
# Connecting to SQL Server with Python
# Install the pyodbc library first:
# pip install pyodbc or use VS to do it
# Bill Nicholson
# nicholdw@ucmail.uc.edu
import pyodbc

# instantaiate the database mgmt class as an object called dbm
from databaseManagementPackage.databaseManagement import *

dbm = DatabaseManagement()

#invoke the connect method in the dbm object and store in an object called conn
conn = dbm.connect_to_database()

# modify the code: implement a class method to replace the code in lines 20 and 21
cursor = dbm.submit_sql_to_server(conn,'SELECT * FROM tAmericanAthleticConference WHERE IsPrivate = 1')


total_enrollment = 0
# Step through all the rows in the results set
for row in cursor: # everyhting in the cursor is a string regardless of waht it is in the table 
    print(row); # All columns in the row
    print (row[1]); # Second column
    print (row[2]); # Third column
    print (row[3]); # Third column
    total_enrollment = total_enrollment + int(row[2]) # running sum of enrollments
print ("Total enrollment = " + str(total_enrollment))
print("------------------------------------------------")
cursor = conn.cursor()
# Submit a query to the SQL Server instance and store the results in the cursor object
cursor.execute('SELECT University, Enrollment, IsPrivate FROM tAmericanAthleticConference')
for row in cursor:
    print(row.University)
