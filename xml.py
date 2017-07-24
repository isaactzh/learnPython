#API application program interface
#sending Data across the "Net" on some format we agree on
#serialize and de-serialize inter-media protocal, agree on a "Wire Format"


#XML- Extensible Markup Language (Serialization format)
#XML "Elements" (Nodes), tags
#purpose: share structured data
#basics: start tag, end tag, text content, attribute, self closing tag(slash)
#XML as a Tree: each tag is a node of a tree. content is a child, and attributes are other children


#XML Schema: Describing a "contract" as to what is acceptable XML
#XML Validataion: send Document and Schema Contract to the Validator
import xml.etree.ElementsTree as ET
#triple quote string
data = '''<person> 
	<name>Chuck</name>
	<phone type="intl">
		+1 734 303 4456
	</phone>
	<email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text) #attribute of the name tag
print('Attr:',tree.find('email').get('hide'))





################333
input = '''<stuff>
	<users>
		<user x = "2">
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
lst = stuff.findall('users/user') #search all the user tag under users
print('User count:', len(lst))
for item in list:
	print('Name', item.find('name').text)
	print('id', item.find('id').text)
	print('Attribute', item.get("x"))




#########3
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)



###homework example
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
while True:
    address = input('Enter location: ')
    if len(address) < 1 : break
    print('Retrieving', address)
    uh = urllib.request.urlopen(address)
    data = uh.read()
    print('Retrieved',len(data),'characters')
    print(data.decode())
    tree = ET.fromstring(data)
    lst = tree.findall('comments/comment')
    #lst = tree.findall('.//count')
    print('Count: ', len(lst))
    num = 0
    for item in lst:
        x = item.find('count').text
        num = num + int(x)
    print('Sum: ', num)
