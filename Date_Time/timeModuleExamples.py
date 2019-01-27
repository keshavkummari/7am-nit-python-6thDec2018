"""
#!/usr/bin/python3
import time

def procedure():
    time.sleep(60)

# measure process time
t0 = time.clock()
procedure()
print (time.clock() - t0, "seconds process time")

# measure wall time
t0 = time.time()
procedure()
print (time.time() - t0, "seconds wall time")


"""
import time

print ("ctime : ", time.ctime())


print ("gmtime :", time.gmtime(1455511418.000000)) # 1970 no of sec's until  1020304050.34375

print ("time.localtime() : %s" , time.localtime())

t = (2016, 2, 15, 10, 13, 38, 1, 48, 0)
d = time.mktime(t)
print ("time.mktime(t) : %f" %  d)
print ("asctime(localtime(secs)): %s" % time.asctime(time.localtime(d)))
