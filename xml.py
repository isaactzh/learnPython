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