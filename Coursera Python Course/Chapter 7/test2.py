fhand = open('mbox.txt')

for line in fhand:
	line = line.rstrip() #take out the newline character '\n'
	if not '@uct.ac.za' in line:
		continue
	print line