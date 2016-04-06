
counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
	counts[name] = counts.get(name,0) + 1 # it creates or updates the entry under key "name"
print counts

# counts.get(name,0) is equivalent to:
# 
# if name in counts:
# 	print counts[name]
# else:
#	print 0