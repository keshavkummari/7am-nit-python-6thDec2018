#!/usr/bin/python

import sys

try:
    f = open('abc.txt')
    #f = open('C:\\Users\\Jessicah Princess\\Desktop\\OnlineUcator.txt')
    s = f.readline()
    #i = int(s.strip())
    print (f.read())
except IOError as err:
    print("I/O error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

'''Output:
    I/O error: [Errno 2] No such file or directory: 'myfile.txt'
'''
