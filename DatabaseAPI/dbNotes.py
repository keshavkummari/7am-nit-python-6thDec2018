import MySQLdb, csv, sys
conn = MySQLdb.connect (host = "localhost",user = "root", passwd = "redhat@123",db = "pythonworld")
c = conn.cursor()
csv_data=csv.reader(file("a.txt"))
for row in csv_data:
	print row
	c.execute("INSERT INTO a (first, last) VALUES (%s, %s), row")
c.commit()
c.close()