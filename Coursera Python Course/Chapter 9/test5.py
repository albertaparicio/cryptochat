name = raw_input("Enter File: ")
handle = open(name, 'r')
text = handle.read() # save the whole text... since it is not too large!
words = text.split()

counts = dict()
for word in words:
	counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word, count in counts.items(): # items() creates a list of tupples
	if bigcount is None or count > bigcount: # si es la primera iteracio (None) o trobo un item amb mes aparicions q l'actual (count>bigcount), quedat amb aquest valor!
		bigword = word
		bigcount = count

print bigword, bigcount