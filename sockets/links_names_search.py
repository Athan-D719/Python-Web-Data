import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Robby.html'
pos = (int(input('Enter the name position: '))- 1)
t = int(input('Enter the times this will happen: '))
for i in range(t): 
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    #inp = int(input('Enter number of times: '))
    li = list()
    tags = soup('a')
    for tag in tags:
        ind = tag.get('href', None)
        li.append(ind)
    url = li[pos]
    name = re.findall('_by_([^.]*)', url)
    print(name)
    