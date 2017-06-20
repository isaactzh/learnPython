#dictionary is a bag of values
#it is like map/hashmap in Java
purse = dict()
purse['money'] = 12 #key and value
purse['candy'] = 3
purse['tissues'] = 75
print purse
purse['candy'] = purse['candy'] + 12
#dictionary does not keep the order
jjj = {'chunck':1, 'fred':42, 'jan':100}

#empty dictionary
jjj = {}

#example to count the names
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
	if name not in names:
		counts[name] = 1
	else:
		counts[name] = counts[name] + 1
print counts


#the get method for dictionary
if name in counts:
	print counts[name] #return the value
else:
	print 0 #return 0
#this is equitvalent to 
print counts.get(name, 0)



#modified count example
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
	counts[name] = counts.get(name,0) + 1
print counts


#count the pattern
counts = dict()
print 'Enter a line of text:'
line = rea_input('');

words = line.split()
print 'Words:', words

print 'Counting...'

for word in words:
	counts[word] = counts.get(word,0) + 1

print 'Counts', counts


#iterate the dictionary
counts = {...}
for key in counts: #iterate throught the key

#retrieve lists of keys and values
jjj = {'chunck':1, 'fred':42, 'jan':100}
print list(jjj)
print jjj.values()
print jjj.keys()
print jjj.items()
#two iteration variables
for aaa,bbb in jjj.items():
	print aaa,bbb



#combined example
name = raw_input("Enter file:")
handle = open(name, 'r')
text = handle.read()
words = text.split()

counts = dict()
for word in words:
	counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count

print bigword, bigcount