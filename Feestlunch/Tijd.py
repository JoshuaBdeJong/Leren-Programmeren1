print ('Hoeveel tijd is er nog in de dag over?')

uur = int (input ('Welk uur is het? '))
minuten = int (input ('Welke minuut is het? '))

uur_in_dag = float (2400)

tijd = uur + minuten

tijd_over = uur_in_dag - tijd
print (tijd_over)