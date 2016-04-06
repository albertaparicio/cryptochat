# count which words how many times appear in a list of strings

counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
	if name not in counts:
		counts[name] = 1
	else:
		counts[name] = counts[name]+1

print counts