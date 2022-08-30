import http.server
import socketserver
banner="""
  __  __           _               _____                                                               _    
 |  \/  |   __ _  | |__           |  ___|  _ __    __ _   _ __ ___     ___  __      __   ___    _ __  | | __
 | |\/| |  / _` | | '_ \   _____  | |_    | '__|  / _` | | '_ ` _ \   / _ \ \ \ /\ / /  / _ \  | '__| | |/ /
 | |  | | | (_| | | | | | |_____| |  _|   | |    | (_| | | | | | | | |  __/  \ V  V /  | (_) | | |    |   < 
 |_|  |_|  \__,_| |_| |_|         |_|     |_|     \__,_| |_| |_| |_|  \___|   \_/\_/    \___/  |_|    |_|\_\
                                                                                                            """
print(banner)
print("http://127.0.0.1:8080/index.html")
PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()