import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    #print(parms)
    url = serviceurl + urllib.parse.urlencode(parms) #address=12&key=42
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    #print(data)
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)
'''Enter location: Ann Arbot
Retrieving http://py4e-data.dr-chuck.net/xml?address=Ann+Arbot&key=42
Retrieved 1559 characters
<?xml version="1.0" encoding="UTF-8"?>
<GeocodeResponse>
 <status>OK</status>
 <result>
  <type>locality</type>
  <type>political</type>
  <formatted_address>Ann Arbor, MI, USA</formatted_address>
  <address_component>
   <long_name>Ann Arbor</long_name>
   <short_name>Ann Arbor</short_name>
   <type>locality</type>
   <type>political</type>
  </address_component>
  <address_component>
   <long_name>Washtenaw County</long_name>
   <short_name>Washtenaw County</short_name>
   <type>administrative_area_level_2</type>
   <type>political</type>
  </address_component>
  <address_component>
   <long_name>Michigan</long_name>
   <short_name>MI</short_name>
   <type>administrative_area_level_1</type>
   <type>political</type>
  </address_component>
  <address_component>
   <long_name>United States</long_name>
   <short_name>US</short_name>
   <type>country</type>
   <type>political</type>
  </address_component>
  <geometry>
   <location>
    <lat>42.2808256</lat>
    <lng>-83.7430378</lng>
   </location>
   <location_type>APPROXIMATE</location_type>
   <viewport>
    <southwest>
     <lat>42.2226680</lat>
     <lng>-83.7995720</lng>
    </southwest>
    <northeast>
     <lat>42.3239728</lat>
     <lng>-83.6758069</lng>
    </northeast>
   </viewport>
   <bounds>
    <southwest>
     <lat>42.2226680</lat>
     <lng>-83.7995720</lng>
    </southwest>
    <northeast>
     <lat>42.3239728</lat>
     <lng>-83.6758069</lng>
    </northeast>
   </bounds>
  </geometry>
  <place_id>ChIJMx9D1A2wPIgR4rXIhkb5Cds</place_id>
 </result>
</GeocodeResponse>

lat 42.2808256 lng -83.7430378
Ann Arbor, MI, USA'''