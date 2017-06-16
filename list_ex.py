#ex
fridends = ['Joseph', 'Glenn', 'Sally']
carryon = ['socks', 'waterbottle', 'lalal']
#the item in the list can be in different type
#there can be a list in a list
####
for i in [5, 4, 3, 2, 1]:
	print i

#List are 'mutable'- we can change an elelment of a list using the index operator

#range function: return a list of numbers that range from zero to one less than the parameter

for i in range(len(friends)):
	friends = friends[i]
	print 'Happy New Year:', friends
#concatenating lists using "+"
#lists can be sliced using ":"
#t[1:3] slice the list using the index

stuff = list() #construct an empty list
stuff.append('book')
stuff.append(99)

#is something is a list?
some = [1, 9, 21, 10]
#9 in some: return the boolean value

#sort the list
friends.sort()

#more functions
nums = [2, 3, 4 ,1 ,3]
len(nums)
max(nums)
min(nums)
sum(nums)
sum(nums)/len(nums)

#example: calculate the average value of the inputs
total = 0
count = 0
while True:
	inp = raw_input('Enter a number:')
	if inp == 'done':break
	value = float(inp)
	total = total + value
	count = count + 1
average = total/count
print 'Average:', average

#using the list
numlist = list()
while True:
	inp = raw_input('Enter a number:')
	if inp == 'done': break
	value = float(inp)
	numlist.append(value)
average = sum(numlist) / len(numlist) 
print 'Average:', average


###strings and lists
abc = 'With three words'
stuff = abc.split()
#stuff contains seperate word in the list
#['With', 'three', 'words']
#can split with the special character
line = 'first:second:third'
thing = line.split(':')




#example, handle a file
#"From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if not line.startswith('From'): continue
	words = line.split()
	print words[2]
