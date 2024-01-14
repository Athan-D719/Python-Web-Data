import json

data = '''
[  
  { "id" : "001",  
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",  
    "x" : "7",
    "name" : "Brent"
  },
  "email" : {
     "hide" : "yes"
   }
]'''

info = json.loads(data)
print('User count:', len(info)) #User count: 2, because is a list
                                #of dictionaries
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
    print('Hide:', info["email"]["hide"])
