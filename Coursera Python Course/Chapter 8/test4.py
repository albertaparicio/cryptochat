# Find the day a mail was sent, by analysing the header.

fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if not line.startswith('From'): continue
	words = line.split()
	try:
		print words[2]
	except:
		continue