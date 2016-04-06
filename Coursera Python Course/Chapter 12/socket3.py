# stablish a connection and load a web file, but even faster
import urllib
web = raw_input('Enter the web URL: http://www.')
fhand = urllib.urlopen('http://www.'+web)

for line in fhand:
	print line.strip()
