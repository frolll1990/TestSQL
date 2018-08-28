import time
import socket
import re
#import encode
#import decode


HOST = '127.0.0.1'
PORT = 20025 #MT4
#HOST = '192.168.56.101'
#PORT = 443  #MT5

hello = print('\nQuery Script v0.01\n ')
answer = ""
while answer == "":   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    apiquery = input('Input your query. Example: "getallbalances" \n$: ')
    action = ('action=')


    s.send(action.encode()+apiquery.encode())

    received = True

    while received:
        received = s.recv(1024)
        print (received)
    
    s.close()
    answer = ''
