# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution 
# by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


fhand = open("mbox-short.txt")

# Crear el diccionari

counts = dict()

for line in fhand:
	if not line.startswith("From "):
		continue
	hour = line.split()[5].split(":")[0] # Obtain the 5th word, and therefrom the hour
	counts[hour] = counts.get(hour,0) + 1

counts = sorted(counts.items())

for key, value in counts:
	print key, value
