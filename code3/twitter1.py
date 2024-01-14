import urllib.request, urllib.parse, urllib.error
import twurl
import ssl
import json
import re


# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '2'}) #number of tweets
    #print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    #print(data[:300])
    print(data)
    js = json.loads(data)
    print(json.dumps(js, indent=2))
    #text = re.findall('^text":".","*([^ ]*)', data)
    #print(text)
    fpos = data.find('ext":"')#106
    spos = data.find('","', fpos)#115
    d1 = (data[fpos+6 : spos]) 
    d2 = d1.replace('\s', 'sdas')
    #print(d2)
    print(js[0]["text"])
    headers = dict(connection.getheaders())
    # print headers
    print('Remaining', headers['x-rate-limit-remaining'])

