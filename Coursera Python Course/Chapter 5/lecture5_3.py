smallest_so_far = None

for num in [9,15,3,25,70,1]:
    if smallest_so_far is None:
        smallest_so_far = num
    elif num < smallest_so_far:
        smallest_so_far = num

print "Smallest so far: ", smallest_so_far