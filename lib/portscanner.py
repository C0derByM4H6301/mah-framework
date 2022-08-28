#-*-coding:utf8;-*-
import socket
import os
import random
DEFAULT_TIMEOUT = 0.5
SUCCESS = 0
def check_port(*host_port, timeout=DEFAULT_TIMEOUT):
    sock = socket.socket()
    sock.settimeout(timeout)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connected = sock.connect_ex(host_port) is SUCCESS
    sock.close()
    return connected
banner="""
 ██████   ██████           █████                  █████████                               
░░██████ ██████           ░░███                  ███░░░░░███                              
 ░███░█████░███   ██████   ░███████             ░███    ░░░   ██████   ██████   ████████  
 ░███░░███ ░███  ░░░░░███  ░███░░███  ██████████░░█████████  ███░░███ ░░░░░███ ░░███░░███ 
 ░███ ░░░  ░███   ███████  ░███ ░███ ░░░░░░░░░░  ░░░░░░░░███░███ ░░░   ███████  ░███ ░███ 
 ░███      ░███  ███░░███  ░███ ░███             ███    ░███░███  ███ ███░░███  ░███ ░███ 
 █████     █████░░████████ ████ █████           ░░█████████ ░░██████ ░░████████ ████ █████
░░░░░     ░░░░░  ░░░░░░░░ ░░░░ ░░░░░             ░░░░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░ ░░░░░ 
                                                                                          
                                                                                          
                                                                                          """
banner1="""
███╗   ███╗ █████╗ ██╗  ██╗      ███████╗ ██████╗ █████╗ ███╗   ██╗
████╗ ████║██╔══██╗██║  ██║      ██╔════╝██╔════╝██╔══██╗████╗  ██║
██╔████╔██║███████║███████║█████╗███████╗██║     ███████║██╔██╗ ██║
██║╚██╔╝██║██╔══██║██╔══██║╚════╝╚════██║██║     ██╔══██║██║╚██╗██║
██║ ╚═╝ ██║██║  ██║██║  ██║      ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝      ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                   
"""
#con = check_port('www.google.com', 83)
#print(con)
class portscanner:
    def check(port):
        if port==str(port):
            print("please type integer")
        if port==int(port):
            if port== 7 :
                print(port, ": Service 'ECHO'?")    
            if port== 19 :
                print(port, ": Service 'CHARGEN'?")    
            if port== 20:
                print(port, ": Service 'FTP'?")
            if port == 21:
                print(port, ": Service 'FTP'?")    
            if port== 22:
                print(port, ": Service 'SSH / SCP'?")     
            if port== 23:
                print(port, ": Service 'TELNET'?")    
            if port== 25:
                print(port, ": Service 'SMTP'?")     
            if port== 42 :
                print(port, ": Service 'WINS Replication'?")    
            if port== 43 :
                print(port, ": Service 'WHOIS'?") 
            if port== 49:
                print(port, ": Service 'TACACS'?")
            if port== 53:
                print(port, ": Service 'DNS '?")
            if port== 67:
                print(port, ": Service 'DHCP / BOOTP'?")
            if port== 68:
                print(port, ": Service 'DHCP / BOOTP'?")
            if port== 69:
                print(port, ": Service 'TFTP'?")
            if port== 70:
                print(port, ": Service 'GOPHER'?")
            if port== 79:
                print(port, ": Service 'FINGER'?")
            if port== 80:
                print(port, ": Service 'HTTP'?")
            if port== 88:
                print(port, ": Service 'KERBEROS'?")
            if port== 102:
                print(port, ": Service 'MS EXCHANGE'?")
            if port== 110:
                print(port, ": Service 'POP3'?")
            if port== 113:
                print(port, ": Service 'Ident'?")
            if port== 119:
                print(port, ": Service 'NNTP (Usenet)'?")
            if port== 123:
                print(port, ": Service 'NTP'?")
            if port== 135:
                print(port, ": Service 'MICROSOFT RPC'?")
            if port== 137:
                print(port, ": Service 'NETBIOS'?")
            if port== 138:
                print(port, ": Service 'NETBIOS'?")
            if port== 139:
                print(port, ": Service 'NETBIOS'?")
            if port== 143:
                print(port, ": Service 'IMAP4'?")
            if port== 161:
                print(port, ": Service 'SNMP'?")
            if port== 162:
                print(port, ": Service 'SNMP'?")
            if port== 177:
                print(port, ": Service 'XDMCP'?")
            if port== 179:
                print(port, ": Service 'BGP'?")
            if port== 201:
                print(port, ": Service 'APPLETALK'?")
            if port== 264:
                print(port, ": Service 'BGMP'?")
            if port== 318:
                print(port, ": Service 'TSP'?")
            if port== 381:
                print(port, ": Service 'HP OPENVIEW'?")
            if port== 382:
                print(port, ": Service 'HP OPENVIEW'?")
            if port== 383:
                print(port, ": Service 'HP OPENVIEW'?")
            if port== 389:
                print(port, ": Service 'LDAP'?")
            if port== 411:
                print(port, ": Service 'DIRECT CONNECT'?")
            if port== 412:
                print(port, ": Service 'DIRECT CONNECT'?")
            if port== 443:
                print(port, ": Service 'HTTP OVER SSL / SSL'?")
            if port== 445:
                print(port, ": Service 'MICROSOFT DS'?")
            if port== 464:
                print(port, ": Service 'KERBEROS'?")
            if port== 465:
                print(port, ": Service 'SMTP OVER SSL'?")
            if port== 497:
                print(port, ": Service 'RETROSPECT'?")
            if port== 500:
                print(port, ": Service 'ISAKMP'?")
            if port== 512:
                print(port, ": Service 'rexec'?")
            if port== 513:
                print(port, ": Service 'rlogin'?")
            if port== 514:
                print(port, ": Service 'syslog'?")
            if port== 515:
                print(port, ": Service 'LPD'?")
            if port== 520:
                print(port, ": Service 'RIP'?")
            if port== 521:
                print(port, ": Service 'RIPng (IPv6)'?")
            if port== 540:
                print(port, ": Service 'UUCP'?")
            if port== 554:
                print(port, ": Service 'RTSP'?")
            if port== 546:
                print(port, ": Service 'DHCPv6'?")
            if port== 547:
                print(port, ": Service 'DHCPv6'?")
            if port== 560:
                print(port, ": Service 'rmonitor'?")
            if port== 563:
                print(port, ": Service 'NNTP OVER SSL'?")
            if port== 587:
                print(port, ": Service 'SMTP'?")
            if port== 591:
                print(port, ": Service 'FileMaker'?")
            if port== 593:
                print(port, ": Service 'Microsoft DCOM'?")
            if port== 631:
                print(port, ": Service 'Internet Printing'?")
            if port== 636:
                print(port, ": Service 'LDAP OVER SSL'?")
            if port== 639:
                print(port, ": Service 'MSDP (PIM)'?")
            if port== 646:
                print(port, ": Service 'LDP (MPLS)'?")
            if port== 691:
                print(port, ": Service 'MS EXCHANGE'?")
            if port== 860:
                print(port, ": Service 'iSCSI'?")
            if port== 873:
                print(port, ": Service 'rsync'?")
            if port== 902:
                print(port, ": Service 'VMware Server'?")
            if port== 989:
                print(port, ": Service 'FTP OVER SSL'?")
            if port== 990:
                print(port, ": Service 'FTP OVER SSL'?")
            if port== 993:
                print(port, ": Service 'IMAP4 OVER SSL'?")
            if port== 995:
                print(port, ": Service 'POP3 OVER SSL'?")
            if port== 1025:
                print(port, ": Service 'Microsoft RPC'?")
            if port== 1026:
                print(port, ": Service 'Windows Messenger'?")
            if port== 1027:
                print(port, ": Service 'Windows Messenger'?")
            if port== 1028:
                print(port, ": Service 'Windows Messenger'?")
            if port== 1029:
                print(port, ": Service 'Windows Messenger'?")
            if port== 1080:
                print(port, ": Service 'SOCKS PROXY' or 'MyDoom'?")
            if port== 1194:
                print(port, ": Service 'OpenVPN'?")
            if port== 1214:
                print(port, ": Service 'KAZAA'?")
            if port== 1241:
                print(port, ": Service 'Nessus'?")
            if port== 1311:
                print(port, ": Service 'Dell OpenManage'?")
            if port== 1433:
                print(port, ": Service 'WASTE'?")
            if port== 1432:
                print(port, ": Service 'Microsoft SQL'?")
            if port== 1512:
                print(port, ": Service 'WINS'?")
            if port== 1589:
                print(port, ": Service 'Cisco VQP'?")
            if port== 1701:
                print(port, ": Service 'L2TP'?")
            if port== 1723:
                print(port, ": Service 'MS PPTP'?")
            if port== 1725:
                print(port, ": Service 'STEAM'?")
            if port== 1741:
                print(port, ": Service 'CiscoWorks 2000'?")
            if port== 1755:
                print(port, ": Service 'MS MEDIA SERVER'?")
            if port== 1812:
                print(port, ": Service 'RADIUS'?")
            if port== 1813:
                print(port, ": Service 'RADIUS'?")
            if port== 1863:
                print(port, ": Service 'MSN'?")
            if port== 1985:
                print(port, ": Service 'Cisco HSRP'?")
            if port== 2000:
                print(port, ": Service 'Cisco SCCP'?")
            if port== 2002:
                print(port, ": Service 'Cisco ACS'?")
            if port== 2049:
                print(port, ": Service 'NFS'?")
            if port== 2082:
                print(port, ": Service 'cPanel'?")
            if port== 2083:
                print(port, ": Service 'cPanel'?")
            if port== 2100:
                print(port, ": Service 'Oracle XDB'?")
            if port== 2222:
                print(port, ": Service 'DirectAdmin'?")
            if port== 2302:
                print(port, ": Service 'HALO'?")
            if port== 2483:
                print(port, ": Service 'Oracle DB'?")
            if port== 2484:
                print(port, ": Service 'Oracle DB'?")
            if port== 2745:
                print(port, ": Service 'BAGLE.H'?")
            if port== 2967:
                print(port, ": Service 'Symantec AV'?")
            if port== 3050:
                print(port, ": Service 'Interbase DB'?")
            if port== 3074:
                print(port, ": Service 'XBOX LIVE'?")
            if port== 3124:
                print(port, ": Service 'HTTP Proxy'?")
            if port== 3127:
                print(port, ": Service 'MYDOOM'?")
            if port== 3128:
                print(port, ": Service 'HTTP Proxy'?")
            if port== 3222:
                print(port, ": Service 'GLBP'?")
            if port== 3260:
                print(port, ": Service 'iSCSI Target'?")
            if port== 3306:
                print(port, ": Service 'MySQL'?")
            if port== 3389:
                print(port, ": Service 'Terminal Server'?")
            if port== 3689:
                print(port, ": Service 'iTunes'?")
            if port== 3690:
                print(port, ": Service 'Subversion'?")
            if port== 3724:
                print(port, ": Service 'World Of Warcraft'?")
            if port== 3784:
                print(port, ": Service 'Ventrilo'?")
            if port== 3785:
                print(port, ": Service 'Ventrilo'?")
            if port== 4333:
                print(port, ": Service 'mSQL'?")
            if port== 4444:
                print(port, ": Service 'BLASTER'?")        
            if port== 4664:
                print(port, ": Service 'Google Desktop'?")
            if port== 4672:
                print(port, ": Service 'EMULE'?")
            if port== 4899:
                print(port, ": Service 'Radmin'?")
            if port== 5000:
                print(port, ": Service 'UPnP'?")
            if port== 5001:
                print(port, ": Service 'Slingbox' or 'iperf' ?")
            if port== 5004:
                print(port, ": Service 'RTP'?")
            if port== 5005:
                print(port, ": Service 'RTP'?")
            if port== 5050:
                print(port, ": Service 'YAHOO! MESSENGER'?")
            if port== 5060:
                print(port, ": Service 'SIP'?")
            if port== 5190:
                print(port, ": Service 'AIM / ICQ'?")
            if port== 5222:
                print(port, ": Service 'XMPP / JABBER'?")
            if port== 5223:
                print(port, ": Service 'XMPP / JABBER'?")
            if port== 5432:
                print(port, ": Service 'PostgreSQL'?")
            if port== 5500:
                print(port, ": Service 'VNC Server'?")
            if port== 5554:
                print(port, ": Service 'SASSER'?")
            if port== 5631:
                print(port, ": Service 'pcAnywhere'?")
            if port== 5632:
                print(port, ": Service 'pcAnywhere'?")
            if port== 5800:
                print(port, ": Service 'VNC over HTTP'?")
            if  port >5900  and port < 6000:
                print(port, ": Service 'VNC over HTTP'?")
            if port== 6000:
                print(port, ": Service 'X11'?")
            if port== 6001:
                print(port, ": Service 'X11'?")
            if port== 6112:
                print(port, ": Service 'BATTLE.NET'?")
            if port== 6129:
                print(port, ": Service 'DameWare'?")
            if port== 6257:
                print(port, ": Service 'WINMX'?")
            if port== 6346:
                print(port, ": Service 'GNUTELLA'?")
            if port== 6347:
                print(port, ": Service 'GNUTELLA'?")
            if port== 6500:
                print(port, ": Service 'GAMESPY ARCADE'?")
            if port== 6566:
                print(port, ": Service 'SANE'?")
            if port== 6588:
                print(port, ": Service 'AnalogX'?")
            if port== 6665:
                print(port, ": Service 'IRC'?")
            if port== 6666:
                print(port, ": Service 'IRC'?")
            if port== 6667:
                print(port, ": Service 'IRC'?")
            if port== 6668:
                print(port, ": Service 'IRC'?")
            if port== 6669:
                print(port, ": Service 'IRC'?")
            if port== 6679:
                print(port, ": Service 'IRC OVER SSL'?")
            if port== 6697:
                print(port, ": Service 'IRC OVER SSL'?")
            if port== 6699:
                print(port, ": Service 'NAPSTER'?")
            if port== 6881:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6882:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6883:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6884:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6885:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6886:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6887:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6888:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6889:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6890:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6891:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6892:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6893:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6894:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6895:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6896:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6897:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6898:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6899:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6900:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6901:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6902:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6903:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6904:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6905:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6906:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6907:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6908:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6909:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6910:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6911:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6912:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6913:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6914:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6915:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6916:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6917:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6918:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6919:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6920:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6921:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6922:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6923:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6924:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6925:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6926:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6927:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6928:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6929:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6930:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6931:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6932:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6933:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6934:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6935:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6936:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6937:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6938:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6939:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6940:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6941:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6942:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6943:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6944:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6945:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6946:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6947:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6948:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6949:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6950:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6951:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6952:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6953:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6954:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6955:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6956:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6957:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6958:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6959:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6960:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6961:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6962:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6963:
                print(port, ": Service 'BITTORRENT'?")
            if port==6964:     
                print(port, ": Service 'BITTORRENT'?")
            if port==6965:     
                print(port, ": Service 'BITTORRENT'?")
            if port==6966:     
                print(port, ": Service 'BITTORRENT'?")
            if port==6967:     
                print(port, ": Service 'BITTORRENT'?")
            if port==6968:     
                print(port, ": Service 'BITTORRENT'?")
            if port==6969:     
                print(port, ": Service 'BITTORRENT'?")
            if port==6970:
                print(port, ": Service 'BITTORRENT'?")
            if port==6971:
                print(port, ": Service 'BITTORRENT'?")
            if port==6972:
                print(port, ": Service 'BITTORRENT'?")
            if port==6973:
                print(port, ": Service 'BITTORRENT'?")
            if port==6974:
                print(port, ": Service 'BITTORRENT'?")
            if port==6975:
                print(port, ": Service 'BITTORRENT'?")
            if port==6976:
                print(port, ": Service 'BITTORRENT'?")
            if port==6977:
                print(port, ": Service 'BITTORRENT'?")
            if port==6978:
                print(port, ": Service 'BITTORRENT'?")
            if port==6979:
                print(port, ": Service 'BITTORRENT'?")
            if port==6980:
                print(port, ": Service 'BITTORRENT'?")
            if port==6981:
                print(port, ": Service 'BITTORRENT'?")
            if port==6982:
                print(port, ": Service 'BITTORRENT'?")
            if port==6983:
                print(port, ": Service 'BITTORRENT'?")
            if port==6984:
                print(port, ": Service 'BITTORRENT'?")
            if port==6985:
                print(port, ": Service 'BITTORRENT'?")
            if port==6986:
                print(port, ": Service 'BITTORRENT'?")
            if port==6987:
                print(port, ": Service 'BITTORRENT'?")
            if port==6988:
                print(port, ": Service 'BITTORRENT'?")
            if port==6989:
                print(port, ": Service 'BITTORRENT'?")
            if port==6990:
                print(port, ": Service 'BITTORRENT'?")
            if port==6991:
                print(port, ": Service 'BITTORRENT'?")
            if port==6992:
                print(port, ": Service 'BITTORRENT'?")
            if port==6993:
                print(port, ": Service 'BITTORRENT'?")
            if port==6994:
                print(port, ": Service 'BITTORRENT'?")
            if port==6995:
                print(port, ": Service 'BITTORRENT'?")
            if port==6996:
                print(port, ": Service 'BITTORRENT'?")
            if port==6997:
                print(port, ": Service 'BITTORRENT'?")
            if port==6998:
                print(port, ": Service 'BITTORRENT'?")
            if port==6999:
                print(port, ": Service 'BITTORRENT'?")
            if port== 6891:
                print(port, ": Service 'WINDOWS LIVE'?")
            if port== 6892:
                print(port, ": Service 'WINDOWS LIVE'?")
            if port== 6893:
                print(port, ": Service 'WINDOWS LIVE'?")
            if port== 6894:
                print(port, ": Service 'WINDOWS LIVE'?")
            if port== 6895:
                print(port, ": Service 'WINDOWS LIVE'?")
            if port== 6896:
                print(port, ": Service 'WINDOWS LIVE'?")
            if port== 6897:
                print(port, ": Service 'WINDOWS LIVE'?")
            if port== 6898:
                print(port, ": Service 'WINDOWS LIVE'?")
            if port== 6899:
                print(port, ": Service 'WINDOWS LIVE'?")
            if port== 6900:
                print(port, ": Service 'WINDOWS LIVE'?")
            if port== 6901:
                print(port, ": Service 'WINDOWS LIVE'?")
            if port== 6970:
                print(port, ": Service 'Quicktime'?")
            if port== 7212:
                print(port, ": Service 'GhostSurf'?")
            if port== 7648:
                print(port, ": Service 'CU-SEEME'?")
            if port== 6649:
                print(port, ": Service 'CU-SEEME'?")
            if port== 8000:
                print(port, ": Service 'Internet Radio'?")
            if port== 8080:
                print(port, ": Service 'HTTP Proxy'?")
            if port== 8086:
                print(port, ": Service 'Kaspersky AV'?")
            if port== 8087:
                print(port, ": Service 'Kaspersky AV'?")
            if port== 8118:
                print(port, ": Service 'Peivoxy'?")
            if port== 8200:
                print(port, ": Service 'VMware Server'?")
            if port== 8500:
                print(port, ": Service 'Adobe ColdFusion'?")
            if port== 8767:
                print(port, ": Service 'TEAMSPEAK'?")
            if port== 8866:
                print(port, ": Service 'BAGLE.B'?")
            if port== 9100:
                print(port, ": Service 'HP JetDirect'?")
            if port== 9101:
                print(port, ": Service 'Bacula'?")
            if port== 9102:
                print(port, ": Service 'Bacula'?")
            if port== 9103:
                print(port, ": Service 'Bacula'?")
            if port== 9119:
                print(port, ": Service 'MXIT'?")
            if port== 9800:
                print(port, ": Service 'WebDAV'?")
            if port== 9898:
                print(port, ": Service 'DABBER'?")
            if port== 9988:
                print(port, ": Service 'RBOT / SPYBOT'?")
            if port== 9999:
                print(port, ": Service 'Urchin'?")
            if port== 10000:
                print(port, ": Service 'Webmin' or 'BackupExec'?")
            if port== 10113:
                print(port, ": Service 'NetIQ'?")
            if port== 10114:
                print(port, ": Service 'NetIQ'?")
            if port== 10115:
                print(port, ": Service 'NetIQ'?")
            if port== 10116:
                print(port, ": Service 'NetIQ'?")
            if port== 11371:
                print(port, ": Service 'OpenPGP'?")
            if port== 12035:
                print(port, ": Service 'SECOND LIFE'?")
            if port== 12036:
                print(port, ": Service 'SECOND LIFE'?")
            if port== 12345:
                print(port, ": Service 'NETBUS'?")
            if port== 13720:
                print(port, ": Service 'Netbackup'?")
            if port== 13721:
                print(port, ": Service 'NetBackup'?")
            if port== 14567:
                print(port, ": Service 'BATTLE FIELD'?")
            if port== 15118:
                print(port, ": Service 'DIPNET / ODDP'?")
            if port== 19226:
                print(port, ": Service 'AdminSecure'?")
            if port== 19638:
                print(port, ": Service 'Ensim'?")
            if port== 20000:
                print(port, ": Service 'Usermin'?")
            if port== 24800:
                print(port, ": Service 'Synergy'?")
            if port== 25999:
                print(port, ": Service 'XFIRE'?")
            if port== 27015:
                print(port, ": Service 'HALF-LIFE'?")
            if port== 27374:
                print(port, ": Service 'SUB7'?")
            if port== 28960:
                print(port, ": Service 'CAL OF DUTY'?")
            if port== 31337:
                print(port, ": Service 'BACKORIFICE'?")
            if port >  33433:
                print(port, ": Service 'traceroute'?")    
    def scan(ip):
        number=random.randint(1,2)
        if number==1:
            print(banner)
        if number==2:
            print(banner1)
        try:
            print("use CTRL+C for exit")
            for i in range(0,65536):
                on = check_port(ip, i)
                if on == True:
                    print("port: ",i," open")
                    milfscan.check(i)
        except KeyboardInterrupt:
            exit("ctrl+c detected")
    def shell_scan(ip):
        number=random.randint(1,2)
        if number==1:
            print(banner)
        if number==2:
            print(banner1)
        try:
            print("use CTRL+C for exit")
            for i in range(0,65536):
                on = check_port(ip, i)
                if on == True:
                    print("port: ",i," open")
                    milfscan.check(i)
        except KeyboardInterrupt:
            pass
