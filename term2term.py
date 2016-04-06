import sys

term = sys.argv[1];

t_file = open(term, 'w');

while true
    message = raw_input('Message: '); # In next versions, username could be shown
    print message;
    t_file.write()
