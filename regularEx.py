import re
^X-\S+:
1.match the start of the line
2.match any non-whitespace character
3.one or more times

Extracting data
re.findall()
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
#['2', '19', '42']

#warning greedy matching
^F.+?:
#Start with F, with any number of characters, don't be greedy and end
#with :


# \S+@\S+
# @ with non-blank characters in front of and behind

#Fine-Tuning string EXtraction:
# ^From (\S+@\S+)
#only the characters in the bracket will be return


#'@([^ ]*)'
#find @, after it, match non-blank character, "*" match many of them
#"^" everything but
#[^ ] everything but blank

#example code
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
	line = line.rstrip()
	stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+', line) # . period,    + one or more times
	if len(stuff) != 1 : continue
	num = float(stuff[0])
	numlist.append(num)
print('Maximum: ', max(numlist))