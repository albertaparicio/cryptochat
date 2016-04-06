name = raw_input('Enter a file name: ')
fhand = open(name)
# text = handle.read()

for line in fhand:
	if line.startswith('From'):
		print line.rstrip()
	#print line
	#words = line.split()
	#print words[1]
	#counts[words[1]] = counts.get(words[1],0) + 1

#mail_max = 0
#for mail in counts:
#	if mail > mail_max:
#		mail_max = mail


#print mail_max, counts[mail_max]