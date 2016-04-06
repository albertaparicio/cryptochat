# 7.2 Write a program that prompts for a file name, then opens that file 
# and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the 
# lines and compute the average of those values and produce an output as 
# shown below. Do not use the sum() function or a variable named sum in 
# your solution.
# You can download the sample data at 
# http://www.pythonlearn.com/code/mbox-short.txt when you are testing 
# below enter mbox-short.txt as the file name.

# Ask user to enter file
fname = raw_input('Please introduce a file name: ')

try:
	fhand = open(fname) # load the file
except:
	print 'There was an error with the file name: ', fname
	exit()

count = 0
spam_average = 0

for line in fhand:
	if not 'X-DSPAM-Confidence:' in line:
		continue

	pos = line.find(':') # Obtain position in line where ':' is located
	spam_average = spam_average + float(line[pos+1:]) # Obtain only the numeric value and add it to the cumulative
	count = count + 1 

spam_average = spam_average/count
print 'Average spam confidence: ', spam_average