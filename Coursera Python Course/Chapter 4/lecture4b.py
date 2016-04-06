def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
def addtwo(a,b):
    return a+b

print greet('en'), 'Bastard'
print greet('es'), 'Bastard'
print greet('fr'), 'Bastard'

x = addtwo(3,5)
print x