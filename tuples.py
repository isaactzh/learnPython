#tuples are non-changebale list
#tuple uses parentheses
x = ('d', 'a', 's')
print x[2]

for iter in x:
	print iter

#tuples are immutable
#can not change a specific index's value (not mutable)
x = (3, 2, 1)
#can not sort, append, and reverse the tuples
l = list()
dir(1) #tell what function it has

#tuples can only use count and index method(function)

#tuples are more efficient than list

#tuples and assignment: 
(x, y) = (4 , 'fred') #two tuples
a, b = (99, 98)

# the items() method in dictionaries returns a list of (key, value) tuples

d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():
	print k, v

tups = d.items()
print tups

#tuples are comparable
(0, 1, 2000000) < (0, 3, 4)
('Jones', 'Sally') < ('Jones', 'Fred') #flase

#sort the tuples
d = {'a':10, 'b':1, 'c':22}
t = d.items()
t.sort() #sort by keys
#
t = sorted(d.items())
#sort and print the list contains the tuples
for k, v in sorted(d.items()):
	print k, v


#sort by values instead of key
d = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in d.items():
	tmp.append((v, k)) #reverse the key and value
tmp.sort(reverse = True) #sort from highest to the lowest




#print the first 10 most common value in the list
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
	lst.append((val, key))

for val, key in lst[:10]:
	print key, val

#shorter version (sorted by value), more dense python
d = {'a':10, 'b':1, 'c':22}
#list comprehension, creates a dynamic list. In this case,
#we make a lsit of reversed tuples and then sort it
print sorted ([(v, k)] for k,v in c.items())
