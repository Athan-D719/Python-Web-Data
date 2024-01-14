import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

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
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data) #parses that data that came out from google(dictionaty)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK': #if theres no status key in the js dictionary...
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4)) #whole 'JSON tree'

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

    #Enter location: addres=Ann+Arbor%2C+MI  #%2C = ',', + = [space]
    #http://py4e-data.dr-chuck.net/json?address=addres%3DAnn%2BArbor%252C%2BMI&key=42


#Delete this
'''Enter location: Ann+Arbor%2C+MI       
Retrieving http://py4e-data.dr-chuck.net/json?address=Ann%2BArbor%252C%2BMI&key=42
Retrieved 3971 characters
{
    "results": [
        {
            "access_points": [
                {
                    "access_point_type": "TYPE_ESTABLISHMENT_POI",
                    "location": {
                        "latitude": 42.287771,
                        "longitude": -83.743152
                    },
                    "place_id": "ChIJZ7osZROuPIgR-Cwm6qzLODc",
                    "unsuitable_travel_modes": []
                },
                {
                    "access_point_type": "TYPE_ESTABLISHMENT_POI",
                    "location": {
                        "latitude": 42.287777,
                        "longitude": -83.7431846
                    },
                    "place_id": "ChIJh7CcqxSuPIgRz5fjlF4-YM0",
                    "unsuitable_travel_modes": []
                },
                {
                    "access_point_type": "TYPE_ESTABLISHMENT_POI",
                    "location": {
                        "latitude": 42.277951,
                        "longitude": -83.734971
                    },
                    "place_id": "ChIJmVK1kkOuPIgR3po5VxE6YMY",
                    "unsuitable_travel_modes": []
                },
                {
                    "access_point_type": "TYPE_ESTABLISHMENT_POI",
                    "location": {
                        "latitude": 42.278286,
                        "longitude": -83.747328
                    },
                    "place_id": "ChIJ5ZAuDjyuPIgRggySYwP3OnY",
                    "unsuitable_travel_modes": []
                },
                {
                    "access_point_type": "TYPE_ESTABLISHMENT_POI",
                    "location": {
                        "latitude": 42.24857,
                        "longitude": -83.74013
                    },
                    "place_id": "ChIJweM-ubivPIgRm7ugPCNqiH4",
                    "unsuitable_travel_modes": []
                },
                {
                    "access_point_type": "TYPE_SEGMENT",
                    "location": {
                        "latitude": 42.2808266,
                        "longitude": -83.7430619
                    },
                    "location_on_segment": {
                        "latitude": 42.28083,
                        "longitude": -83.7431469
                    },
                    "place_id": "ChIJS18IsD-uPIgRlgXN58fXgBE",
                    "segment_position": 0.9970229268074036,
                    "unsuitable_travel_modes": []
                }
            ],
            "address_components": [
                {
                    "long_name": "Ann Arbor",
                    "short_name": "Ann Arbor",
                    "types": [
                        "locality",
                        "political"
                    ]
                },
                {
                    "long_name": "Washtenaw County",
                    "short_name": "Washtenaw County",
                    "types": [
                        "administrative_area_level_2",
                        "political"
                    ]
                },
                {
                    "long_name": "Michigan",
                    "short_name": "MI",
                    "types": [
                        "administrative_area_level_1",
                        "political"
                    ]
                },
                {
                    "long_name": "United States",
                    "short_name": "US",
                    "types": [
                        "country",
                        "political"
                    ]
                }
            ],
            "formatted_address": "Ann Arbor, MI, USA",
            "geometry": {
                "bounds": {
                    "northeast": {
                        "lat": 42.3239728,
                        "lng": -83.6758069
                    },
                    "southwest": {
                        "lat": 42.222668,
                        "lng": -83.799572
                    }
                },
                "location": {
                    "lat": 42.2808256,
                    "lng": -83.7430378
                },
                "location_type": "APPROXIMATE",
                "viewport": {
                    "northeast": {
                        "lat": 42.3239728,
                        "lng": -83.6758069
                    },
                    "southwest": {
                        "lat": 42.222668,
                        "lng": -83.799572
                    }
                }
            },
            "place_id": "ChIJMx9D1A2wPIgR4rXIhkb5Cds",
            "types": [
                "locality",
                "political"
            ]
        }
    ],
    "status": "OK"
}
lat 42.2808256 lng -83.7430378
Ann Arbor, MI, USA'''