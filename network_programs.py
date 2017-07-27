#transport control protocol
#port 80 is the web server
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #makes the doorway
mysock.connect(('data.pr4e.org', 80)) #80 is the port, socket connect to the server


#hypertext transfer protocol HTTP:
#allow browsers to retrieve web documents from servers over the internet
#application protocols: mail, world wide web
#protocol + host + document


#continue..
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode() 
mysock.send(cmd) #send something to the server

while True:
	data = mysock.recv(512)
	if (len(data) < 1): #end of transmission
		break
	print(data.decode()) #decode to uni-code
mysock.close()