import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

p = 0
tags = soup('span')
for tag in tags:
    s = int(tag.contents[0])
    p += s
print(p)
#http://py4e-data.dr-chuck.net/comments_42.html