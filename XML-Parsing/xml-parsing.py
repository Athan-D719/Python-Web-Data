import xml.etree.ElementTree as ET #ET Alias

data = '''<person> 
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''
#triple quoted string, potential multiline string

tree = ET.fromstring(data) #parsing in an object
print('Name:',tree.find('name').text) #getting the text inside
print('Attr:', tree.find('email').get('hide')) #get hide attr within     the tag 'email'
#Name: Chuck
#Attr: yes
#################################################################
import xml.etree.ElementTree as ET

input='''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user') #defines sons #.//comment
print('User input:', len(lst))
for item in lst: #for each sun...
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text)
    print('Attribute:', item.get("x"))
#User input: 2
#Name: Chuck
#Id: 001
#Attribute: 2
#Name: Brent
#Id: 009
#Attribute: 7
###################################################################



