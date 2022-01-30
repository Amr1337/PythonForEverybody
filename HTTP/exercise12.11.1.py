''' Change the socket program socket1.py to prompt the user
for the URL so it can read any web page. You can use split('/') to
break the URL into its component parts so you can extract the host
name for the socket connect call. Add error checking using try and
except to handle the condition where the user enters an improperly
formatted or non-existent URL.

'''
import os
import socket
usr_url = input("Enter valid URL: ")
try:
    HOST = usr_url.split("/")[2]
    print(HOST)
except:
    print("URL is not valid")
    os.sys.exit(1)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, 80))
cmd = 'GET ' + usr_url + ' HTTP/1.0\r\n\r\n'
# print(cmd)
ecmd = cmd.encode()
mysock.send(ecmd)
while True:
    data = mysock.recv(512)
    if len(data) < 1: break
    print(data.decode(), end='')
mysock.close()