"""
The Python standard for database interfaces is the Python DB-API. 
Most Python database interfaces adhere to this standard.

You can choose the right database for your application.
Python Database API supports a wide range of database servers such as :

1. GadFly
2. mSQL 
3. MySQL
4. PostgreSQL
5. Microsoft SQL Server 2000
6. Informix
7. Interbase
8. Oracle
9. Sybase
10. mariadb


To communicate with Databases we need a language i.e. ANCI SQL 2003

Database API's :

Step-1 : Import API 

Step-2 : Connection the DB from the code

Step-3 : Execute SQL Queries 

Step-4 : Closing the connection
"""

#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("13.233.113.46","root","redhat@123")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print("Database version : %s " % data)

# disconnect from server
db.close()
