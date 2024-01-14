import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

a = 0
url='http://py4e-data.dr-chuck.net/comments_592389.xml'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('Retreiving', url)
sup = urllib.request.urlopen(url, context=ctx)
data = sup.read()
print('Retreiving:', len(data), 'Characters.')
tree = ET.fromstring(data)

lst = tree.findall('.//comment')
for item in lst:
    c = int(item.find('count').text)
    a +=c
print(a)
#Adding the numbres founf in .//comment.(2511)