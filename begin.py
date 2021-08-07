#!/usr/bin/env python3
import requests
import socket

def check_localhost():
    localhost = socket.gethostbyname('localhost')
#    print(localhost)
    return localhost == "127.0.0.1"
def check_connectivity():
    request = requests.get("http://www.google.com")
 #   print(request)
    return request.status_code == 200
#print(check_localhost())
#print(check_connectivity())
