# cat cgi-bin/checkbox.py

#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form.getvalue('Python'):
        course_python = "You have selected Python Course"
else:
   course_python = "You have not selected"

if form.getvalue('Perl'):
    course_perl = "You have selected Perl Course"
else:
    course_perl = "You have not selected"

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Checkbox - CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2> CheckBox Python is : %s</h2>" % course_python)
print ("<h2> CheckBox Perl is : %s</h2>" % course_python)
print ("</body>")
print ("</html>")
