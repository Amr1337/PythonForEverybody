import urllib.request, urllib.error, urllib.parse
'''
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover.jpg','wb')
fhand.write(img)
fhand.close()'''

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size += len(info)
    fhand.write(info)
print(size, 'charcters copied!')
fhand.close()