jjj = ['a':1,'b':2,'c':3]
print list(jjj) # Converts into list and prints the keys
print jjj.keys() # prints the keys
print jjj.values() # prints the values
print jjj.items() # prints tupples.

for aaa,bbb in jjj.items(): # 2 variables in the loop iteration! (key,value)
	print aaa,bbb