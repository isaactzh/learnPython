#using urllib in python
#library that does all the socket work for us and makes web pages look like a file
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

fhand = urllib.request.urlopen('http://data.pr4e.org/remeo.txt') #return a file handle
for line in fhand:
	print(line.decode().strip())


#example below
fhand = urllib.request.urlopen('http://data.pr4e.org/remeo.txt')
counts = dict()
for line in fhand:
	words = line.decode().split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1
print(counts)


#web scraping, spidering web 
#from bs4 import BeautifulSoup
url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup =  BeautifulSoup(html, 'html.parser') #clean up the nasty html

#Retrieve all of the anchor tags
tags = soup('a') #
for tag in tags:
	print(tag.get('href', None))

#example for beautifulsoup

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input('Enter count: ')
position = input('Enter position')
for i in range(int(count)):
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	num = 0
	tags = soup('a')
	for tag in tags:
		num = num + 1
		if num == int(position):
			url = tag.get('href', None)
			print(url)