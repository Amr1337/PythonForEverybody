'''Change your socket program so that it counts the number
of characters it has received and stops displaying any text after it has
shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count
of the number of characters at the end of the document.'''
#  http://data.pr4e.org/romeo.txt
import socket
usr_url = input('Enter - ')
try:
    HOST = usr_url.split("/")[2]
    # print(HOST)
except:
    print("Valid url")
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, 80))
cmd = 'GET ' + usr_url + ' HTTP/1.0\r\n\r\n'
# print(cmd)
ecmd = cmd.encode()
mysock.send(ecmd)

count = 0
while True:
    data = mysock.recv(512)
    count += len(data)
    if len(data) <1 or count >= 3000:break
    print(data.decode(), end='')
print(count)
mysock.close()