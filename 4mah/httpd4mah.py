import http.server
import socketserver
import argparse
banner="""
##     #   #          ##    ##               ##                 
 #     #   #           #   ###                #                 
 ###  ### ### #####  ###  ## #  ######  ###   ###    ##### ## # 
 # #   #   #   #  # #  #  #####  # # #   ##   # #     #  # #  # 
 # #   #   #   #  # #  #     #   # # #  # #   # #     #  #  ### 
#####  ##  ##  ###  #####   ### ####### ## # ##### #  ###   ##  
               #                                      #      #  
              ###                                    ###    #  
"""
print(banner)
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", type=int,default=80,help="port to http server")
parser.add_argument("-d","--directory", type=str,default=".",help="directory")
parser.add_argument("-s","--start",action="store_true",help="Start server, only if you use this, port 80 will broadcast in the directory it is in.")
args = parser.parse_args()
PORT = int(args.port)
DIRECTORY = args.directory
class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
if args.start:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
else:
    print("please:\n\t python3 http4mah.py -h")