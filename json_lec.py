#JSON: serilization, very native to javasript
import json
data = '''{
	"name" : "Chuck",
	"phone" : {
		"tpye" : "intl"
		"number" : "+1 734 303 4456"
	},
	"email": {
		"hide" : "yes"
	}
}'''

info = json.loads(data)
print('Name:', info["name"]) #info is a dictionary
print('Hide:', info["email"]["hide"]) #info["email"] is also a dictionary

#JSON represents data as nested "lists" and "dictionaries"
import json
input = '''{
	{   "id" : "001",
	    "x" : "2",
	    "name" : "Chuck"
	},
	{	"id" : "009",
		"x" : "7",
		"name" : "Chuck"
	}
}'''

info = json.loads(input)
print('User count:', len(info))
for item in info:
	print('Name', item['name'])
	print('Id', item['id'])
	print('Attribute', item['x'])



#Json and API example
#Service Oriented Approach
#API application program interface
#service layer, help to share the data
#data interchange
#we want to know what the API is
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://map.googleapis.com/maps/apo/geocode/json?'

while True:
	address = input('Enter location: ')
	if len(address) < 1: break

	url = serviceurl + urllib.parse.urlencode({'address': address})

	print('Retrieving',url)
	uh = urllib.request.urlopen(url)
	data = uh.read().decode()
	print('Retrieving', len(data), 'characters')

	try:
		js = json.loads(data)
	except:
		js = None

	if not js or 'status' not in js or js['status'] != 'OK':
		print('====Failure To Retrieve====')
		print(data)
		continue

	lat = js["result"][0]["geometry"]["location"]["lat"]
	lng = js["result"][0]["geometry"]["location"]["lng"]
	print('lat', lat, 'lng', lng)
	location = js['result'][0]['formatted_address']
	print(location)



# hw1
import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?sensor=false&'


address = input('Enter location: ')


url = serviceurl + urllib.parse.urlencode(
    {'address': address})

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)
id = js['results'][0]['place_id']
print(id)




