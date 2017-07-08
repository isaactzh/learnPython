#unicode characters ans Strings
#ord() function tells us the numeric value of a simple ASCII character
print(ord('H'))

#unicode: character sets
#UTF-8: 1-4 bytes
	#Upwards compatible with ASCII
	#automaticaly detected

#byte string
x = b'abc'
#byte string and regular string is different in python3
#all the strings in the python3 is default unicode

#when we talk to external resource like a network socket, we need to encode Python3 strings
#when we read data from an external resource, we must decode it based on the character set
while True:
	data = mysock.recv(512) #data is in byte here
	if(len(data) < 1):
		break
	mystring = data.decode() #decode into unicode
	print(mystring)
#encode(): make the strings into bytes
#String(Unicode) -> Bytes(UTF-8)