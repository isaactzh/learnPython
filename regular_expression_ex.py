import re
hand = open('regex_sum_5758.txt')
numlist = list()
for line in hand:
	line = line.rstrip()
	stuff = re.findall('[0-9]+', line)
	for each in stuff:
		numlist.append(int(each))
print(sum(numlist))
