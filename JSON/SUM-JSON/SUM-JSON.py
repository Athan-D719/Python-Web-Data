import u rllib.request, urllib.error, urllib.parse
import json
import ssl

count = list()
num = 0

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Location: ')
connection = urllib.request.urlopen(url, context = ctx)
data = connection.read().decode()

js = json.loads(data)
#print(json.dumps(js, indent=2))
jso = js['comments']
for item in jso:
    n = item['count']
    count.append(n)
for i in range(len(count)):
    num += count[i]
print('Retreiving:',url )
print('Retrieved ', len(data), 'characters')
print('Count: ', len(count))
print('Sum: ',num)

#2333