# mah-framework
A hub that runs software embedded as modules. Libraries and software that I wrote will exist as default modules.

## Download and installation
 
`root@kali:~# git clone https://github.com/C0derByM4H6301/mah-framework.git`

`root@kali:~# cd mah-framework`

`root@kali:~# bash install.sh`
### one line command install 
` git clone https://github.com/C0derByM4H6301/mah-framework.git && cd mah-framework && bash install.sh`
### help documentation
#### shell command
```
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
    |--> modules : prints available modules to the screen. Example: show modules
```
### argparse help
```
usage: mah-framework.py [-h] [-s] [--install] [-v] [-q] [--http-server]
                        [--portscan PORTSCAN]

options:
  -h, --help           show this help message and exit
  -s, --start          start to mah-framework
  --install            installs the necessary software for mah-framework
  -v, --version        version information
  -q, --quiet          quiet output
  --http-server        start to http server, port: 8000
  --portscan PORTSCAN  start to portscan, E.g: --portscan 127.0.0.1
     

```
## Modules
### 1. TORGHOST
Torghost software, one of the successful tools in the field of privacy and anonymity, has been added as a module for those who care about privacy.

[Torghost Github](https://github.com/SusmithKrishnan/torghost)

### 2. Portscan / Mah- Scan
Portscan port scan tool is a simple scan tool that shows open ports. It has the reflex to detect services using standard ports.
### 3. Wordlist4mah.py
In brute force attacks, the use dictionary method is mostly preferred. here is a simple wordlist tool tuned for just that.
### 4. Httpd4mah.py
text...
### 5. server2ftp4mah.py
ftp server text...
# We commemorate ancestor with respect
![alt text](https://github.com/C0derByM4H6301/mah-framework/blob/main/img/ata.jpg?raw=true)

### I like this logo
![alt text](https://github.com/C0derByM4H6301/mah-framework/blob/main/img/msf_logo.jpg)
