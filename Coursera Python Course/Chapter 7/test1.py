handle = open('mbox.txt')
count = 0

for line in handle:
	line = line.rstrip()
	if not line.startswith('From'):
		continue

	print line
	count = count +1

print 'Line Count:',count