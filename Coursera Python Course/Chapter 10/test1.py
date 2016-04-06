# tupples are immutable like strings
# list = [1,2,3]; list[1] = 0 WORKS
# tupple = (1,2,3); tupple[1] = 0 ERROR

(0, 2, 10) < (1, 20, 11) # Compara element a element, fins que troba que es cumpleix l'inequacio
('Jones', 'Sally') < ('Jones', 'Fred')

d = {'a':10,'b':1,'c':22} # create a dictionary
t = d.items() # create a list of tupples
print t
t.sort() # since tupples can be compared, a list of tupples can be sorted!
print t