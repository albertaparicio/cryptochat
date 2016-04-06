# -*- coding: utf-8 -*-
# stablish a connection and load a web file, but even faster
import urllib
web = raw_input('Enter the web URL: http://www.')
fhand = urllib.urlopen('http://www.'+web)

# create dictionary and store word frequency
counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word,0) + 1

# Copy the content of the dictionary into a new created list
tmp = list()
for key, value in counts.items():
	tmp.append((value,key))

# order the content
tmp.sort(reverse=True)

# Display 10 most frequent values
for val, key in tmp[:10]:
	print key, val