from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
banner="""
 #######   #####   #####              #####   ######   #####    #    #   ######   #####   
  ##   #     #     #    #            ##   ##  #        #    #   #    #   #        #    #  
  ##         #     #    #            ##       #        #    #   #    #   #        #    #  
  ####       #     #####              #####   ####     #####     #  #    ####     #####   
  ##         #     #                      ##  #        #  #      #  #    #        #  #    
  ##         #     #                 ##   ##  #        #   #      ##     #        #   #   
 ####        #     #                  #####   ######   #    #     ##     ######   #    #  
"""
print(banner)
print("The ftp service is hosted on port 1026!")
authorizer = DummyAuthorizer()
authorizer.add_user("user", "123456", "user", perm="elradfmw")
#authorizer.add_anonymous("anonim", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 1026), handler)
server.serve_forever()