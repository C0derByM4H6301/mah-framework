import argparse # 1
from colorama import * # 2
import os # 3
import time # 4
import logging # 5
import readline # 6
import random # 7
from requests import get # 8
import http.server # 9
import socketserver # 10
from lib import banner # 11
from lib import portscanner # 12
from lib import rs # 13
#import progressbar # 13
#"NMAP"
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
init(autoreset=True)
#info
Version = 1.5
Author = "Coder Mahmut"
GitHub = "https://github.com/C0derByM4H6301"
#helpful handsome guys=hng
hng="My brother is Yusufcan(HAFIZ)"
hng="My friend is Ahmet"
hng="My friend is Sefa"
hng="My friend is Berat"
hng="My big machine is Emin"
hng="My friend is Bunyamin"
#info done

# Argparse 
parser = argparse.ArgumentParser()
parser.add_argument("-s","--start",help="start to mah-framework",action="store_true")
parser.add_argument("--install",help="installs the necessary software for mah-framework",action="store_true")
parser.add_argument("-v","--version",help="version information",action="store_true")
parser.add_argument("-q","--quiet",help="quiet output",action="store_true")
parser.add_argument("--http-server",help="start to http server, port: 8000",action="store_true")
parser.add_argument("--portscan",help="start to portscan, E.g: --portscan 127.0.0.1")
args = parser.parse_args()
#Argparse done
hostname=Fore.BLUE+"SERDAR"
username=Fore.RED+"developer"
et=Fore.YELLOW+"@"
loc=Fore.CYAN+"Main"+Fore.WHITE+"/"
ip=Fore.GREEN+"127.0.0.1"
type_head=Fore.MAGENTA+"mh-f"
head1=Fore.BLUE+">"
head2=Fore.CYAN+">"
type_color=Fore.WHITE+" "
say=Fore.LIGHTCYAN_EX+"I like Machine!"
space_string=Fore.WHITE+" ~ "
##++++++++++++++++
#Emin makine easteregg
banner11="""
 / \----------------------, 
 \_,|                     | 
    |    I like machine   | 
    |  ,--------------------
    \_/___________________/ 
"""
banner12="""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▄█░▄▀▄░██▄██░▄▄▀████▄██░▄▄███░▄▄▀████░▄▀▄░█░▄▄▀█▀▄▀█░█████▄██░▄▄▀█░▄▄
██░▄▄▄█░█▄█░██░▄█░██░████░▄█▄▄▀███░▀▀░████░█░█░█░▀▀░█░█▀█░▄▄░██░▄█░██░█░▄▄
██░▀▀▀█▄███▄█▄▄▄█▄██▄███▄▄▄█▄▄▄███▄██▄████░███░█▄██▄██▄██▄██▄█▄▄▄█▄██▄█▄▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
"""
#Emin makine easteregg done
readline.parse_and_bind("tab: complete")
##autocomplate function
def complete(text,state):
    volcab = ['help','install','banner','exec','modules','show','jobs','ip','portscan','say','set','hostname','exit','mini_say','Emin','emin','start','torghost','stop','getip']
    results = [x for x in volcab if x.startswith(text)] + [None]
    return results[state]
#get ip function
def getip():
    IP_API = "https://api.ipify.org/?format=json"
    while True:
        try:
            jsonRes = get(IP_API).json()
            ipTxt = jsonRes["ip"]
        except:
            continue
        break
    return Fore.CYAN+ipTxt
#jobs function
torghost=False

def stop():
    if torghost==True:
        os.system("python modules/Anominy/torghost/torghost.py -x")

def jobs():
    asd,dsa,sad=Fore.BLUE+"[",Fore.BLUE+"]",Fore.RED+"*"
    if torghost==True:
        print(asd+sad+dsa+Fore.CYAN+" Torghost is running")
    if torghost==False:
        print(asd+sad+dsa+Fore.CYAN+" Torghost is stoped")        
#jobs function
# http-server function
def http_server():
    try:
        PORT = 8000
        Handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("serving at port", PORT)    
            print("use CTRL+C for exit")
            httpd.serve_forever()
    except KeyboardInterrupt:
        exit("CTRL+C detected, httpd is shutting")
def framework_install():
    print(Fore.YELLOW+"Installation started!!!")
    os.system("sudo apt-get install python3 -y")
    os.system("sudo apt-get install python3-pip -y")
    os.system("sudo apt-get install tor -y")
    os.system("sudo pip3 install colorama")
    os.system("sudo pip3 install os")
    os.system("sudo pip3 install time")
    os.system("sudo pip3 install argparse")
    os.system("sudo pip3 install logging")
    os.system("sudo pip3 install readline")
    os.system("sudo pip3 install pyfiglet")
    os.system("sudo pip3 install progressbar")
    os.system("sudo pip3 install pyftpdlib")
    os.system("sudo pip3 install emoji")
    os.system("sudo pip3 install -r modules/Anominy/torghost/requirements.txt")
    os.system("sudo chmod 777 modules/Anominy/torghost/torghost.py")
    os.system("bash modules/Anominy/torghost/build.sh")
    os.system("sudo rm -rf build")
    print(Fore.RED+"installation successful!")
def help():
    help_string="""
    help : This command writes you the help documents.
    exit : It closes the running modules and exits.
    getip : Use it to find out your ip.
    exec : When this command runs, the commands you type in the "exec>" input are executed in the shell.
    banner : Prints a banner on the screen.
    portscan : A tool that scans all ports. E.g: portscan 127.0.0.1 
    install : use it if it is necessary to reinstall the necessary tools.

    set : This command to assign data to some variables. Warning, press a space at most once after this command.
    |--> hostname : It is used to change the hostname variable. Example: set hostname serdar
    |--> ip : It is used to change the ip variable. Example: set hostname serdar
    |--> username : It is used to change the username variable. Example: set hostname serdar
    |--> say : It is used to change the say variable. Example: set hostname serdar
    |--> mini_say : It is used to change the mini_say variable. Example: set hostname serdar

    start : used to run existing modules.
    |--> torghost : Privacy and anonymity tool. Example: start torghost

    stop : It is used to stop or close current running modules.
    |--> torghost : Privacy and anonymity tool. Example: stop torghost

    show : prints things like running jobs and modules to the screen.
    |--> jobs : if you want to see current running processes use. Example: show jobs
    |--> modules : prints available modules to the screen. Example: show modules"""
    print(help_string)
#def animated_marker():
#    widgets = ['Loading: ', progressbar.AnimatedMarker()]
#    bar = progressbar.ProgressBar(widgets=widgets).start()
      
#    for i in range(40):
#        time.sleep(0.1)
#        bar.update(i)
# http-server function
bannerarg=True
if args.portscan:
    portscanner.portscanner.scan(args.portscan)
    bannerarg=False
if args.quiet:
    bannerarg=False

if args.start:
    #animated_marker()
    if bannerarg== True:
        banner.banners.random_banner()
    logging.info("shell is creating")
    readline.set_completer(complete)
    jobs=[]
    try:
        rs.random_sentence.random_sent()
        while True:
            random_number=random.randrange(1,3)
            sh=input(username+et+hostname+space_string+loc+space_string+ip+space_string+say+"\n"+type_head+space_string+head1+head2+type_color)
            if sh=="exit":
                logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
                logging.warning('Admin logged out')
                stop()
                exit()
            if sh=="help":
                help()
            if sh[:3]=="set":
                if sh[4:12]=="hostname":
                    hostname = Fore.BLUE+sh[13:]
                if sh[4:6]=="ip":
                    ip=Fore.GREEN+sh[7:]
                if sh[4:12]=="username":
                    username=Fore.RED+sh[13:]
                if sh[4:7]=="say":
                    say=Fore.BLUE+sh[8:]
                if sh[4:12]=="mini_say":
                    type_head=sh[13:]
            if sh=="username":
                print(username)
            if sh=="hostname":
                print(hostname)
            if sh=="say":
                print(say)
            if sh=="ip":
                print(ip)
            if sh[:5]=="start":
                if sh[6:]=="torghost":
                    if torghost==False:
                        os.system("python modules/Anominy/torghost/torghost.py -s")
                        torghost=True
                    if torghost==True:
                        logging.error("torghost started with") 
            if sh[:4]=="stop":
                if sh[5:]=="torghost":
                    if torghost==True:
                        os.system("python modules/Anominy/torghost/torghost.py -x")
                        torghost=False
                    if torghost==False:
                        logging.info("torghost is not running")
            if sh[:4]=="show":
                if sh[5:]=="jobs":
                    jobs()
                if sh[5:]=="modules":
                    print(Fore.RED+"Available modules: ")
                    print(Fore.BLUE+"Torghost")
            if sh=="emin" or sh=="Emin":
                if random_number==1:
                    print(banner11)
                if random_number==2:
                    print(banner12)
            if sh=="getip":
                print("your ip is: ",getip())
            if sh=="exec":
                cmd=input("command:=> ")
                os.system(cmd)
            if sh=="banner":
                banner.banners.random_banner()
            if sh[:8]=="portscan":
                try:
                    pass
                    portscanner.portscanner.shell_scan(sh[9:])
                except KeyboardInterrupt:
                    continue
            if sh=="install":
                framework_install()
    except KeyboardInterrupt:
        stop()
        exit()
if args.install:
    framework_install()

if args.version:
    Version=str(Version)
    print(Fore.GREEN+"Version: "+Version)
if args.http_server:
    http_server()

else:
    banner.banners.random_banner()
    time.sleep(0.2)
    print(Fore.RED+"please python3 file.py -h")
### <-- done --> ###
