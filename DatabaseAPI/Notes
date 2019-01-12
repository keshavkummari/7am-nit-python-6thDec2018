Python MySQL Database Access:
*****************************
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

Here is the list of available Python database interfaces:
*********************************************************
Python Database Interfaces and APIs .
You must download a separate DB API module for each database you need to access.
For example, if you need to access an Oracle database as well as a MySQL database,
you must download both the Oracle and the MySQL database modules.

The DB API provides a minimal standard for working with databases using
Python structures and syntax wherever possible.

This API includes the following:

1. Importing the API module.
2. Acquiring a connection with the database.
3. Issuing SQL statements and stored procedures.
4. Closing the connection
-----------------------------------------------------------
What is MySQLdb?
****************
MySQLdb is an interface for connecting to a MySQL database server from Python.
It implements the Python Database API v2.0 and is built on top of the MySQL C API.

-----------------------------------------------------------
How do I Install MySQLdb?
*************************
Before proceeding, you make sure you have MySQLdb installed on your machine.
Just type the following in your Python script and execute it:

#!/usr/bin/python
import MySQLdb

Note: If it produces the following result,
then it means MySQLdb module is not installed:

Output:
Traceback (most recent call last):
  File "test.py", line 3, in <module>
    import MySQLdb
ImportError: No module named MySQLdb

-----------------------------------------------------------------
To install MySQLdb module, download it from MySQLdb website:

Go to browser and serach for this package and download and move it to linux server:

MySQL-python-1.2.2.tar.gz

$ tar -xvf MySQL-python-1.2.2.tar

$ cd MySQL-python-1.2.2

$ python setup.py build

$ python setup.py install

Note: Make sure you have root privilege to install above module.
-----------------------------------------------------------------
Database Connection:
********************

Before connecting to a MySQL database, make sure of the followings -
You have created a database HADOOP.

1. You have created a table emp in HADOOP.
2. This table has fields FIRST_NAME, LAST_NAME, AGE, SEX and INCOME.
3. User ID "root" and password "redhat" are set to access HADOOP.
4. Python module MySQLdb is installed properly on your machine.
5. You have gone through MySQL tutorial to understand MySQL Basics.
-----------------------------------------------------------------
# yum install MySQLdb* -y
-----------------------------------------------------------------
Example:

Following is the example of connecting with MySQL database "HADOOP"

#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","redhat","HADOOP" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version : %s " % data)

# disconnect from server
db.close()


Output:
Database version : 5.0.45

-----------------------------------------------------------------
If a connection is established with the datasource, then a Connection Object is returned and saved into db for further use, otherwise db is set to None. Next, db object is used to create a cursor object, which in turn is used to execute SQL queries. Finally, before coming out, it ensures that database connection is closed and resources are released.

Creating Database Table
Once a database connection is established, we are ready to create tables or records into the database tables using execute method of the created cursor.

Example
Let us create Database table emp:

#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","redhat","HADOOP" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS emp")

# Create table as per requirement
sql = """CREATE TABLE emp (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         Gender CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

# disconnect from server
db.close()
-----------------------------------------------------------------
INSERT Operation:
*****************

It is required when you want to create your records into a database table.

Example
The following example, executes SQL INSERT statement to create a record into emp table -

#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","redhat","HADOOP" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO emp(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()

-----------------------------------------------------------------
Above example can be written as follows to create SQL queries dynamically -

#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","redhat","HADOOP" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO emp(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()

-----------------------------------------------------------------
Example:

Following code segment is another form of execution where you can pass parameters directly -

..................................
user_id = "redhat"
password = "password"

con.execute('insert into Login values("%s", "%s")' % \
             (user_id, password))
..................................
-----------------------------------------------------------------
READ Operation:
***************

READ Operation on any database means to fetch some useful information from the database.

Once our database connection is established, you are ready to make a query into this database. You can use either fetchone() method to fetch single record or fetchall() method to fetech multiple values from a database table.

fetchone():
It fetches the next row of a query result set.
A result set is an object that is returned when a cursor object is used to query a table.

fetchall(): It fetches all the rows in a result set.
If some rows have already been extracted from the result set, then it retrieves the remaining rows from the result set.

rowcount: This is a read-only attribute and returns the number of rows that were affected by an execute() method.

-----------------------------------------------------------------
Example:
********

The following procedure queries all the records from emp table having salary more than 1000 -

#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","redhat","HADOOP" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM emp \
       WHERE INCOME > '%d'" % (1000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # Now print fetched result
      print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income )
except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()

Output:

fname=Mac, lname=Mohan, age=20, sex=M, income=2000

-----------------------------------------------------------------
Update Operation:
*****************

UPDATE Operation on any database means to update one or more records, which are already available in the database.

The following procedure updates all the records having SEX as 'M'. Here, we increase AGE of all the males by one year.

Example
#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","redhat","HADOOP" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to UPDATE required records
sql = "UPDATE emp SET AGE = AGE + 1
                          WHERE SEX = '%c'" % ('M')
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()

-----------------------------------------------------------------
DELETE Operation:
*****************

DELETE operation is required when you want to delete some records from your database. Following is the procedure to delete all the records from emp where AGE is more than 20 -

Example
#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","redhat","HADOOP" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to DELETE required records
sql = "DELETE FROM emp WHERE AGE > '%d'" % (20)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()

-----------------------------------------------------------------
Performing Transactions:
************************

Transactions are a mechanism that ensures data consistency. Transactions have the following four properties:

Atomicity: Either a transaction completes or nothing happens at all.

Consistency: A transaction must start in a consistent state and leave the system in a consistent state.

Isolation: Intermediate results of a transaction are not visible outside the current transaction.

Durability: Once a transaction was committed, the effects are persistent, even after a system failure.

The Python DB API 2.0 provides two methods to either commit or rollback a transaction.

-----------------------------------------------------------------
Example:

You already know how to implement transactions. Here is again similar example -

# Prepare SQL query to DELETE required records
sql = "DELETE FROM emp WHERE AGE > '%d'" % (20)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
-----------------------------------------------------------------
COMMIT Operation:
*****************

Commit is the operation, which gives a green signal to database to finalize the changes, and after this operation, no change can be reverted back.

Output:
db.commit()

ROLLBACK Operation:
*******************
If you are not satisfied with one or more of the changes and you want to revert back those changes completely, then use rollback() method.

Output:
db.rollback()

Disconnecting Database:
***********************
To disconnect Database connection, use close() method.

Output:
db.close()

If the connection to a database is closed by the user with the close() method, any outstanding transactions are rolled back by the DB. However, instead of depending on any of DB lower level implementation details, your application would be better off calling commit or rollback explicitly.

*****************************************************
Handling Errors
There are many sources of errors. A few examples are a syntax error in an executed SQL statement, a connection failure, or calling the fetch method for an already canceled or finished statement handle.

The DB API defines a number of errors that must exist in each database module. The following table lists these exceptions.

Exception	Description:
************************

Warning	Used for non-fatal issues. Must subclass StandardError.
Error	Base class for errors. Must subclass StandardError.
InterfaceError	Used for errors in the database module, not the database itself. Must subclass Error.
DatabaseError	Used for errors in the database. Must subclass Error.
DataError	Subclass of DatabaseError that refers to errors in the data.
OperationalError	Subclass of DatabaseError that refers to errors such as the loss of a connection to the database. These errors are generally outside of the control of the Python scripter.
IntegrityError	Subclass of DatabaseError for situations that would damage the relational integrity, such as uniqueness constraints or foreign keys.
InternalError	Subclass of DatabaseError that refers to errors internal to the database module, such as a cursor no longer being active.
ProgrammingError	Subclass of DatabaseError that refers to errors such as a bad table name and other things that can safely be blamed on you.
NotSupportedError	Subclass of DatabaseError that refers to trying to call unsupported functionality.
Your Python scripts should handle these errors, but before using any of the above exceptions, make sure your MySQLdb has support for that exception. You can get more information about them by reading the DB API 2.0 specification.
-----------------------------------------------------------------
