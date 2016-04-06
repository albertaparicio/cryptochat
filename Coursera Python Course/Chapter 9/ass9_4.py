# 9.4 Write a program to read through the mbox-short.txt and figure 
# out who has the sent the greatest number of mail messages. The 
# program looks for 'From ' lines and takes the second word of those 
# lines as the person who sent the mail. The program creates a Python
# dictionary that maps the sender's mail address to a count of the 
# number of times they appear in the file. After the dictionary is 
# produced, the program reads through the dictionary using a maximum 
# loop to find the most prolific committer.


# Propmt for a file name and open it
name = raw_input('Enter a file name: ')
fhand = open(name)

# Create the dictionary for the mails and its counting
counts = dict()

# Examine the text, analyze the lines stating with "From " and 
# storing the second word appearences (the mail)
for line in fhand:
	if not line.startswith('From '):
		continue
	words = line.split()
	counts[words[1]] = counts.get(words[1],0) + 1

# Find the maximum value using a for loop
bigword = None
bigcount = None

for word,count in counts.items():
	if bigword is None or count > bigcount:
		bigword = word
		bigcount = counts[word]

print bigword, bigcount