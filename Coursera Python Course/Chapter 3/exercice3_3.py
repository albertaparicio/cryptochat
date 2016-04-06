
try:
    hours = int(raw_input('Enter hours: '))
    rate = int(raw_input('Enter rate: '))
    aux = 0
except:
    print 'Please introduce valid numbers'

if hours > 40:
    pay = 40*rate + (hours-40)*1.5*rate
else:
    pay = hours * rate
    
print 'Pay: ', pay, 'Eur'