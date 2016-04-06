# Sort by the values
c = {'a':10,'b':1,'c':22}
tmp = list()

# copy the content of the tupple into a temporary variable of type list
for k,v in c.items():
	tmp.append((k,v)) # Note: Value first, Key second!

print tmp

tmp.sort(reverse=True) # de gran a petit

