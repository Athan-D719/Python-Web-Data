import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = ('https://www.internetlivestats.com/watch/internet-users/region/')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
a = list()

tags = soup('span')
for tag in tags:
    #a.append(tag.get('class', None))
    a.append(tag.contents)
    #a.append(tag.attrs)
    #
    print(a)
    #hehe = a[0]
    #jeje = re.findall('^class="internet-user-region>"([^<*])', hehe)
print(a)   #print(jeje)
    
