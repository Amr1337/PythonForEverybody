import urllib.request, urllib.error, urllib.parse
import ssl
from bs4 import BeautifulSoup

#ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#retrive all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))