fhand = open('test.txt')
for line in fhand:
	line = line.rstrip() #remove the blank
	if not '@uct.ac.za' in line:
		continue
	print line




#########################
fname = raw_input('Enter the file name')
try:
	fhand = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()
count = 0
for line in fhand:
	if line.startswith('Subject:'):
		count = count + 1
print 'There were', count, 'subject lines in', fname



###########################
fname = raw_input("Enter file name: ")
fh = open(fname)
x = fh.read();
x = x.rstrip();
x = x.upper()
print x;



#########################3
# Use the file name mbox-short.txt as the file name
count = 0;
total = 0
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    pos = line.find(':')
    num = float(line[pos + 1: ])
    total = total + num
print "Average spam confidence:", total/count
