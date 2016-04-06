# 7.1 Write a program that prompts for a file name, then opens that file 
# and reads through the file, and print the contents of the file in upper 
# case. Use the file words.txt to produce the output below.
# You can download the sample data at 
# http://www.pythonlearn.com/code/words.txt

fname = raw_input('Enter a file name: ')

try:
	fhand = open(fname)
except:
	print 'There was an error with the file: ', fname
	exit()

for line in fhand:
	print line.rstrip().upper()