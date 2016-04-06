# The ten most common words 
fhand = open('romeo.txt')
counts = dict()

for line in fhand:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word,0) + 1

# Now sort

# create temporary list
tmp = list()
for key,value in counts.items():
	tmp.append((value, key))

# sort list
tmp.sort(reverse=True)

for val, key in tmp[:10]:
	print key, val