"""
SMTP or Mail Server Details :

UserName : 
PassWord :
Hostname :
Port No  :

"""

#!/usr/bin/python
import smtplib

sender = 'root@mail.abiel.com'
receivers = ['mahesh@abiel.com','sundeep@abiel.com','abiel@abiel.com']

message = """From: From Person <root@abiel.com>
To: To Person <mahesh@abiel.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print ("Email has been sent successfully")
except SMTPException:
   print ("Error: unable to send email")



[root@smtp ~]# cat smtp.py
#!/usr/bin/python
import smtplib

sender = 'root@smtp.kk.com'
receivers = ['nareshit@smtp.kk.com','balaji@smtp.kk.com']

message = """From: From Person <root@smtp.kk.com>
To: To Person <'nareshit@smtp.kk.com','balaji@smtp.kk.com'>
Subject: SMTP e-mail test - Using Python Code

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print ("Email has been sent successfully")
except SMTPException:
   print ("Error: unable to send email")



