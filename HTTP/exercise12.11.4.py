import  urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

#ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# https://docs.python.org
url = input("Enter - ")
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('p')
count = 0
for tag in tags:
    count+=1
print(count)